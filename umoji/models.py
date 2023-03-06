from django.db import models

# articles/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('announcements')

class Wsf(models.Model):
    title = models.CharField(max_length=200)
    wsf_prayers = models.TextField()
    wsf_outline = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Kap(models.Model):
    title = models.CharField(max_length=200)
    prayers = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class ServiceReport(models.Model):
    body = models.TextField()
    Income_report = models.TextField()
    message_title = models.CharField(max_length=40)
    service_sequence = models.CharField(max_length=3)
    number_of_males = models.CharField(max_length=10)
    number_of_females = models.CharField(max_length=10)
    number_of_children = models.CharField(max_length=10)
    number_of_first_timers = models.CharField(max_length=10)
    number_of_new_converts = models.CharField(max_length=10)
    number_of_cars = models.CharField(max_length=10)
    Total_attendace = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class ManagementReport(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    Income_report = models.TextField()
    service_unit = models.CharField(max_length=40)
    message_title = models.CharField(max_length=40)
    service_sequence = models.CharField(max_length=3)
    number_of_males = models.CharField(max_length=10)
    number_of_females = models.CharField(max_length=10)
    number_of_children = models.CharField(max_length=10)
    number_of_first_timers = models.CharField(max_length=10)
    number_of_new_converts = models.CharField(max_length=10)
    number_of_cars = models.CharField(max_length=10)
    Total_attendace = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class WsfLeaders(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    wsf_centre_name = models.CharField(max_length=40)
    number_of_males = models.CharField(max_length=10)
    number_of_females = models.CharField(max_length=10)
    number_of_children = models.CharField(max_length=10)
    number_of_first_timers = models.CharField(max_length=10)
    number_of_new_converts = models.CharField(max_length=10)
    Total_attendace = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Media(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    testifier_name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])