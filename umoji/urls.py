from django.urls import path
from .views import HomePageView, IndexPageView, WorkersPageView, PastorPageView, CmcPageView

urlpatterns = [
    path('cmc/', CmcPageView.as_view(), name='cmc'),
    path('pastor/', PastorPageView.as_view(), name='pastor'),
    path('workers/', WorkersPageView.as_view(), name='workers'),
    path('index/', IndexPageView.as_view(), name='index'),
    path('', HomePageView.as_view(), name='home'),
    
]



