import os
import csv
import json
from datetime import datetime
from django.core import serializers
from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from aif import constants as aif
from aif import data_serializer


class ArmorCatalog(models.Model):
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
    def add_to_character(character, category, name, description=""):
        if character.skills_set.filter(name=name):
            sk = character.skills_set.get(name=name)
        else:
            sort_order = 0
            if character.skills_set.filter(skill_type=aif.ARMOR):
                sort_order = character.skills_set.filter(skill_type=aif.ARMOR).latest('sort_order').sort_order
                sort_order += 1
            sk = character.skills_set.create(name=name, skill_type=aif.ARMOR, sort_order=sort_order)
            sk.save()
            character.save()

        armor = ArmorCatalog.objects.get(category=category, name=name)
        a = character.armor_set.create(name=name, skill=sk.pk)
        a.description = description if description != "" else name
        a.type = armor.type
        a.durability = armor.durability
        a.slashing = armor.slashing
        a.piercing = armor.piercing
        a.bludgeoning = armor.bludgeoning
        a.cleaving = armor.cleaving
        a.load = armor.load
        a.carried = armor.carried
        a.durability = armor.durability
        a.save()
        character.save()

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/armor_catalog", ArmorCatalog)
        # data_serializer.deserialize_object(__file__, "/data/armor_catalog_shortened.xml", ArmorCatalog)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/armor_catalog", ArmorCatalog)

    @staticmethod
    def import_csv():
        try:
            ArmorCatalog.objects.all().delete()
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/armor_catalog.csv"
            with open(fn, newline='\n') as file:
                for row in csv.reader(file, delimiter=',', quotechar='"'):
                    key = row[1].strip().replace(" ", "_") + "_" + row[0].strip()
                    if ArmorCatalog.objects.filter(key=key).count() == 0:
                        print("Adding " + row[1].strip() + " (" + row[0].strip() + ") to Armor Catalog table")
                        a = ArmorCatalog()
                    else:
                        print("Updating " + row[1].strip() + " (" + row[0].strip() + ") in Armor Catalog table")
                        a = ArmorCatalog.objects.get(key=key)
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
    def export_csv():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/armor_catalog.csv"
            fn_backup = os.path.dirname(os.path.realpath(__file__)) + "/data/armor_catalog_" + datetime.now().strftime(
                "%Y%m%d-%H%M%S") + ".csv"
            os.rename(fn, fn_backup)
            with open(fn, "w", newline='\n') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in ArmorCatalog.objects.all():
                    print("Exporting " + row.name + " (" + row.category + ") from Armor Catalog table")
                    writer.writerow([row.category, row.name, row.cost, row.type, row.slashing, row.piercing,
                                     row.bludgeoning, row.cleaving, row.load, row.carried, row.durability])
        except FileNotFoundError:
            print("file not found")


class ArmorCatalogForm(ModelForm):
    class Meta:
        model = ArmorCatalog
        fields = ['category', 'name', 'cost', 'type', 'slashing', 'piercing', 'bludgeoning',
                  'cleaving', 'load', 'carried', 'durability']


class EquipmentCatalog(models.Model):
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
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/equipment_catalog", EquipmentCatalog)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/equipment_catalog", EquipmentCatalog)

    @staticmethod
    def import_csv():
        try:
            EquipmentCatalog.objects.all().delete()
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/equipment_catalog.csv"
            with open(fn, newline='\n') as file:
                for row in csv.reader(file, delimiter=',', quotechar='"'):
                    key = row[1].strip().replace(" ", "_") + "_" + row[0].strip()
                    if EquipmentCatalog.objects.filter(key=key).count() == 0:
                        print("Adding " + row[1].strip() + " (" + row[0].strip() + ") to Equipment Catalog table")
                        e = EquipmentCatalog()
                    else:
                        print("Updating " + row[1].strip() + " (" + row[0].strip() + ") in Equipment Catalog table")
                        e = EquipmentCatalog.objects.get(key=key)
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
    def export_csv():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/equipment_catalog.csv"
            fn_backup = os.path.dirname(os.path.realpath(__file__)) + "/data/equipment_catalog_" + datetime.now().strftime(
                "%Y%m%d-%H%M%S") + ".csv"
            os.rename(fn, fn_backup)
            with open(fn, "w", newline='\n') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in EquipmentCatalog.objects.all():
                    print("Exporting " + row.name + " (" + row.category + ") from EquipmentCatalog table")
                    writer.writerow([row.category, row.name, row.cost, row.load, row.capacity, row.slashing,
                                     row.piercing, row.bludgeoning, row.cleaving, row.durability])
        except FileNotFoundError:
            print("file not found")


class EquipmentCatalogForm(ModelForm):
    class Meta:
        model = EquipmentCatalog
        fields = ['category', 'name', 'cost', 'load', 'capacity', 'slashing', 'piercing', 'bludgeoning',
                  'cleaving', 'durability']


class SkillsList(models.Model):
    key = models.CharField(max_length=150, default="")
    name = models.CharField(max_length=100, default="")
    skill_type = models.CharField(max_length=10, default="")
    skill_class = models.CharField(max_length=25, default="")
    description = models.TextField()

    @staticmethod
    def add_to_character(character, name, type, rank, mastered=False, buff=0):
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
        sk.buff = buff
        sk.save()
        character.save()

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/skills_list", SkillsList)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/skills_list", SkillsList)


class SpellsList(models.Model):
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
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/spells_list_list", SpellsList)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/spells_list_list", SpellsList)

    @staticmethod
    def import_csv():
        try:
            SpellsList.objects.all().delete()
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/spells_list.csv"
            with open(fn, newline='\n') as file:
                for row in csv.reader(file, delimiter=',', quotechar='"'):
                    key = row[0].strip() + "_" + row[1].strip().replace(" ", "_") + "_" + row[2].strip().replace(" ",
                                                                                                                 "_")
                    if SpellsList.objects.filter(key=key).count() == 0:
                        print("Adding " + row[2].strip() + " (" + row[0].strip() + " " + row[
                            1].strip() + ") to Spells List table")
                        s = SpellsList()
                    else:
                        print("Updating " + row[2].strip() + " (" + row[0].strip() + " " + row[
                            1].strip() + ") in Spells List table")
                        s = EquipmentCatalog.objects.get(key=key)
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
    def export_csv():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/spells_list.csv"
            fn_backup = os.path.dirname(os.path.realpath(__file__)) + "/data/spells_list_" + datetime.now().strftime(
                "%Y%m%d-%H%M%S") + ".csv"
            os.rename(fn, fn_backup)
            with open(fn, "w", newline='\n') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in EquipmentCatalog.objects.all():
                    print("Exporting " + row.name + " (" + row.category + ") from spells List table")
                    writer.writerow([row.category, row.circle, row.name, row.area, row.duration, row.range,
                                     row.saves, row.upkeep, row.duration])
        except FileNotFoundError:
            print("file not found")

    @staticmethod
    def add_to_character(character, name, type, rank, mastered=False):
        if character.spells_set.filter(name=name).count() > 0:
            sp = character.spells_set.get(name=name)
        else:
            sp = character.skills_set.create(name=name)
            sp.save()
            character.save()
        sp.rank = rank
        sp.mastered = mastered
        sp.save()
        character.save()


class SpellsListForm(ModelForm):
    class Meta:
        model = SpellsList
        fields = ['category', 'circle', 'name', 'area', 'duration', 'range', 'saves', 'upkeep', 'description']


class WeaponsCatalog(models.Model):
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
        for weapon in WeaponsCatalog.objects.filter(name=name):
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

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/weapons_catalog", WeaponsCatalog)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/weapons_catalog", WeaponsCatalog)

    @staticmethod
    def import_csv():
        try:
            WeaponsCatalog.objects.all().delete()
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/weapons_catalog.csv"
            with open(fn, newline='\n') as file:
                for row in csv.reader(file, delimiter=',', quotechar='"'):
                    key = row[1].strip().replace(" ", "_") + "_" + row[0].strip()
                    if WeaponsCatalog.objects.filter(key=key).count() == 0:
                        print("Adding " + row[1].strip() + " (" + row[0].strip() + ") to Weapons Catalog table")
                        w = WeaponsCatalog()
                    else:
                        print("Updating " + row[1].strip() + " (" + row[0].strip() + ") in Weapons Catalog table")
                        w = WeaponsCatalog.objects.get(key=key)
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
    def export_csv():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/weapons_catalog.csv"
            fn_backup = os.path.dirname(os.path.realpath(__file__)) + "/data/weapons_catalog_" + datetime.now().strftime(
                "%Y%m%d-%H%M%S") + ".csv"
            os.rename(fn, fn_backup)
            with open(fn, "w", newline='\n') as file:
                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for row in WeaponsCatalog.objects.all():
                    print("Exporting " + row.name + " (" + row.category + ") from Weapons Catalog table")
                    writer.writerow([row.category, row.name, row.cost, row.size, row.type, row.damage, row.range,
                                     row.load, row.durability])
        except FileNotFoundError:
            print("file not found")


class WeaponsCatalogForm(ModelForm):
    class Meta:
        model = WeaponsCatalog
        fields = ['category', 'name', 'cost', 'size', 'type', 'damage', 'range', 'load', 'durability']
