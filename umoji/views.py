from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Announcement, Wsf, Kap, Media, WsfLeaders, ServiceReport, ManagementReport, Church
from .forms import ChurchForm, ManagementReportForm, ServiceReportForm, WsfLeadersForm, MediaForm, KapForm, WsfForm, AnnouncementForm
from django.urls import reverse_lazy, reverse

# Create your views here.

class AnnouncementPageView(ListView):
    template_name = 'announcements.html'
    model = Announcement

class WorkersPageView(LoginRequiredMixin, TemplateView):
    template_name = 'workers.html'
    login_url ='login'

class PastorPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pastor_desk.html'
    login_url ='login'

class CmcPageView(LoginRequiredMixin, TemplateView):
    template_name = 'cmc_desk.html'
    login_url ='login'

class AboutUsPageView(TemplateView):
    template_name = 'about_us.html'

class InfoUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'info_update.html'
    model = Announcement
    form_class = AnnouncementForm
    login_url ='login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class InfoUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'info_update_edit.html'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class InfoUpdateDetailView(DetailView): 
    model = Announcement
    template_name = 'info_update_detail.html'

class InfoUpdateDeleteView(LoginRequiredMixin, DeleteView): 
    model = Announcement
    template_name = 'info_update_delete.html'
    success_url = reverse_lazy('info_update')
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WsfOperationsPageView(ListView):
    template_name = 'wsf_operations.html'
    model = Wsf
class WsfUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'wsf_update.html'
    model = Wsf
    form_class = WsfForm
    login_url ='login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WsfUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = Wsf
    form_class = WsfForm
    template_name = 'wsf_update_edit.html'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WsfUpdateDetailView(DetailView): 
    model = Wsf
    template_name = 'wsf_update_detail.html'

class WsfUpdateDeleteView(LoginRequiredMixin, DeleteView): # new
    model = Wsf
    template_name = 'wsf_update_delete.html'
    success_url = reverse_lazy('wsf_update')
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class KingdomAdvancementPrayersView(ListView):
    template_name = 'kingdom_advancement_prayers.html'
    model = Kap
    

class KapUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'kap_update.html'
    model = Kap
    form_class = KapForm
    login_url ='login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class KapUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = Kap
    form_class = KapForm
    template_name = 'kap_update_edit.html'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class KapUpdateDetailView(DetailView): 
    model = Kap
    template_name = 'kap_update_detail.html'

class KapUpdateDeleteView(LoginRequiredMixin, DeleteView): # new
    model = Kap
    template_name = 'kap_update_delete.html'
    success_url = reverse_lazy('kap_update')
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class TestimoniesView(ListView):
    template_name = 'testimonies.html'
    model = Media

class MediaUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'media_update.html'
    model = Media
    login_url ='login'
    form_class = MediaForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MediaUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = Media
    form_class = MediaForm
    template_name = 'media_update_edit.html'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class MediaUpdateDetailView(DetailView): 
    model = Media
    template_name = 'media_update_detail.html'

class MediaUpdateDeleteView(LoginRequiredMixin, DeleteView): # new
    model = Media
    template_name = 'media_update_delete.html'
    success_url = reverse_lazy('media_update')
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WsfReportView(LoginRequiredMixin, ListView):
    template_name = 'wsf_report.html'
    model = WsfLeaders
    login_url ='login'

class WsfLeadersUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'wsf_leaders_update.html'
    model = WsfLeaders
    login_url ='login'
    form_class = WsfLeadersForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class WsfLeadersUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = WsfLeaders
    form_class = WsfLeadersForm
    template_name = 'wsf_leaders_update_edit.html'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WsfLeadersUpdateDetailView(LoginRequiredMixin, DetailView): 
    model = WsfLeaders
    template_name = 'wsfleaders_update_detail.html'
    login_url ='login'

class WsfLeadersUpdateDeleteView(LoginRequiredMixin, DeleteView): # new
    model = WsfLeaders
    template_name = 'wsf_leaders_update_delete.html'
    success_url = reverse_lazy('wsf_leaders_update')
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class UshersReportView(LoginRequiredMixin, ListView): 
    template_name = 'ushers_report.html'
    model = ServiceReport
    login_url ='login'

class UshersUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'ushers_update.html'
    model = ServiceReport
    form_class = ServiceReportForm
    login_url ='login'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class UshersUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = ServiceReport
    form_class = ServiceReportForm
    template_name = 'ushers_update_edit.html'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class UshersUpdateDetailView(LoginRequiredMixin, DetailView): 
    model = ServiceReport
    template_name = 'ushers_update_detail.html'
    login_url ='login'

class UshersUpdateDeleteView(LoginRequiredMixin, DeleteView): # new
    model = ServiceReport
    template_name = 'ushers_update_delete.html'
    success_url = reverse_lazy('ushers_update')
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CmcReportView(LoginRequiredMixin, ListView): 
    template_name = 'cmc_report.html'
    model = ManagementReport
    login_url ='login'

class CmcUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'cmc_updates.html'
    model = ManagementReport
    login_url ='login'
    form_class = ManagementReportForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class CmcUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = ManagementReport
    form_class = ManagementReportForm
    template_name = 'cmc_update_edit.html'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CmcUpdateDetailView(LoginRequiredMixin, DetailView): 
    model = ManagementReport
    template_name = 'cmc_update_detail.html'
    login_url ='login'

class CmcUpdateDeleteView(LoginRequiredMixin, DeleteView): # new
    model = ManagementReport
    template_name = 'cmc_update_delete.html'
    success_url = reverse_lazy('cmc_updates')
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ChurchReportView(LoginRequiredMixin, ListView): 
    template_name = 'church_report.html'
    model = Church
    login_url ='login'

class ChurchUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'church_updates.html'
    login_url ='login'
    model = Church
    form_class = ChurchForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class ChurchUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = Church
    form_class = ChurchForm
    template_name = 'church_update_edit.html'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ChurchUpdateDetailView(LoginRequiredMixin, DetailView): 
    model = Church
    template_name = 'church_update_detail.html'
    login_url ='login'

class ChurchUpdateDeleteView(LoginRequiredMixin, DeleteView): # new
    model = Church
    template_name = 'church_update_delete.html'
    success_url = reverse_lazy('church_updates')
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)






