from django.core.management.base import BaseCommand, CommandError
from aif_playerstome.models import ArmorCatalog, EquipmentCatalog, SpellsList, WeaponsCatalog


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        ArmorCatalog.import_csv()
        EquipmentCatalog.import_csv()
        SpellsList.import_csv()
        WeaponsCatalog.import_csv()
