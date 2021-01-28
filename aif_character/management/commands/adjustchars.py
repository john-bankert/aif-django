from django.core.management.base import BaseCommand, CommandError
from aif_character.models import Character
from aif_playerstome.models import Weapons, Armor


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.adjust_character('Chauncy')
        self.adjust_character('Zandor')
        self.adjust_character('Fredo')
        self.adjust_character('Brunie')
        self.adjust_character('Elanor')
        self.adjust_character('Zax')
        self.adjust_character('Prosser')
        self.adjust_character('Boudica')
        self.adjust_character('Rosie')
        self.adjust_character('Flanders')
        self.adjust_character('Trisha')
        self.adjust_character('Glinka')
        self.adjust_character('Horanda')
        self.adjust_character('George')

    def adjust_character(self, _name):
        if Character.objects.filter(name=_name).count() != 0:
            self.stdout.write("Adjusting Character " + _name)
            c = Character.objects.get(name=_name)
            c.adjust()
            c.save()
