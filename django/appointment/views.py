from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class HomeTemplateView(TemplateView):
    template_name = "index.html"