from django.core.management.base import BaseCommand, CommandError
from aif_character.models import Character


class Command(BaseCommand):


    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        for row in Character.objects.all():
            print(row.name + " (" + row.player + ") " + row.race + " " + row.char_class)