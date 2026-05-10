from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'homepage/index.html'


class UserCreateView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('homepage:index')
