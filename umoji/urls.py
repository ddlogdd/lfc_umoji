from django.urls import path
from .views import HomePageView, AnnouncementPageView, WorkersPageView, PastorPageView, CmcPageView, AboutUsPageView, InfoUpdatePageView

urlpatterns = [
    path('info_update/', InfoUpdatePageView.as_view(), name='info_update'),
    path('about_us/', AboutUsPageView.as_view(), name='about_us'),
    path('cmc/', CmcPageView.as_view(), name='cmc'),
    path('pastor/', PastorPageView.as_view(), name='pastor'),
    path('workers/', WorkersPageView.as_view(), name='workers'),
    path('announcement/', AnnouncementPageView.as_view(), name='announcements'),
    path('', HomePageView.as_view(), name='home'),
    
]



