from django.core.management.base import BaseCommand, CommandError
from aif_playerstome.models import Armor, Equipment, Weapons, Spells


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        Armor.exportData()
        Equipment.exportData()
        Weapons.exportData()
        Spells.exportData()
