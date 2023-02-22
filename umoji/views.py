from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class IndexPageView(TemplateView):
    template_name = 'index.html'

class WorkersPageView(TemplateView):
    template_name = 'workers.html'

class PastorPageView(TemplateView):
    template_name = 'pastor_desk.html'


class CmcPageView(TemplateView):
    template_name = 'cmc_desk.html'
