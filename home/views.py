from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'


class AboutView(TemplateView):
    template_name = 'home/about.html'


class ContactMeView(TemplateView):
    template_name = 'home/contact-me.html'


class PortfolioView(TemplateView):
    template_name = 'home/portfolio.html'
    projects = {
        'fub': {},
        'devops': {},
        'blog': {},
        'none': {}
    }

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context['available_projects'] = self.projects
        context['project'] = self.__get_project(self.request.GET.get('projeto'))
        return context

    def __get_project(self, project_key):
        project = self.projects.get(project_key)

        if not project:
            return self.projects.get('none')

        return project
