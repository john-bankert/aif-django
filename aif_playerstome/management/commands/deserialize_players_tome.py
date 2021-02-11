from django.core.management.base import BaseCommand, CommandError
from aif_playerstome.models import ArmorCatalog, EquipmentCatalog, SkillsList, SpellsList, WeaponsCatalog


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        ArmorCatalog.deserialize()
        EquipmentCatalog.deserialize()
        SkillsList.deserialize()
        SpellsList.deserialize()
        WeaponsCatalog.deserialize()
