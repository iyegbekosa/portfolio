from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'cover.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class FinderrView(TemplateView):
    template_name = 'finderr.html'

class PriceView(TemplateView):
    template_name = 'pricing.html'

class ServiceView(TemplateView):
    template_name = 'services.html'

class ProjectView(TemplateView):
    template_name = 'projects.html'