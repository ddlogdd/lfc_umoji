from django import forms
from django.forms import ModelForm
from.models import Church, ManagementReport, ServiceReport, WsfLeaders, Media, Kap, Wsf, Announcement

class ChurchForm(ModelForm):
    class Meta:
        model = Church
        fields = ('title', 'body', 'total_sunday_attendance', 'avg_sunday_attendance', 'total_midweek_attendance', 'avg_midweek_attendance',  'avg_adults', 'avg_children', 'avg_chop', 'no_of_wsf', 'bfc', 'highest_sunday_attendance', 'highest_midweek_attendance','first_timers', 'new_converts', 'Total_income',)
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body' :forms.TextInput(attrs={'class':'form-control'}),
            'total_sunday_attendance' :forms.NumberInput(attrs={'class':'form-control'}),
            'avg_sunday_attendance' :forms.NumberInput(attrs={'class':'form-control'}),
            'total_midweek_attendance' :forms.NumberInput(attrs={'class':'form-control'}),
            'avg_midweek_attendance' :forms.NumberInput(attrs={'class':'form-control'}),
            'avg_adults' :forms.NumberInput(attrs={'class':'form-control'}),
            'avg_children' :forms.NumberInput(attrs={'class':'form-control'}),
            'avg_chop' :forms.NumberInput(attrs={'class':'form-control'}),
            'avg_wsf' :forms.NumberInput(attrs={'class':'form-control'}), 
            'no_of_wsf' :forms.NumberInput(attrs={'class':'form-control'}),
            'bfc' :forms.NumberInput(attrs={'class':'form-control'}),
            'highest_sunday_attendance' :forms.NumberInput(attrs={'class':'form-control'}),
            'highest_midweek_attendance' :forms.NumberInput(attrs={'class':'form-control'}),
            'first_timers' :forms.NumberInput(attrs={'class':'form-control'}),
            'new_converts' :forms.NumberInput(attrs={'class':'form-control'}),
            'Total_income' :forms.NumberInput(attrs={'class':'form-control'}),
            
            
        }
class ManagementReportForm(ModelForm):
    class Meta:
        model = ManagementReport
        fields = ( 'message_title', 'body', 'Income_report',  'service_sequence', 'number_of_cars', 'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace',)
        widgets = {
            'message_title':forms.TextInput(attrs={'class':'form-control'}),
            'body' :forms.TextInput(attrs={'class':'form-control'}),
            'Income_report':forms.TextInput(attrs={'class':'form-control'}),
            'service_sequence' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_cars' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_males' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_females':forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_children' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_first_timers' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_new_converts' :forms.NumberInput(attrs={'class':'form-control'}), 
            'Total_attendace' :forms.NumberInput(attrs={'class':'form-control'}),
        }

class ServiceReportForm(ModelForm):
    class Meta:
        model = ServiceReport
        fields = ( 'message_title', 'body', 'Income_report',  'service_sequence', 'number_of_cars', 'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace',)
        widgets = {
            'message_title':forms.TextInput(attrs={'class':'form-control'}),
            'body' :forms.TextInput(attrs={'class':'form-control'}),
            'Income_report':forms.TextInput(attrs={'class':'form-control'}),
            'service_sequence' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_cars' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_males' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_females':forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_children' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_first_timers' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_new_converts' :forms.NumberInput(attrs={'class':'form-control'}), 
            'Total_attendace' :forms.NumberInput(attrs={'class':'form-control'}),
    }

class WsfLeadersForm(ModelForm):
    class Meta:
        model = WsfLeaders
        fields = ( 'title', 'body', 'wsf_centre_name',  'number_of_males', 'number_of_females', 'number_of_children', 'number_of_first_timers', 'number_of_new_converts', 'Total_attendace',)
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body' :forms.TextInput(attrs={'class':'form-control'}),
            'wsf_centre_name':forms.TextInput(attrs={'class':'form-control'}),
            'number_of_males' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_females':forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_children' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_first_timers' :forms.NumberInput(attrs={'class':'form-control'}),
            'number_of_new_converts' :forms.NumberInput(attrs={'class':'form-control'}), 
            'Total_attendace' :forms.NumberInput(attrs={'class':'form-control'}),
    } 

class MediaForm(ModelForm):
    class Meta:
        model = Media
        fields = ('title', 'body', 'testifier_name',) 
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body' :forms.TextInput(attrs={'class':'form-control'}),
            'testifier_name':forms.TextInput(attrs={'class':'form-control'}),
    } 

class KapForm(ModelForm):
    class Meta:
        model = Kap
        fields = ('title', 'prayers', 'message',) 
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'prayers' :forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'}),
    } 

class WsfForm(ModelForm):
    class Meta:
        model = Wsf
        fields = ('title', 'wsf_prayers', 'wsf_outline', )
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'wsf_prayers' :forms.TextInput(attrs={'class':'form-control'}),
            'wsf_outline':forms.TextInput(attrs={'class':'form-control'}),
    } 

class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'body', )
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body' :forms.TextInput(attrs={'class':'form-control'}),
            
     }
