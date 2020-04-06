from django.urls import path
from .views import HomeTemplateView
from . import views

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('works/', views.works, name='works'),
]
