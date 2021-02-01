import os
import csv
import json
from datetime import datetime
from django.core import serializers
from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from aif import constants as aif


class Armor(models.Model):

    key = models.CharField(max_length=150, default="")
    category = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=100, default="")
    cost = models.CharField(max_length=15, default="")
    type = models.CharField(max_length=5, default="")
    slashing = models.CharField(max_length=5, default="")
    piercing = models.CharField(max_length=5, default="")
    bludgeoning = models.CharField(max_length=5, default="")
    cleaving = models.CharField(max_length=5, default="")
    load = models.CharField(max_length=10, default="")
    carried = models.CharField(max_length=10, default="")
    durability = models.CharField(max_length=10, default="")

    @staticmethod
    def importData():
        try:
            Armor.objects.all().delete()
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/armor.csv"
            with open(fn, newline='\n') as file:
                for row in csv.reader(file, delimiter=',', quotechar='"'):
                    key = row[1].strip().replace(" ", "_") + "_" + row[0].strip()
                    if Armor.objects.filter(key=key).count() == 0:
                        print("Adding " + row[1].strip() + " (" + row[0].strip() + ") to armor table")
                        a = Armor()
                    else:
                        print("Updating " + row[1].strip() + " (" + row[0].strip() + ") in armor table")
                        a = Armor.objects.get(key=key)
                    a.key = key
                    a.category = row[0].strip()
                    a.name = row[1].strip()
                    a.cost = row[2].strip()
                    a.type = row[3].strip()
                    a.slashing = row[4].strip()
                    a.piercing = row[5].strip()
                    a.bludgeoning = row[6].strip()
                    a.cleaving = row[7].strip()
                    a.load = row[8].strip()
                    a.carried = row[9].strip()
                    a.durability = row[10].strip()
                    a.save()
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/armor.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Armor.objects.all())
            with open(filename, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def exportData():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/armor.csv"
            fn_backup = os.path.dirname(os.path.realpath(__file__)) + "/data/armor_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
            os.rename(fn, fn_backup)
            with open(fn, "w", newline='\n') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in Armor.objects.all():
                    print("Exporting " + row.name + " (" + row.category + ") from armor table")
                    writer.writerow([row.category, row.name, row.cost, row.type, row.slashing, row.piercing, 
                                        row.bludgeoning, row.cleaving, row.load, row.carried, row.durability])
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def add_to_character(character, category, name, description=""):
        try:
            if character.skills_set.filter(name=name).count() > 0:
                sk = character.skills_set.get(name=name)
            else:
                sort_order = 0
                if character.skills_set.filter(skill_type=aif.ARMOR):
                    sort_order = character.skills_set.filter(skill_type=aif.ARMOR).latest('sort_order').sort_order
                    sort_order += 1
                sk = character.skills_set.create(name=name, skill_type=aif.ARMOR, sort_order=sort_order)
                sk.save()
                character.save()

            _armor = Armor.objects.get(category=category, name=name)
            a = character.armor_set.create(name=name, skill=sk.pk)
            a.description = description if description != "" else name
            a.type = _armor.type
            a.durability = _armor.durability
            a.slashing = _armor.slashing
            a.piercing = _armor.piercing
            a.bludgeoning = _armor.bludgeoning
            a.cleaving = _armor.cleaving
            a.load = _armor.load
            a.carried = _armor.carried
            a.durability = _armor.durability
            a.save()
            character.save()
        except ObjectDoesNotExist:
            pass


class ArmorForm(ModelForm):
    class Meta:
        model = Armor
        fields = ['category', 'name', 'cost', 'type', 'slashing', 'piercing', 'bludgeoning', 
                    'cleaving', 'load', 'carried', 'durability']


class Equipment(models.Model):

    key = models.CharField(max_length=150, default="")
    category = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=100, default="")
    cost = models.CharField(max_length=15, default="")
    load = models.CharField(max_length=10, default="")
    capacity = models.CharField(max_length=10, default="")
    slashing = models.CharField(max_length=5, default="")
    piercing = models.CharField(max_length=5, default="")
    bludgeoning = models.CharField(max_length=5, default="")
    cleaving = models.CharField(max_length=5, default="")
    durability = models.CharField(max_length=10, default="")

    @staticmethod
    def importData():
        try:
            Equipment.objects.all().delete()
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/equipment.csv"
            with open(fn, newline='\n') as file:
                for row in csv.reader(file, delimiter=',', quotechar='"'):
                    key = row[1].strip().replace(" ", "_") + "_" + row[0].strip()
                    if Equipment.objects.filter(key=key).count() == 0:
                        print("Adding " + row[1].strip() + " (" + row[0].strip() + ") to equipment table")
                        e = Equipment()
                    else:
                        print("Updating " + row[1].strip() + " (" + row[0].strip() + ") in equipment table")
                        e = Equipment.objects.get(key=key)
                    e.key = key
                    e.category = row[0].strip()
                    e.name = row[1].strip()
                    e.cost = row[2].strip()
                    e.load = row[3].strip()
                    e.capacity = row[4].strip()
                    e.slashing = row[5].strip()
                    e.piercing = row[6].strip()
                    e.bludgeoning = row[7].strip()
                    e.cleaving = row[6].strip()
                    e.durability = row[9].strip()
                    e.save()
        except FileNotFoundError:
            print("file not found")
        
    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/equipment.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Equipment.objects.all())
            with open(filename, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def exportData():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/equipment.csv"
            fn_backup = os.path.dirname(os.path.realpath(__file__)) + "/data/equipment_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
            os.rename(fn, fn_backup)
            with open(fn, "w", newline='\n') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in Equipment.objects.all():
                    print("Exporting " + row.name + " (" + row.category + ") from equipment table")
                    writer.writerow([row.category, row.name, row.cost, row.load, row.capacity, row.slashing, 
                                        row.piercing, row.bludgeoning, row.cleaving, row.durability])
        except FileNotFoundError:
            print("file not found")


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['category', 'name', 'cost', 'load', 'capacity', 'slashing', 'piercing', 'bludgeoning', 
                    'cleaving', 'durability']


# class Races(models.Model):
class Skills(models.Model):
    key = models.CharField(max_length=150, default="")
    name = models.CharField(max_length=100, default="")
    skill_type = models.CharField(max_length=10, default="")
    skill_class = models.CharField(max_length=25, default="")
    description = models.TextField()

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/skills.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Spells.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def add_to_character(character, name, type, rank, mastered=False):
        if character.skills_set.filter(name=name, skill_type=type).count() > 0:
            sk = character.skills_set.get(name=name, skill_type=type)
        else:
            sort_order = 0
            if character.skills_set.filter(skill_type=type):
                sort_order = character.skills_set.filter(skill_type=type).latest('sort_order').sort_order
                sort_order += 1
            sk = character.skills_set.create(name=name, skill_type=type, sort_order=sort_order)
            sk.save()
            character.save()
        sk.rank = rank
        sk.mastered = mastered
        sk.save()
        character.save()


class Spells(models.Model):

    key = models.CharField(max_length=150, default="")
    category = models.CharField(max_length=50, default="")
    circle = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=100, default="")
    area = models.CharField(max_length=50, default="")
    duration = models.CharField(max_length=50, default="")
    range = models.CharField(max_length=50, default="")
    saves = models.CharField(max_length=50, default="")
    upkeep = models.CharField(max_length=10, default="")
    description = models.TextField()

    @staticmethod
    def importData():
        try:
            Spells.objects.all().delete()
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/spells.csv"
            with open(fn, newline='\n') as file:
                for row in csv.reader(file, delimiter=',', quotechar='"'):
                    key = row[0].strip() + "_"+ row[1].strip().replace(" ", "_") + "_" + row[2].strip().replace(" ", "_")
                    if Spells.objects.filter(key=key).count() == 0:
                        print("Adding " + row[2].strip() + " (" + row[0].strip() + " " + row[1].strip() + ") to spells table")
                        s = Spells()
                    else:
                        print("Updating " + row[2].strip() + " (" + row[0].strip() + " " + row[1].strip() + ") in spells table")
                        s = Equipment.objects.get(key=key)
                    s.key = key
                    s.category = row[0].strip()
                    s.circle = row[1].strip()
                    s.name = row[2].strip()
                    s.area = row[3].strip()
                    s.duration = row[4].strip()
                    s.range = row[5].strip()
                    s.saves = row[6].strip()
                    s.upkeep = row[7].strip()
                    s.description = row[8].strip()
                    s.save()
        except FileNotFoundError:
            print("file not found")
        
    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/spells.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Spells.objects.all())
            with open(filename, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def exportData():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/spells.csv"
            fn_backup = os.path.dirname(os.path.realpath(__file__)) + "/data/spells_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
            os.rename(fn, fn_backup)
            with open(fn, "w", newline='\n') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in Equipment.objects.all():
                    print("Exporting " + row.name + " (" + row.category + ") from spells table")
                    writer.writerow([row.category, row.circle, row.name, row.area, row.duration, row.range,
                                        row.saves, row.upkeep, row.duration])
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def add_to_character(character, name, type, rank, mastered=False):
        if character.skills_set.filter(name=name, skill_type=type).count() > 0:
            sk = character.skills_set.get(name=name, skill_type=type)
        else:
            sk = character.skills_set.create(name=name, skill_type=type)
            sk.save()
            character.save()
        sk.rank = rank
        sk.mastered = mastered
        sk.save()
        character.save()


class SpellsForm(ModelForm):
    class Meta:
        model = Spells
        fields = ['category', 'circle', 'name', 'area', 'duration', 'range', 'saves', 'upkeep', 'description']


class Weapons(models.Model):

    key = models.CharField(max_length=150, default="")
    category = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=100, default="")
    cost = models.CharField(max_length=15, default="")
    size = models.CharField(max_length=5, default="")
    type = models.CharField(max_length=5, default="")
    damage = models.CharField(max_length=15, default="")
    range = models.CharField(max_length=15, default="")
    load = models.CharField(max_length=10, default="")
    durability = models.CharField(max_length=10, default="")

    @staticmethod
    def importData():
        try:
            Weapons.objects.all().delete()
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/weapons.csv"
            with open(fn, newline='\n') as file:
                for row in csv.reader(file, delimiter=',', quotechar='"'):
                    key = row[1].strip().replace(" ", "_") + "_" + row[0].strip()
                    if Weapons.objects.filter(key=key).count() == 0:
                        print("Adding " + row[1].strip() + " (" + row[0].strip() + ") to weapons table")
                        w = Weapons()
                    else:
                        print("Updating " + row[1].strip() + " (" + row[0].strip() + ") in weapons table")
                        w = Weapons.objects.get(key=key)
                    w.key = key
                    w.category = row[0].strip()
                    w.name = row[1].strip()
                    w.cost = row[2].strip()
                    w.size = row[3].strip()
                    w.type = row[4].strip()
                    w.damage = row[5].strip()
                    w.range = row[6].strip()
                    w.load = row[7].strip()
                    w.durability = row[8].strip()
                    w.save()
        except FileNotFoundError:
            print("file not found")
        
    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/weapons.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Weapons.objects.all())
            with open(filename, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def exportData():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/weapons.csv"
            fn_backup = os.path.dirname(os.path.realpath(__file__)) + "/data/weapons_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".csv"
            os.rename(fn, fn_backup)
            with open(fn, "w", newline='\n') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in Weapons.objects.all():
                    print("Exporting " + row.name + " (" + row.category + ") from weapons table")
                    writer.writerow([row.category, row.name, row.cost, row.size, row.type, row.damage, row.range,
                                        row.load, row.durability])
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def add_to_character(character, name, description=""):
        if character.skills_set.filter(name=name):
            sk = character.skills_set.get(name=name)
        else:
            sort_order = 0
            if character.skills_set.filter(skill_type=aif.WEAPON):
                sort_order = character.skills_set.filter(skill_type=aif.WEAPON).latest('sort_order').sort_order
                sort_order += 1
            sk = character.skills_set.create(name=name, skill_type=aif.WEAPON, sort_order=sort_order)
            sk.save()
            character.save()
        w = character.weapons_set.create(name=name, skill_pk=sk.pk)
        w.description = description if description != "" else name
        for weapon in Weapons.objects.filter(name=name):
            w.size = weapon.size
            w.weapon_pk = weapon.pk
            w.type = weapon.type
            w.damage = weapon.damage
            w.range = weapon.range
            w.durability = weapon.durability
            w.load = weapon.load
            if weapon.category == 'T':
                w.is_missile = True
            else:
                w.is_melee = True
        w.save()
        character.save()


class WeaponsForm(ModelForm):
    class Meta:
        model = Weapons
        fields = ['category', 'name', 'cost', 'size', 'type', 'damage', 'range', 'load', 'durability']
