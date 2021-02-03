from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from aif_ui.models import Themes


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        self.stdout.write("creating theme black")
        t = Themes.objects.create(name='black')
        t.navbar_bg_color = 'black'
        t.navbar_fg_color = 'white'
        t.menubar_bg_color = 'white'
        t.tabbar_hover_bg_color = 'silver'
        t.tabbar_hover_fg_color = 'black'
        t.tabbar_active_bg_color = 'black'
        t.tabbar_active_fg_color = 'white'
        t.save()
        self.stdout.write("creating theme blue")
        t = Themes.objects.create(name='blue')
        t.navbar_bg_color = 'navy'
        t.navbar_fg_color = 'white'
        t.menubar_bg_color = 'dodgerblue'
        t.tabbar_hover_bg_color = 'dodgerblue'
        t.tabbar_hover_fg_color = 'black'
        t.tabbar_active_bg_color = 'navy'
        t.tabbar_active_fg_color = 'white'
        t.save()
        self.stdout.write("creating theme brown")
        t = Themes.objects.create(name='brown')
        t.navbar_bg_color = 'saddlebrown'
        t.navbar_fg_color = 'white'
        t.menubar_bg_color = 'yellow'
        t.tabbar_hover_bg_color = 'yellow'
        t.tabbar_hover_fg_color = 'black'
        t.tabbar_active_bg_color = 'saddlebrown'
        t.tabbar_active_fg_color = 'white'
        t.save()
        self.stdout.write("creating theme green")
        t = Themes.objects.create(name='green')
        t.navbar_bg_color = 'darkgreen'
        t.navbar_fg_color = 'white'
        t.menubar_bg_color = 'lime'
        t.tabbar_hover_bg_color = 'lime'
        t.tabbar_hover_fg_color = 'black'
        t.tabbar_active_bg_color = 'darkgreen'
        t.tabbar_active_fg_color = 'white'
        t.save()
        self.stdout.write("creating theme orange")
        t = Themes.objects.create(name='orange')
        t.navbar_bg_color = 'darkorange'
        t.navbar_fg_color = 'white'
        t.menubar_bg_color = 'coral'
        t.tabbar_hover_bg_color = 'coral'
        t.tabbar_hover_fg_color = 'black'
        t.tabbar_active_bg_color = 'darkorange'
        t.tabbar_active_fg_color = 'white'
        t.save()
        self.stdout.write("creating theme red")
        t = Themes.objects.create(name='red')
        t.navbar_bg_color = 'darkred'
        t.navbar_fg_color = 'white'
        t.menubar_bg_color = 'red'
        t.tabbar_hover_bg_color = 'red'
        t.tabbar_hover_fg_color = 'black'
        t.tabbar_active_bg_color = 'darkred'
        t.tabbar_active_fg_color = 'white'
        t.save()
