from django.core.management.base import BaseCommand, CommandError
from aif_ui.models import Profile, Session, Themes


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        Profile.deserialize()
        Session.deserialize()
        Themes.deserialize()
