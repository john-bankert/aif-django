from django.core.management.base import BaseCommand, CommandError
from aif_character.models import  Character, ClassSkills, RacialSkills, HonorSkills, SpellSkills, Spells, Weapons, Armor, Container, Equipment, Tips, Buffs


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        Character.serialize()
        ClassSkills.serialize()
        RacialSkills.serialize()
        HonorSkills.serialize()
        SpellSkills.serialize()
        Spells.serialize()
        Weapons.serialize()
        Armor.serialize()
        Container.serialize()
        Equipment.serialize()
        Tips.serialize()
        Buffs.serialize()
