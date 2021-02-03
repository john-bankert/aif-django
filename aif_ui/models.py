from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Themes(models.Model):
    name = models.CharField(max_length=75, default="")
    font_family = models.CharField(max_length=75, default="Arial, Helvetica, Sans Serif")
    font_size = models.CharField(max_length=10, default="10pt")
    current_theme = models.CharField(max_length=10, default="black")
    navbar_bg_color = models.CharField(max_length=25, default="black")
    navbar_fg_color = models.CharField(max_length=25, default="white")
    navbar_button_fg_color = models.CharField(max_length=25, default="black")
    navbar_button_bg_color = models.CharField(max_length=25, default="#e7e7e7")
    navbar_button_border_color = models.CharField(max_length=25, default="white")
    dropdown_fg_color = models.CharField(max_length=25, default="black")
    dropdown_bg_color = models.CharField(max_length=25, default="#f9f9f9")
    dropdown_hover_color = models.CharField(max_length=25, default="#dddddd")
    menubar_bg_color = models.CharField(max_length=25, default="white")
    tabbar_bg_color = models.CharField(max_length=25, default="white")
    tabbar_fg_color = models.CharField(max_length=25, default="black")
    tabbar_border_color = models.CharField(max_length=25, default="black")
    tabbar_hover_bg_color = models.CharField(max_length=25, default="grey")
    tabbar_hover_fg_color = models.CharField(max_length=25, default="white")
    tabbar_active_bg_color = models.CharField(max_length=25, default="black")
    tabbar_active_fg_color = models.CharField(max_length=25, default="white")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    font_family = models.CharField(max_length=75, default="Arial, Helvetica, Sans Serif")
    font_size = models.CharField(max_length=10, default="10pt")
    current_theme = models.CharField(max_length=10, default="black")
    navbar_bg_color = models.CharField(max_length=25, default="black")
    navbar_fg_color = models.CharField(max_length=25, default="white")
    navbar_button_fg_color = models.CharField(max_length=25, default="black")
    navbar_button_bg_color = models.CharField(max_length=25, default="#e7e7e7")
    navbar_button_border_color = models.CharField(max_length=25, default="white")
    dropdown_fg_color = models.CharField(max_length=25, default="black")
    dropdown_bg_color = models.CharField(max_length=25, default="#f9f9f9")
    dropdown_hover_color = models.CharField(max_length=25, default="#dddddd")
    menubar_bg_color = models.CharField(max_length=25, default="white")
    tabbar_bg_color = models.CharField(max_length=25, default="white")
    tabbar_fg_color = models.CharField(max_length=25, default="black")
    tabbar_border_color = models.CharField(max_length=25, default="black")
    tabbar_hover_bg_color = models.CharField(max_length=25, default="grey")
    tabbar_hover_fg_color = models.CharField(max_length=25, default="white")
    tabbar_active_bg_color = models.CharField(max_length=25, default="black")
    tabbar_active_fg_color = models.CharField(max_length=25, default="white")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
