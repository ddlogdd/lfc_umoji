from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Announcement

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AnnouncementPageView(ListView):
    template_name = 'announcements.html'
    model = Announcement

class WorkersPageView(TemplateView):
    template_name = 'workers.html'

class PastorPageView(TemplateView):
    template_name = 'pastor_desk.html'

class CmcPageView(TemplateView):
    template_name = 'cmc_desk.html'

class AboutUsPageView(TemplateView):
    template_name = 'about_us.html'

class InfoUpdatePageView(CreateView):
    template_name = 'info_update.html'
    model = Announcement
    fields = ('title', 'body', 'author')



