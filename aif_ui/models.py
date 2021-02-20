from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from aif import data_serializer


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

    @staticmethod
    def add_to_user(request):
        theme = Themes.objects.get(name=request.POST['theme_selected'])
        request.user.profile.current_theme = theme.name
        request.user.profile.save()
        request.user.session.current_theme = theme.name
        request.user.session.font_family = theme.font_family
        request.user.session.font_size = theme.font_size
        request.user.session.navbar_bg_color = theme.navbar_bg_color
        request.user.session.navbar_fg_color = theme.navbar_fg_color
        request.user.session.navbar_button_bg_color = theme.navbar_button_bg_color
        request.user.session.navbar_button_fg_color = theme.navbar_button_fg_color
        request.user.session.navbar_button_border_color = theme.navbar_button_border_color
        request.user.session.dropdown_bg_color = theme.dropdown_bg_color
        request.user.session.dropdown_fg_color = theme.dropdown_fg_color
        request.user.session.dropdown_hover_color = theme.dropdown_hover_color
        request.user.session.menubar_bg_color = theme.menubar_bg_color
        request.user.session.tabbar_bg_color = theme.tabbar_bg_color
        request.user.session.tabbar_fg_color = theme.tabbar_fg_color
        request.user.session.tabbar_border_color = theme.tabbar_border_color
        request.user.session.tabbar_hover_bg_color = theme.tabbar_hover_bg_color
        request.user.session.tabbar_hover_fg_color = theme.tabbar_hover_fg_color
        request.user.session.tabbar_active_bg_color = theme.tabbar_active_bg_color
        request.user.session.tabbar_active_fg_color = theme.tabbar_active_fg_color
        request.user.session.save()

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/themes", Themes)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/themes", Themes)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_character = models.CharField(max_length=75, default="")
    current_theme = models.CharField(max_length=10, default="black")

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/user", User)
        data_serializer.deserialize_object(__file__, "/data/profile", Profile)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/user", User)
        data_serializer.serialize_object(__file__, "/data/profile", Profile)


class Session(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=75, default="")
    ui_state = models.CharField(max_length=10, default="index")  # was flag
    sheet_id = models.CharField(max_length=10, default="Sheet_1")
    current_theme = models.CharField(max_length=10, default="black")
    # theme variables
    font_family = models.CharField(max_length=75, default="Arial, Helvetica, Sans Serif")
    font_size = models.CharField(max_length=10, default="10pt")
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

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/session", Session)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/session", Session)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def create_user_session(sender, instance, created, **kwargs):
    if created:
        Session.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_session(sender, instance, **kwargs):
    instance.session.save()
