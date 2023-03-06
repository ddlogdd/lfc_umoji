from django.urls import path
from .views import SignUpView
urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),
# path('password_change/',  PasswordsChangeView.as_view(template_name='registration/password_change_form.html')),

]