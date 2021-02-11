from django.core.management.base import BaseCommand, CommandError
from aif_character.models import Character, Armor, Buffs, Container, Equipment, Skills, Spells, Tips, Weapons


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        Character.deserialize()
        Armor.deserialize()
        Buffs.deserialize()
        Container.deserialize()
        Equipment.deserialize()
        Skills.deserialize()
        Spells.deserialize()
        Tips.deserialize()
        Weapons.deserialize()
