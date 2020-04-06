from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        # first, call super get context data
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context


def about(request):
    return HttpResponse('<h1>About Page</h1>')


def services(request):
    return HttpResponse('<h1>Services Page</h1>')


def works(request):
    return HttpResponse('<h1>Portfolio Page</h1>')
