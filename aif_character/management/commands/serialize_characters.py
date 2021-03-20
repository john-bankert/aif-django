from django.core.management.base import BaseCommand, CommandError
from aif_character.models import Character, Armor, Buffs, Container, Equipment, Skills, Spells, StaticBuffs,\
    Tips, Weapons


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        Character.serialize()
        Armor.serialize()
        Buffs.serialize()
        Container.serialize()
        Equipment.serialize()
        Skills.serialize()
        Spells.serialize()
        StaticBuffs.serialize()
        Tips.serialize()
        Weapons.serialize()
