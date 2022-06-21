from math import prod
from django.shortcuts import get_object_or_404, redirect, render
from .models import Ocena
from user_auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from helpers.modulfunctions import *
from helpers.norm import return_score

def index(request):
    return render(request, 'data/index.html')

def about(request):
    return render(request, 'data/about.html')

@login_required
def profile(request):
    sve_ocene = Ocena.objects.filter(student_id=request.user)
    i = 0
    sum = 0
    ostv_espb = 0
    
    context = {'items': sve_ocene}

    if request.method == 'POST':

        for item in sve_ocene:
            tr_ocena = request.POST.get(str(item.predmet_id.pk))
            if tr_ocena == '': tr_ocena = 5
            if tr_ocena != item.ocena:
                update_ocena = get_object_or_404(Ocena, pk=item.pk)
                update_ocena.ocena = tr_ocena
                update_ocena.save()
            if int(tr_ocena) != 5:
                ostv_espb += update_ocena.predmet_id.ESPB
                sum += int(tr_ocena)
                i += 1

        if i == 0:
            prosek = 5.00
        else:
            prosek = round(sum/i, 2)
        request.user.prosek = prosek
        request.user.ostvareni_espb = ostv_espb
        score = return_score(ostv_espb, prosek, request.user.indeks)
        if score == 0:
            messages.add_message(request, messages.WARNING, 'Nemate stečene uslove za upis godine! Vaš Score: 0')
        request.user.modul_score = score
        request.user.save()

        #update upada na zelje
        all_users = User.objects.all()
        returnList(request, all_users, skrati_modul(request.user.modul_prva_zelja), False)
        returnList(request, all_users, skrati_modul(request.user.modul_druga_zelja), False)

        messages.add_message(request, messages.SUCCESS, 'Podaci uspešno ažurirani')

        return HttpResponseRedirect(reverse('profile'))

    return render(request, 'data/profile.html', context)

@login_required
def update_zelje(request):
    
    if request.method == "POST":
        w1 = request.POST.get('modul_wish1')
        w2 = request.POST.get('modul_wish2')

        request.user.modul_prva_zelja = w1
        request.user.modul_druga_zelja = w2
        all_users = User.objects.all()
        returnList(request, all_users, skrati_modul(request.user.modul_prva_zelja), False)
        returnList(request, all_users, skrati_modul(request.user.modul_druga_zelja), False)
        if request.POST.get('ishidden'):
            request.user.hidden = True
        else:
            request.user.hidden = False

        request.user.save()
        messages.add_message(request, messages.SUCCESS, 'Podaci uspešno ažurirani')

        return HttpResponseRedirect(reverse('profile'))

    return redirect(reverse('home'))

@never_cache
@login_required
def rang_lists(request):
    all_users = User.objects.all()
    user_count = all_users.count()
    lista_prni = []
    lista_rtrk = []
    lista_auto = []
    filter = vrati_filter(request)

    #Tabela za prvu zelju mora biti prva ocitana tabela
    if request.user.modul_prva_zelja == 'Primenjene računarske nauke i informatika':
        lista_prni = returnList(request, all_users, 'prni', True)
        lista_rtrk = returnList(request, all_users, 'rtrk', True)
        lista_auto = returnList(request, all_users, 'auto', True)
    elif request.user.modul_prva_zelja == 'Računarska tehnika i računarske komunikacije':
        lista_rtrk = returnList(request, all_users, 'rtrk', True)
        lista_prni = returnList(request, all_users, 'prni', True)
        lista_auto = returnList(request, all_users, 'auto', True)
    else:
        lista_auto = returnList(request, all_users, 'auto', True)
        lista_rtrk = returnList(request, all_users, 'rtrk', True)
        lista_prni = returnList(request, all_users, 'prni', True)
    
    context = {'lprni': lista_prni, 'lrtrk': lista_rtrk, 'lauto': lista_auto, 'user_count': user_count}
    return render(request, 'data/rang-list.html', context)

def support(request):

    return render(request, 'data/support.html')