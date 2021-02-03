import os
import json
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Group, Permission
from aif_character.models import Character, Armor, Buffs, Container, Equipment, Skills, Spells, Tips, Weapons
# from aif_playerstome.models import Armor, Equipment, Weapons, Spells


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
        Tips.serialize()
        Weapons.serialize()
