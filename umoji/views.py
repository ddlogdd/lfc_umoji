from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin
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

class PastorPageView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'pastor_desk.html'
    login_url ='login'
    permission_required = 'umoji.pastor alone'

class CmcPageView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'cmc_desk.html'
    login_url ='login'
    permission_required = 'umoji.elder'

class AboutUsPageView(TemplateView):
    template_name = 'about_us.html'

class InfoUpdatePageView(LoginRequiredMixin, CreateView):
    template_name = 'info_update.html'
    model = Announcement
    form_class = AnnouncementForm
    login_url ='login'
    permission_required = 'umoji.pastor alone'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class InfoUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'info_update_edit.html'
    login_url ='login'
    permission_required = 'umoji.pastor alone'
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
    permission_required = 'umoji.pastor alone'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WsfOperationsPageView(ListView):
    template_name = 'wsf_operations.html'
    model = Wsf
class WsfUpdatePageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'wsf_update.html'
    model = Wsf
    form_class = WsfForm
    login_url ='login'
    permission_required = 'umoji.pastor alone'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class WsfUpdateEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView): 
    model = Wsf
    form_class = WsfForm
    template_name = 'wsf_update_edit.html'
    login_url ='login'
    permission_required = 'umoji.pastor alone'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WsfUpdateDetailView(DetailView): 
    model = Wsf
    template_name = 'wsf_update_detail.html'

class WsfUpdateDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView): # new
    model = Wsf
    template_name = 'wsf_update_delete.html'
    success_url = reverse_lazy('wsf_update')
    login_url ='login'
    permission_required = 'umoji.pastor alone'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class KingdomAdvancementPrayersView(ListView):
    template_name = 'kingdom_advancement_prayers.html'
    model = Kap
    

class KapUpdatePageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'kap_update.html'
    model = Kap
    form_class = KapForm
    login_url ='login'
    permission_required = 'umoji.pastor alone'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class KapUpdateEditView(LoginRequiredMixin, UpdateView): 
    model = Kap
    form_class = KapForm
    template_name = 'kap_update_edit.html'
    login_url ='login'
    permission_required = 'umoji.pastor alone'
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
    permission_required = 'umoji.pastor alone'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class TestimoniesView(ListView):
    template_name = 'testimonies.html'
    model = Media

class MediaUpdatePageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'media_update.html'
    model = Media
    login_url ='login'
    permission_required = 'umoji.media'
    form_class = MediaForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class MediaUpdateEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView): 
    model = Media
    form_class = MediaForm
    template_name = 'media_update_edit.html'
    login_url ='login'
    permission_required = 'umoji.media'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class MediaUpdateDetailView(DetailView): 
    model = Media
    template_name = 'media_update_detail.html'

class MediaUpdateDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView): # new
    model = Media
    template_name = 'media_update_delete.html'
    success_url = reverse_lazy('media_update')
    login_url ='login'
    permission_required = 'umoji.media'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WsfReportView(LoginRequiredMixin, ListView):
    template_name = 'wsf_report.html'
    model = WsfLeaders
    login_url ='login'

class WsfLeadersUpdatePageView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'wsf_leaders_update.html'
    model = WsfLeaders
    login_url ='login'
    form_class = WsfLeadersForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    permission_required = 'umoji.special'
class WsfLeadersUpdateEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView): 
    model = WsfLeaders
    form_class = WsfLeadersForm
    template_name = 'wsf_leaders_update_edit.html'
    login_url ='login'
    permission_required = 'umoji.special'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class WsfLeadersUpdateDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView): 
    model = WsfLeaders
    template_name = 'wsfleaders_update_detail.html'
    login_url ='login'
    permission_required = 'umoji.special_status'

class WsfLeadersUpdateDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView): # new
    model = WsfLeaders
    template_name = 'wsf_leaders_update_delete.html'
    success_url = reverse_lazy('wsf_leaders_update')
    login_url ='login'
    permission_required = 'umoji.special'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class UshersReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView): 
    template_name = 'ushers_report.html'
    model = ServiceReport
    login_url ='login'
    permission_required = 'umoji.ushers'

class UshersUpdatePageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'ushers_update.html'
    model = ServiceReport
    form_class = ServiceReportForm
    login_url ='login'
    permission_required = 'umoji.ushers alone'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class UshersUpdateEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView): 
    model = ServiceReport
    form_class = ServiceReportForm
    template_name = 'ushers_update_edit.html'
    login_url ='login'
    permission_required = 'umoji.ushers alone'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class UshersUpdateDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView): 
    model = ServiceReport
    template_name = 'ushers_update_detail.html'
    login_url ='login'
    permission_required = 'umoji.ushers'
    

class UshersUpdateDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView): # new
    model = ServiceReport
    template_name = 'ushers_update_delete.html'
    success_url = reverse_lazy('ushers_update')
    login_url ='login'
    permission_required = 'umoji.ushers alone'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CmcReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView): 
    template_name = 'cmc_report.html'
    model = ManagementReport
    login_url ='login'
    permission_required = 'umoji.access'

class CmcUpdatePageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'cmc_updates.html'
    model = ManagementReport
    login_url ='login'
    form_class = ManagementReportForm
    permission_required = 'umoji.elder'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class CmcUpdateEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView): 
    model = ManagementReport
    form_class = ManagementReportForm
    template_name = 'cmc_update_edit.html'
    login_url ='login'
    permission_required = 'umoji.elder'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class CmcUpdateDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView): 
    model = ManagementReport
    template_name = 'cmc_update_detail.html'
    login_url ='login'
    permission_required = 'umoji.access'

class CmcUpdateDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView): # new
    model = ManagementReport
    template_name = 'cmc_update_delete.html'
    success_url = reverse_lazy('cmc_updates')
    permission_required =  'umoji.elder'
    login_url ='login'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ChurchReportView(LoginRequiredMixin, PermissionRequiredMixin, ListView): 
    template_name = 'church_report.html'
    model = Church
    login_url ='login'
    permission_required = 'umoji.pastor'

class ChurchUpdatePageView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'church_updates.html'
    login_url ='login'
    model = Church
    form_class = ChurchForm
    permission_required = 'umoji.pastor alone'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class ChurchUpdateEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView): 
    model = Church
    form_class = ChurchForm
    template_name = 'church_update_edit.html'
    login_url ='login'
    permission_required = 'umoji.pastor alone'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ChurchUpdateDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView): 
    model = Church
    template_name = 'church_update_detail.html'
    login_url ='login'
    permission_required = 'umoji.pastor'

class ChurchUpdateDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView): # new
    model = Church
    template_name = 'church_update_delete.html'
    success_url = reverse_lazy('church_updates')
    login_url ='login'
    permission_required = 'umoji.pastor alone'
    def dispatch(self, request, *args, **kwargs): 
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


