from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactMeView(TemplateView):
    template_name = 'home/contact-me.html'


class PortfolioView(TemplateView):
    template_name = 'home/portfolio.html'
