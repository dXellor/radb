from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),
    path('update_zelje', views.update_zelje, name='update_zelje'),
    path('rang-lists', views.rang_lists, name='rang-lists'),
    path('support', views.support, name='support')
]