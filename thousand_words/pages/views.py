from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.shortcuts import render
from django.urls import reverse_lazy


class PageAPIView(TemplateView):
    template_name = 'pages/api_page.html'
