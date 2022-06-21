import email
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User
from data.models import Predmet, Ocena
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from helpers.decorators import deny_for_logged_in
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.conf import settings
from .utils import generate_token 
import re
import threading

regex = "([a-z])+.ra[0-9]+.[0-9]+@uns.ac.rs"

class mailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_verif_email(user, request):
    current_site = get_current_site(request)
    subject = "Aktivirajte Vaš nalog"
    body = render_to_string('user_auth/verification.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
        })

    email_message = EmailMessage(subject=subject, body=body,
                                from_email=settings.EMAIL_FROM_USER,
                                to=[user.email])

    mailThread(email_message).start()

@deny_for_logged_in
def login_user(request):

    if request.method == 'POST':
        context = {'data': request.POST, 'verified': True}

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if not user:
            messages.add_message(request, messages.ERROR, 'Podaci koji su uneti nisu validni.')
            return render(request, 'user_auth/login.html', context)

        if not user.is_verified:
            messages.add_message(request, messages.ERROR, 'Vaš nalog nije aktiviran, proverite Vaš inbox.')
            context['verified'] = False
            return render(request, 'user_auth/login.html', context) #zahtev za ponovno slanje emaila

        login(request, user)
        messages.add_message(request, messages.SUCCESS, 'Uspešno ste prijavljeni!')
        return redirect(reverse('profile'))

    return render(request, 'user_auth/login.html', {'verified': True})

def logout_user(request):

    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Uspešno ste odjavljeni!')

    return redirect(reverse('login'))

@deny_for_logged_in
def register(request):

    if request.method=='POST':
        context = {'error': False, 'data': request.POST}
        
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2') 

        if not re.search(regex, email):
            messages.add_message(request, messages.ERROR, 'Niste uneli validan UNS email. Šablon: prezime.raXX.20XX@uns.ac.rs')
            context['error'] = True
        else:
            #simic.ra32.2020@uns.ac.rs
            x = email.split('.')
            indeks = x[1].upper() + "/" +  x[2].split('@')[0]

        if len(password) < 6:
            messages.add_message(request, messages.ERROR, 'Šifra mora da bude barem 6 karaktera dugačka')
            context['error'] = True

        if password!=password2:
            messages.add_message(request, messages.ERROR, 'Šifre se ne poklapaju')
            context['error'] = True

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, 'Već postoji nalog koji koristi ovaj email. U slučaju da Vam je neko uzeo nalog možete nas kontaktirati ovde: link')
            context['error'] = True

        if context['error']:
            return render(request, 'user_auth/register.html', context)
        else:
            user = User.objects.create_user(email=email, first_name=first_name, last_name=last_name, indeks=indeks, modul_prva_zelja = 'Neopredeljen',
                modul_druga_zelja = 'Neopredeljen')
            user.set_password(password)
            user.save()

            send_verif_email(user, request)

            predmeti = Predmet.objects.all()
            for predmet in predmeti:
                nova_ocena = Ocena()
                nova_ocena.predmet_id = predmet
                nova_ocena.student_id = user
                nova_ocena.ocena = 5
                nova_ocena.save()

            messages.add_message(request, messages.INFO, 'Na Vaš email je poslat link za aktivaciju naloga. Proverite Vaš inbox.')

            return redirect('login')


    return render(request, 'user_auth/register.html')

@deny_for_logged_in
def verify(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user:
        if user.is_verified:
            messages.add_message(request, messages.INFO, 'Vaš nalog je već aktiviran')
            return redirect(reverse('login'))
        elif generate_token.check_token(user, token):
            user.is_verified = True
            user.save()

            messages.add_message(request, messages.SUCCESS, 'Uspešno ste aktivirali nalog. Možete se prijaviti.')
            return redirect(reverse('login'))
        else:
            return render(request, 'user_auth/verification_failed.html', {'uidb64': uidb64})

    messages.add_message(request, messages.ERROR, 'Došlo je do greške u sistemu.')
    return redirect(reverse('login'))

def request_verif_email(request, uidb64):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)

    send_verif_email(user, request)
    messages.add_message(request, messages.INFO, 'Na Vaš email je poslat link za aktivaciju naloga. Proverite Vaš inbox.')

    return redirect(reverse('login'))

@deny_for_logged_in
def request_verif_email_form(request):

    if request.method == "POST":
        context = {'data': request.POST}
        email = request.POST.get('email')
        user = User.objects.filter(email=email)

        if not user:
            messages.add_message(request, messages.ERROR, 'Email koji ste uneli ne pripada nijednom registrovanom nalogu')
            return render(request, 'user_auth/request_verification_email.html', context)
        else:
            send_verif_email(user[0], request)
            messages.add_message(request, messages.INFO, 'Na Vaš email je poslat link za aktivaciju naloga. Proverite Vaš inbox.')
            return redirect(reverse('login'))

    return render(request, 'user_auth/request_verification_email.html')

