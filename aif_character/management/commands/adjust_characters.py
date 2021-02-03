from django.core.management.base import BaseCommand, CommandError
from aif_character.models import Character


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # for char in Character.objects.filter(name='Torburn'):
        for char in Character.objects.all():
            self.stdout.write("Adjusting Character " + char.name)
            char.adjust()
            char.save()
