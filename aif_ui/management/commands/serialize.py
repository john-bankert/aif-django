import os
import json
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Group, Permission
from aif_character.models import Character
from aif_playerstome.models import Armor, Equipment, Weapons, Spells

class Command(BaseCommand):


    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        self.dumpToJson(User.objects.all(), "user.json")
        self.dumpToJson(Character.objects.all(), "character.json")
        self.dumpToJson(Armor.objects.all(), "armor.json")
        self.dumpToJson(Equipment.objects.all(), "equipment.json")
        self.dumpToJson(Weapons.objects.all(), "weapons.json")
        
    def dumpToJson(self, queryset, filename):
        # fn = os.path.dirname(os.path.realpath(__file__)) + "/data/armor.csv"
        JSONSerializer = serializers.get_serializer("json")
        json_serializer = JSONSerializer()
        json_serializer.serialize(queryset)
        parsed = json.loads(json_serializer.getvalue())
        with open(filename, "w") as out:
            out.write(json.dumps(parsed, indent=4))
