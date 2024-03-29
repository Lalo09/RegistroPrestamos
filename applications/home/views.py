from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import TemplateView

class HomePage(LoginRequiredMixin,TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy('users_app:login') #Indicar que si no hay usuario entonces enviar a login
