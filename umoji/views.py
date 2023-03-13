from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Announcement, Wsf, Kap, Media, WsfLeaders, ServiceReport, ManagementReport, Church
from django.urls import reverse_lazy, reverse

# Create your views here.

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

class InfoUpdateEditView(UpdateView): 
    model = Announcement
    fields = ('title', 'body',)
    template_name = 'info_update_edit.html'

class InfoUpdateDetailView(DetailView): 
    model = Announcement
    template_name = 'info_update_detail.html'

class InfoUpdateDeleteView(DeleteView): # new
    model = Announcement
    template_name = 'info_update_delete.html'
    success_url = reverse_lazy('info_update')

class WsfOperationsPageView(ListView):
    template_name = 'wsf_operations.html'
    model = Wsf
class WsfUpdatePageView(CreateView):
    template_name = 'wsf_update.html'
    model = Wsf
    fields = ('title', 'wsf_prayers', 'wsf_outline', 'author')

class WsfUpdateEditView(UpdateView): 
    model = Wsf
    fields = ('title', 'wsf_prayers', 'wsf_outline', 'author')
    template_name = 'wsf_update_edit.html'

class WsfUpdateDetailView(DetailView): 
    model = Wsf
    template_name = 'wsf_update_detail.html'

class WsfUpdateDeleteView(DeleteView): # new
    model = Wsf
    template_name = 'wsf_update_delete.html'
    success_url = reverse_lazy('wsf_update')

class KingdomAdvancementPrayersView(ListView):
    template_name = 'kingdom_advancement_prayers.html'
    model = Kap
    

class KapUpdatePageView(CreateView):
    template_name = 'kap_update.html'
    model = Kap
    fields = ('title', 'prayers', 'message', 'author')

class KapUpdateEditView(UpdateView): 
    model = Kap
    fields = ('title', 'prayers', 'message', 'author')
    template_name = 'kap_update_edit.html'

class KapUpdateDetailView(DetailView): 
    model = Kap
    template_name = 'kap_update_detail.html'

class KapUpdateDeleteView(DeleteView): # new
    model = Kap
    template_name = 'kap_update_delete.html'
    success_url = reverse_lazy('kap_update')

class TestimoniesView(ListView):
    template_name = 'testimonies.html'
    model = Media

class MediaUpdatePageView(CreateView):
    template_name = 'media_update.html'
    model = Media
    fields = ('title', 'body', 'testifier_name', 'author')

class MediaUpdateEditView(UpdateView): 
    model = Media
    fields = ('title', 'body', 'testifier_name', 'author')
    template_name = 'media_update_edit.html'

class MediaUpdateDetailView(DetailView): 
    model = Media
    template_name = 'media_update_detail.html'

class MediaUpdateDeleteView(DeleteView): # new
    model = Media
    template_name = 'media_update_delete.html'
    success_url = reverse_lazy('media_update')

class WsfReportView(ListView):
    template_name = 'wsf_report.html'
    model = WsfLeaders

class WsfLeadersUpdatePageView(CreateView):
    template_name = 'wsf_leaders_update.html'
    model = WsfLeaders
    fields = ('title', 'body', 'wsf_centre_name', 'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace', 'author')

class WsfLeadersUpdateEditView(UpdateView): 
    model = WsfLeaders
    fields = ('title', 'body', 'wsf_centre_name', 'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace', 'author')
    template_name = 'wsf_leaders_update_edit.html'

class WsfLeadersUpdateDetailView(DetailView): 
    model = WsfLeaders
    template_name = 'wsfleaders_update_detail.html'

class WsfLeadersUpdateDeleteView(DeleteView): # new
    model = WsfLeaders
    template_name = 'wsf_leaders_update_delete.html'
    success_url = reverse_lazy('wsf_leaders_update')

class UshersReportView(ListView): 
    template_name = 'ushers_report.html'
    model = ServiceReport

class UshersUpdatePageView(CreateView):
    template_name = 'ushers_update.html'
    model = ServiceReport
    fields = ( 'body', 'Income_report', 'message_title', 'service_sequence', 'number_of_cars', 'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace', 'author')

class UshersUpdateEditView(UpdateView): 
    model = ServiceReport
    fields = ( 'body', 'Income_report', 'message_title', 'service_sequence', 'number_of_cars', 'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace', 'author')
    template_name = 'ushers_update_edit.html'

class UshersUpdateDetailView(DetailView): 
    model = ServiceReport
    template_name = 'ushers_update_detail.html'

class UshersUpdateDeleteView(DeleteView): # new
    model = ServiceReport
    template_name = 'ushers_update_delete.html'
    success_url = reverse_lazy('ushers_update')

class CmcReportView(ListView): 
    template_name = 'cmc_report.html'
    model = ManagementReport

class CmcUpdatePageView(CreateView):
    template_name = 'cmc_updates.html'
    model = ManagementReport
    fields = ( 'body', 'Income_report', 'message_title', 'service_sequence', 'number_of_cars', 'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace', 'author',)

class CmcUpdateEditView(UpdateView): 
    model = ManagementReport
    fields = ( 'body', 'Income_report', 'message_title', 'service_sequence', 'number_of_cars', 'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace', 'author',)
    template_name = 'cmc_update_edit.html'

class CmcUpdateDetailView(DetailView): 
    model = ManagementReport
    template_name = 'cmc_update_detail.html'

class CmcUpdateDeleteView(DeleteView): # new
    model = ManagementReport
    template_name = 'cmc_update_delete.html'
    success_url = reverse_lazy('cmc_updates')

class ChurchReportView(ListView): 
    template_name = 'church_report.html'
    model = Church

class ChurchUpdatePageView(CreateView):
    template_name = 'church_updates.html'
    model = Church
    fields = ('title', 'body', 'total_sunday_attendance', 'avg_sunday_attendance',   'avg_adults', 'avg_children', 'avg_chop', 'avg_wsf', 'no_of_wsf', 'bfc', 'highest_sunday_attendance', 'first_timers', 'new_converts', 'Total_income', 'author')

class ChurchUpdateEditView(UpdateView): 
    model = Church
    fields = ( 'title', 'body', 'total_sunday_attendance', 'avg_sunday_attendance',   'avg_adults', 'avg_children', 'avg_chop', 'avg_wsf', 'no_of_wsf', 'bfc', 'highest_sunday_attendance', 'first_timers', 'new_converts', 'Total_income', 'author')
    template_name = 'church_update_edit.html'

class ChurchUpdateDetailView(DetailView): 
    model = Church
    template_name = 'church_update_detail.html'

class ChurchUpdateDeleteView(DeleteView): # new
    model = Church
    template_name = 'church_update_delete.html'
    success_url = reverse_lazy('church_updates')






