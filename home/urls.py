from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sobre-mim', views.AboutView.as_view(), name='about-me'),
    path('portfolio', views.PortfolioView.as_view(), name='portfolio'),
    path('entre-em-contato', views.ContactMeView.as_view(), name='contact-me')
]
