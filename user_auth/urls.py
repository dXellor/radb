from site import venv
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('verify/<uidb64>/<token>', views.verify, name='verify'),
    path('request_verif_email_form', views.request_verif_email_form, name='request_verif_email_form'),
    path('request_verif_email/<uidb64>', views.request_verif_email, name='request_verif_email')
]