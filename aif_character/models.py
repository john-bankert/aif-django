import os
import json
import random
import decimal
import importlib
from django.db import models
from django.forms import ModelForm
from django.core import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from aif import constants as aif
from aif import data_serializer
from aif_campaign import functions as fn
from aif_playerstome import races, classes, spells
from aif_playerstome.models import EquipmentCatalog, SpellsList, WeaponsCatalog

application_label = 'aif_character'


class Character(models.Model):
    name = models.CharField(max_length=100, default="")
    player = models.CharField(max_length=100, default="")
    party = models.CharField(max_length=100, default="")
    race = models.CharField(max_length=25, default="")
    char_class = models.CharField(max_length=50, default="")
    gender = models.CharField(max_length=25, default="")
    age = models.IntegerField(default=18)
    height = models.CharField(max_length=25, default="")
    weight = models.CharField(max_length=25, default="")
    notes = models.TextField()
    open = models.BooleanField(default=False)

    movement = models.CharField(max_length=10)
    # movement_buff = models.IntegerField(default=0)
    walking_base = models.IntegerField(default=0)
    walking_buff = models.IntegerField(default=0)
    walking_display = models.IntegerField(default=0)
    running_base = models.IntegerField(default=0)
    running_buff = models.IntegerField(default=0)
    running_display = models.IntegerField(default=0)
    swimming_base = models.IntegerField(default=0)
    swimming_buff = models.IntegerField(default=0)
    swimming_display = models.IntegerField(default=0)

    encumbrance = models.IntegerField(default=0)
    total_load = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    weapons_total_load = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    armor_total_load = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    money_total_load = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    modifiers = models.IntegerField(default=0)
    burdened = models.IntegerField(default=0)

    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    next_level = models.IntegerField(default=10)

    str_base = models.IntegerField(default=0)
    str_buff = models.IntegerField(default=0)
    str_display = models.IntegerField(default=0)
    str_modifiers = models.CharField(max_length=10, default="")

    dex_base = models.IntegerField(default=0)
    dex_buff = models.IntegerField(default=0)
    dex_display = models.IntegerField(default=0)
    dex_modifiers = models.CharField(max_length=10, default="")

    int_base = models.IntegerField(default=0)
    int_buff = models.IntegerField(default=0)
    int_display = models.IntegerField(default=0)
    int_modifiers = models.CharField(max_length=10, default="")

    health_base = models.IntegerField(default=0)
    health_buff = models.IntegerField(default=0)
    health_display = models.IntegerField(default=0)
    health_modifiers = models.CharField(max_length=10, default="")
    health_current = models.IntegerField(default=0)

    honor_points_base = models.IntegerField(default=0)
    honor_points_current = models.IntegerField(default=0)

    spell_points_base = models.IntegerField(default=0)
    spell_points_current = models.IntegerField(default=0)
    spell_effectiveness_modifier = models.IntegerField(default=0)
    rhythm_points_base = models.IntegerField(default=0)
    rhythm_points_current = models.IntegerField(default=0)
    spell_cards_base = models.IntegerField(default=0)
    spell_cards_current = models.IntegerField(default=0)

    knockdown_base = models.IntegerField(default=0)
    knockdown_buff = models.IntegerField(default=0)
    knockdown_cf_points = models.IntegerField(default=0)
    knockdown_display = models.IntegerField(default=0)

    defense_base = models.IntegerField(default=0)
    defense_buff = models.IntegerField(default=0)
    defense_cf_points = models.IntegerField(default=0)
    defense_display = models.IntegerField(default=0)

    stun_base = models.IntegerField(default=0)
    stun_buff = models.IntegerField(default=0)
    stun_cf_points = models.IntegerField(default=0)
    stun_display = models.IntegerField(default=0)
    stun_current = models.IntegerField(default=0)

    endurance_base = models.IntegerField(default=0)
    endurance_cf_points = models.IntegerField(default=0)
    endurance_buff = models.IntegerField(default=0)
    endurance_display = models.IntegerField(default=0)

    fatigue = models.IntegerField(default=0)
    extra_fatigue = models.IntegerField(default=0)

    withstand_dice = models.IntegerField(default=3)
    withstand_modifiers = models.CharField(max_length=10)
    withstand_display = models.CharField(max_length=10)

    dodge_dice = models.IntegerField(default=3)
    dodge_modifiers = models.CharField(max_length=10)
    dodge_display = models.CharField(max_length=10)

    resist_dice = models.IntegerField(default=3)
    resist_modifiers = models.CharField(max_length=10)
    resist_display = models.CharField(max_length=10)

    damage_dice_base = models.IntegerField(default=0)
    damage_dice_buff = models.IntegerField(default=0)
    damage_dice_display = models.CharField(max_length=15)

    damage_mods_base = models.IntegerField(default=0)
    damage_mods_buff = models.IntegerField(default=0)
    damage_mods_display = models.CharField(max_length=15)

    damage_display = models.CharField(max_length=15)

    to_hit_dice_base = models.IntegerField(default=0)
    to_hit_dice_buff = models.IntegerField(default=0)
    to_hit_dice_display = models.CharField(max_length=15)

    to_hit_mods_base = models.IntegerField(default=0)
    to_hit_mods_buff = models.IntegerField(default=0)
    to_hit_mods_display = models.CharField(max_length=15)

    to_hit_display = models.CharField(max_length=15)

    actions_base = models.IntegerField(default=1)
    actions_buff = models.IntegerField(default=0)
    actions_display = models.CharField(max_length=15)

    outside_search_dice = models.IntegerField(default=3)
    outside_search_modifiers = models.IntegerField(default=0)
    outside_search_display = models.CharField(max_length=15)

    underground_search_dice = models.IntegerField(default=3)
    underground_search_modifiers = models.IntegerField(default=0)
    underground_search_display = models.CharField(max_length=15)

    spbc_buff = models.IntegerField(default=0)

    gold_amount = models.IntegerField(default=0)
    gold_load = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

    silver_amount = models.IntegerField(default=0)
    silver_load = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

    copper_amount = models.IntegerField(default=0)
    copper_load = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

    total_slashing_protection = models.CharField(max_length=7, default="")
    total_piercing_protection = models.CharField(max_length=7, default="")
    total_bludgeoning_protection = models.CharField(max_length=7, default="")
    total_cleaving_protection = models.CharField(max_length=7, default="")

    current_round = models.IntegerField(default=0)
    mastered_count = models.IntegerField(default=0)
    game_day = models.IntegerField(default=0)
    game_time = models.CharField(max_length=5)

    class Meta:
        app_label = application_label

    def __str__(self):
        return self.name
        
    def new(self, character_name="", character_race="", character_gender="", character_class="", _str=0, _dex=0, _int=0, _hlth=0):

        self.name = character_name

        self.race = character_race
        if character_race != "":
            _race = getattr(importlib.import_module("aif_playerstome.races"), self.race.replace(" ", ""))()
            self.walking_base = _race.movement
            self.running_base = self.walking_base * 2
            self.swimming_base = round(self.walking_base / 2)
            self.withstand_dice = _race.save_dice[aif.WITHSTAND]
            self.withstand_modifiers = _race.save_bonuses[aif.WITHSTAND]
            self.dodge_dice = _race.save_dice[aif.DODGE]
            self.dodge_modifiers = _race.save_bonuses[aif.DODGE]
            self.resist_dice = _race.save_dice[aif.RESIST]
            self.resist_modifiers = _race.save_bonuses[aif.RESIST]
            self.outside_search_dice = _race.search_dice[aif.OUTSIDE]
            self.outside_search_modifiers = _race.search_bonuses[aif.OUTSIDE]
            self.underground_search_dice = _race.search_dice[aif.UNDERGROUND]
            self.underground_search_modifiers = _race.search_bonuses[aif.UNDERGROUND]
            self.save()

            for skill in _race.racial_skills:
                sk = self.skills_set.create(name=skill, skill_type=aif.RACIAL)
                sk.save()

        self.char_class = character_class
        self.save()
        _classes = {}
        if character_class != "":
            for cls in self.char_class.split("/"):
                _classes[cls] = getattr(importlib.import_module("aif_playerstome.classes"), cls)()
 
            class_skills = []
            for cls in _classes:
                class_skills.extend(_classes[cls].skills_list)
            class_skills = sorted(class_skills)

            for skill in class_skills:
                sk = self.skills_set.create(name=skill, skill_type=aif.CLASS)
                sk.save()

            if aif.PALADIN in self.char_class:
                self.honor_points_base = 2
                self.honor_points_current = self.honor_points_base
                sort_order = 0
                for skill in _classes[aif.PALADIN].honor_skills_list:
                    sk = self.skills_set.create(name=skill, skill_type=aif.HONOR, sort_order=sort_order)
                    sk.save()
                    sort_order += 1

            if self.is_spellcaster():
                for circle in range(1, 6):
                    sk = self.skills_set.create(name="Circle " + str(circle) + " Spell Group",
                                                skill_type=aif.SPELL)
                    sk.save()
                    if aif.ILLUSIONIST in self.char_class:
                        sk = self.skills_set.create(name="Circle " + str(circle) + " Affinity",
                                                    skill_type=aif.SPELL)
                        sk.save()
                for cls in [aif.BARD, aif.DRUID, aif.MAGICIAN, aif.WITCH]:
                    if cls in self.char_class:
                        for spell in SpellsList.objects.filter(category=cls):
                            ss = self.spells_set.create(name=spell.name)
                            ss.circle = spell.circle
                            ss.category = cls
                            ss.save()
                if self.is_wizard():
                    for spell in SpellsList.objects.filter(category=aif.WIZARD):
                        ss = self.spells_set.create(name=spell.name)
                        ss.circle = spell.circle
                        ss.category = aif.WIZARD
                        ss.save()
                if self.is_priest():
                    for spell in SpellsList.objects.filter(category=aif.PRIEST):
                        ss = self.spells_set.create(name=spell.name)
                        ss.circle = spell.circle
                        ss.category = aif.PRIEST
                        ss.save()

        self.gender = character_gender
        self.str_base = _str
        self.dex_base = _dex
        self.int_base = _int
        self.health_base = _hlth
        self.health_current = self.health_base

        self.encumbrance = self.str_base * 2
        self.burdened = self.str_base

        self.knockdown_base = round(self.str_base / 2)
        self.defense_base = round((self.str_base + self.dex_base + self.int_base) / 3)
        self.stun_base = round(self.int_base / 2)
        self.endurance_base = self.health_base

        self.damage_dice_base = 0
        self.to_hit_dice_base = 3
        self.actions_base = 1

        weapons_types = {aif.SLASHING_GRP: "S", aif.PIERCING_GRP: "P", aif.BLUDGEONING_GRP: "B", 
                            aif.CLEAVING_GRP: "C", aif.THROWING_GRP: "-", aif.BOW_GRP: "-"}
        sort_order = 0
        for weapon in weapons_types:
            sk = self.skills_set.create(name=weapon, skill_type=aif.WEAPON)
            sk.sort_order = sort_order
            sk.save()
            w = self.weapons_set.create(name=weapon)
            w.skill_pk = sk.pk
            w.description = weapon
            w.sort_order = sort_order
            w.size = "-"
            w.type = weapons_types[weapon]
            w.load = "-"
            w.save()
            sort_order += 1

        armor_types = {aif.LIGHT_GRP: "L", aif.MEDIUM_GRP: "M", aif.HEAVY_GRP: "H", aif.HELMET_GRP: "-",
                        aif.UNARMED_GRP: "U", aif.SHIELD_GRP: "S"}
        sort_order = 0
        for armor in armor_types:
            sk = self.skills_set.create(name=armor, skill_type=aif.ARMOR)
            sk.sort_order = sort_order
            sk.save()
            a = self.armor_set.create(name=armor)
            a.skill_pk = sk.pk
            a.description = armor
            a.sort_order = sort_order
            a.type = armor_types[armor]
            a.load = "-"
            a.save()
            sort_order += 1

        self.adjust()
        self.save()

    def random(self):

        _name = ""
        for idx in range(1, random.randint(7, 12)):
            ascii_char = chr(random.randint(97, 122))
            _name += ascii_char.upper() if idx == 1 else ascii_char

        _race = races.race_list[random.randint(0, len(races.race_list) - 1)]
        _class = classes.class_list[random.randint(0, len(classes.class_list) - 1)]

        cl_race = getattr(importlib.import_module("aif_playerstome.races"), _race.replace(" ", ""))()
        rd6 = cl_race.racial_d6[random.randint(0, len(cl_race.racial_d6) - 1)]
        dice = {aif.STR: 3, aif.INT: 3, aif.DEX: 3, aif.HLTH: 3}
        dice[rd6] += 1
        _str = fn.roll_dice(dice[aif.STR], (False if rd6 == aif.STR else True))
        _dex = fn.roll_dice(dice[aif.DEX], (False if rd6 == aif.DEX else True))
        _int = fn.roll_dice(dice[aif.INT], (False if rd6 == aif.INT else True))
        _health = fn.roll_dice(dice[aif.HLTH], (False if rd6 == aif.HLTH else True))
        _gender = "Male" if random.randint(0, 1) == 0 else "Female"

        self.new(_name, _race, _gender, _class, _str, _dex, _int, _health)
        if self.is_spellcaster():
            if self.char_class == aif.BARD:
                self.rhythm_points_base = fn.roll_dice(1)
                self.rhythm_points_current = self.rhythm_points_base
            elif self.char_class == aif.ILLUSIONIST:
                self.spell_cards_base = fn.roll_dice(1)
            else:
                self.spell_points_base = fn.roll_dice(1)
                self.spell_points_current = self.spell_points_base
                if aif.BARD in self.char_class:
                    self.rhythm_points_base = fn.roll_dice(1)
                    self.rhythm_points_current = self.rhythm_points_base
                if aif.ILLUSIONIST in self.char_class:
                    self.spell_cards_base = fn.roll_dice(1)

        self.random_attributes()
        self.save()

    def random_attributes(self):
        _race = getattr(importlib.import_module("aif_playerstome.races"), self.race.replace(" ", ""))()
        hw = _race.attributes[self.gender].split(",")
        self.age = self.variance(_race.attributes[aif.AGE])
        inches = self.variance(int(hw[0]))
        feet = int(inches / 12)
        self.height = str(feet) + "' " + str(inches - (feet * 12)) + "\""
        self.weight = self.variance(int(hw[1]))
        self.silver_amount = fn.roll_dice(3) * 10
        self.save()
        
    def is_spellcaster(self):
        return self.check_spell_caster(aif.spell_casters)

    def uses_spellpoints(self):
        if self.char_class == aif.BARD or self.char_class == aif.ILLUSIONIST:
            return False
        else:
            return True

    def is_wizard(self):
        return self.check_spell_caster(aif.wizards)
    
    def is_priest(self):
        return self.check_spell_caster(aif.priests)

    def check_spell_caster(self, _list):
        if "/" not in self.char_class:
            return self.char_class in _list
        else:
            for cls in self.char_class.split("/"):
                if cls in _list:
                    return True
        return False

    def adjust(self):

        d0 = decimal.Decimal('0')
        d100 = decimal.Decimal('100')
        self.total_load = d0

        # Fatigue Penalty
        fatigue_penalty = 0
        # if "Yawp" not in self[aif.BUFFS_LIST]:
        #    if self[aif.FATIGUE] and self[aif.FATIGUE] > 0:
        #        fatigue_penalty = -2 * int(self[aif.FATIGUE] / self[aif.ENDURANCE][aif.ADJ])

        # reset buff fields
        self.movement = ""
        self.walking_buff = 0
        self.str_buff = 0
        self.dex_buff = 0
        self.int_buff = 0
        self.health_buff = 0
        self.knockdown_buff = 0
        self.defense_buff = 0
        self.stun_buff = 0
        self.endurance_buff = 0
        self.damage_dice_buff = 0
        self.damage_mods_buff = 0
        self.to_hit_dice_buff = 0
        self.to_hit_mods_buff = 0
        self.actions_buff = 0
        self.spbc_buff = 0

        # Apply Buffs - original code in desktop/character.py
        '''
        for buff in self[aif.BUFFS_LIST]:
            if "classes.Paladin.recover_" in self[aif.BSP + buff][aif.METHOD]:
                continue
            else:
                pass
            effects = self[aif.BSP + buff][aif.EFFECTS]
            for effect in effects:
                fields = effect[aif.FIELD].split("::")
                if isinstance(effect[aif.BUFF], str):
                    if "::" not in effect[aif.FIELD]:
                        self[fields[0]] = effect[aif.BUFF]
                    else:
                        self[fields[0]][fields[1]] = effect[aif.BUFF]
                else:
                    if "::" not in effect[aif.FIELD]:
                        self[fields[0]] += effect[aif.BUFF]
                    else:
                        self[fields[0]][fields[1]] += effect[aif.BUFF]

        '''

        # Buff stats, get new buffed stat bonuses
        move_mods = 0
        # strength
        self.str_display = self.str_base + self.str_buff
        asm = Character.ability_score_mod(self.str_display)
        self.str_modifiers = ("+" if asm > 0 else "") + str(asm)
        move_mods += asm

        # dexterity
        self.dex_display = self.dex_base + self.dex_buff
        asm = Character.ability_score_mod(self.dex_display)
        self.dex_modifiers = ("+" if asm > 0 else "") + str(asm)
        move_mods += asm

        # intelligence
        self.int_display = self.int_base + self.int_buff
        asm = Character.ability_score_mod(self.int_display)
        self.int_modifiers = ("+" if asm > 0 else "") + str(asm)
        move_mods += asm

        # health
        self.health_display = self.health_base + self.health_buff
        self.health_modifiers = "-"

        # adjust movement based on buffed stats
        self.walking_display = self.walking_base + self.walking_buff + move_mods + fatigue_penalty

        # check for movement buff - right now only from speed,
        if self.movement != "":
            if "*" in self.movement:
                self.walking_display = self.walking_display * int(self.movement[1:])
        # running & swimming from walking
        self.running_display = self.walking_display * 2
        self.swimming_display = round(self.walking_display / 2)

        # auto set level, next level, actions and save dice
        xp_dict = Character.generate_xp_dict()
        for level in xp_dict:
            low = xp_dict[level][0]
            high = xp_dict[level][-1]
            if level == 1:
                low = 0
            if low <= self.experience <= high:
                self.level = level
                self.next_level = high + 1
                break
        level_by_four = round(self.level / 4)
        self.actions_base = 1 + level_by_four
        if aif.PALADIN in self.char_class:
            self.honor_points_base = self.level + 1

        # update save roll stat bonuses
        self.withstand_modifiers = int(self.str_modifiers) + fatigue_penalty
        self.withstand_modifiers = ("+" if self.withstand_modifiers > 0 else "") + str(self.withstand_modifiers)
        self.dodge_modifiers = int(self.dex_modifiers) + fatigue_penalty
        self.dodge_modifiers = ("+" if self.dodge_modifiers > 0 else "") + str(self.dodge_modifiers)
        self.resist_modifiers = int(self.int_modifiers) + fatigue_penalty
        self.resist_modifiers = ("+" if self.resist_modifiers > 0 else "") + str(self.resist_modifiers)

        self.withstand_display = str(self.withstand_dice + level_by_four) + "d6" + \
            (self.withstand_modifiers if not self.withstand_modifiers == "0" else "")
        self.dodge_display = str(self.dodge_dice + level_by_four) + "d6" + \
            (self.dodge_modifiers if not self.dodge_modifiers == "0" else "")
        self.resist_display = str(self.resist_dice + level_by_four) + "d6" + \
            (self.resist_modifiers if not self.resist_modifiers == "0" else "")

        # update combat factor base value on buffed stats
        self.knockdown_base = round(self.str_display / 2)
        self.stun_base = round(self.int_display / 2)
        self.defense_base = round((self.str_display + self.dex_display + self.int_display) / 3)

        # add in combat factor adjustments from leveling
        self.knockdown_display = self.knockdown_base + self.knockdown_cf_points + self.knockdown_buff
        self.stun_display = self.stun_base + self.stun_cf_points + self.stun_buff
        self.defense_display = self.defense_base + self.defense_cf_points + self.defense_buff
        self.endurance_display = self.endurance_base + self.endurance_cf_points + self.endurance_buff

        # update to hit/damage modifier display values
        # This should include dice bonuses from things like onslaught spell. Needs to be fixed.
        self.to_hit_mods_base = int(self.dex_modifiers)
        self.to_hit_mods_display = self.to_hit_mods_base
        self.damage_mods_base = int(self.str_modifiers)
        self.damage_mods_display = self.damage_mods_base
        self.to_hit_mods_buff += fatigue_penalty
        # check on this
        # self.damage_mods_buff += fatigue_penalty

        # include action modifiers from things like speed spell
        self.actions_display = str(self.actions_base + self.actions_buff)

        # set search roll display strings
        self.outside_search_display = str(self.outside_search_dice) + "d6" + \
            Character.dice_mod_string(self.outside_search_modifiers + fatigue_penalty)
        self.underground_search_display = str(self.underground_search_dice) + "d6" + \
            Character.dice_mod_string(self.underground_search_modifiers + fatigue_penalty)

        # get racial skill descriptions. Refactor so it's not constantly being called.
        # descriptions = self.race.get_racial_skill_descriptions(self[aif.RACIAL_SKILLS])
        # for skill in descriptions:
        #    self[aif.RSP + skill][aif.DESC] = descriptions[skill]

        # initialize var to track number of mastered skills
        mastered_skills = 0

        # calculate racial skill order values from rank
        for skill in self.skills_set.all():
            skill.display = skill.rank + skill.buff
            skill.order = int(skill.display / 4)
            skill.save()
            if skill.name == 'Toughness':
                if self.armor_set.filter(name='Toughness').count() == 0:
                    a = self.armor_set.create(name='Toughness', rank=skill.rank, display=skill.display)
                    a.description = a.name
                    a.load = "-"
                else:
                    a = self.armor_set.get(name='Toughness')
                a.slashing = skill.order
                a.piercing = skill.order
                a.bludgeoning = skill.order
                a.cleaving = skill.order
                a.save()
            if skill.mastered:
                mastered_skills += 1

        # calculate spell order values from rank
        for skill in self.spells_set.all():
            skill.display = skill.rank + skill.buff
            skill.order = int(skill.display / 4)
            skill.save()
            if skill.mastered:
                mastered_skills += 1

        # apply racial skill buffs/get racial skill tips
        # self.race.apply_skills(self)

        # apply class skill buffs/get class skill tips
        # for cls in self.classes:
        #    self.classes[cls].apply_skills(self)

        # this should eventually go away. For now, dump the weapon skill rank from Skills into 
        # the weapon.rank field.
        for weapon in self.weapons_set.all():
            if weapon.skill_pk == 0:
                if self.skills_set.filter(skill_type=aif.WEAPON, name=weapon.name).count() > 0:
                    ws = self.skills_set.get(skill_type=aif.WEAPON, name=weapon.name)
                    weapon.skill_pk = ws.pk
                    weapon.rank = ws.rank
                    weapon.save()
            else:
                if self.skills_set.filter(pk=weapon.skill_pk).count() > 0:
                    ws = self.skills_set.get(pk=weapon.skill_pk)
                    weapon.rank = ws.rank
                    weapon.save()

        # calculate weapon order values, get SPBC order values to buff damage dice, calculate total weapon load
        spbc = {}
        self.weapons_total_load = d0
        for weapon in self.weapons_set.all():
            weapon.order = int(weapon.rank / 4)
            if aif.GROUP in weapon.name:
                spbc[weapon.type] = weapon.order
            self.weapons_total_load += Character.load_to_num(weapon.load)
            if weapon.mastered:
                mastered_skills += 1
            weapon.save()

        # calculate weapon to hit/damage dice rolls with buffs applied.
        for weapon in self.weapons_set.all():
            weapon.to_hit_display = ""
            weapon.damage_display = ""
            if aif.GROUP in weapon.name or weapon.size == '-':
                weapon.save()
                continue
            weapon.melee_display = ""
            weapon.missile_display = ""
            weapon.save()

            # factor in modifiers for melee and missile to hit
            thmodstr = ""

            to_hit_mods = self.to_hit_mods_base + self.to_hit_mods_buff
            if weapon.is_melee:
                weapon.melee_display = Character.dice_mod_string(weapon.melee_modifier + to_hit_mods)
                thmodstr = weapon.melee_display
            if weapon.is_missile:
                weapon.missile_display = Character.dice_mod_string(weapon.missile_modifier + to_hit_mods)
                thmodstr += "" if thmodstr == "" else "/"
                thmodstr += weapon.missile_display

            # calculate to hit dice - base + any buffs.
            nd = self.to_hit_dice_base + self.to_hit_dice_buff

            weapon.to_hit_display = str(nd + weapon.order) + "d6" + thmodstr
            dmg = weapon.damage.split("d6")
            dmg[0] = int(dmg[0]) + spbc[weapon.type] + self.damage_dice_buff
            if len(dmg) == 1:
                dmg.append(0)
            if dmg[1] == '':
                dmg[1] = 0
            dmg[1] = int(dmg[1]) + int(self.str_modifiers if not self.str_modifiers == "" else "0")
            weapon.damage_display = str(dmg[0]) + "d6" + Character.dice_mod_string(dmg[1])
            if weapon.is_melee:
                d6 = str(nd + weapon.order + dmg[0]) + "d6"
                ms = dmg[1] + (0 if weapon.melee_display == "" else int(weapon.melee_display))
                weapon.melee_display = d6 + Character.dice_mod_string(ms)
            if weapon.is_missile:
                d6 = str(nd + weapon.order + dmg[0]) + "d6"
                ms = dmg[1] + (0 if weapon.missile_display == "" else int(weapon.missile_display))
                weapon.missile_display = d6 + Character.dice_mod_string(ms)
            weapon.save()

        # calculate armor order values, total armor load
        self.armor_total_load = d0
        defense_adj = 0
        t_spbc = str(self.spbc_buff) + "/" + str(self.spbc_buff)
        total_spbc = {aif.SLASHING: t_spbc, aif.PIERCING: t_spbc, aif.BLUDGEONING: t_spbc, aif.CLEAVING: t_spbc}

        # this should eventually go away. For now, dump the armor skill rank from Skills into 
        # the armor.rank field.
        for armor in self.armor_set.all():
            if armor.skill_pk == 0:
                if self.skills_set.filter(skill_type=aif.ARMOR, name=armor.name).count() > 0:
                    ws = self.skills_set.get(skill_type=aif.ARMOR, name=armor.name)
                    armor.skill_pk = ws.pk
                    armor.rank = ws.rank
                    armor.save()
            else:
                if self.skills_set.filter(pk=armor.skill_pk).count() > 0:
                    ws = self.skills_set.get(pk=armor.skill_pk)
                    armor.rank = ws.rank
                    armor.save()

        for armor in self.armor_set.all():
            armor.order = ""
            ordered = False
            if isinstance(armor.rank, int):
                armor.order = int(armor.rank / 4)
                ordered = True
                if aif.GROUP in armor.name:
                    defense_adj += armor.order

            spbc_display = {aif.SLASHING: armor.slashing, aif.PIERCING: armor.piercing,
                             aif.BLUDGEONING: armor.bludgeoning, aif.CLEAVING: armor.cleaving}
            if aif.GROUP not in armor.name and not armor.load == "-":
                if ordered:
                    spbc_display = {aif.SLASHING: int(armor.slashing), aif.PIERCING: int(armor.piercing),
                                     aif.BLUDGEONING: int(armor.bludgeoning), aif.CLEAVING: int(armor.cleaving)}
                    for spbc in [aif.SLASHING, aif.PIERCING, aif.BLUDGEONING, aif.CLEAVING]:
                        spbc_display[spbc] += armor.order
                        t_spbc = total_spbc[spbc].split("/")
                        if "helm" in armor.name.lower():
                            t_spbc[1] = int(t_spbc[1]) + int(spbc_display[spbc])
                        else:
                            t_spbc[0] = int(t_spbc[0]) + int(spbc_display[spbc])
                            t_spbc[1] = int(t_spbc[1]) + int(spbc_display[spbc])
                        total_spbc[spbc] = str(t_spbc[0]) + "/" + str(t_spbc[1])
            self.armor_total_load += Character.load_to_num(armor.load)
            armor.slashing_display = spbc_display[aif.SLASHING]
            armor.piercing_display = spbc_display[aif.PIERCING]
            armor.bludgeoning_display = spbc_display[aif.BLUDGEONING]
            armor.cleaving_display = spbc_display[aif.CLEAVING]
            if armor.mastered:
                mastered_skills += 1
            armor.save()

        for spbc in [aif.SLASHING, aif.PIERCING, aif.BLUDGEONING, aif.CLEAVING]:
            t_spbc = total_spbc[spbc].split("/")
            if int(t_spbc[0]) == int(t_spbc[1]):
                total_spbc[spbc] = t_spbc[0]

        '''
        # calculate armor order values, total armor load
        self[aif.ASP + aif.TOTAL_LOAD] = 0
        defense_adj = 0
        for spbc in [aif.SLASHING, aif.PIERCING, aif.BLUDGEONING, aif.CLEAVING]:
            self[aif.ASP + aif.TOTAL + spbc] = str(self[aif.SPBC_BUFF]) + "/" + str(self[aif.SPBC_BUFF])

        for armor in self[aif.ARMOR_LIST]:
            self[aif.ASP + armor][aif.ORDER] = ""
            ordered = False
            if isinstance(self[aif.ASP + armor][aif.RANK], int):
                self[aif.ASP + armor][aif.ORDER] = int(self[aif.ASP + armor][aif.RANK] / 4)
                ordered = True
                if aif.GROUP in armor:
                    defense_adj += self[aif.ASP + armor][aif.ORDER]

            for spbc in [aif.SLASHING, aif.PIERCING, aif.BLUDGEONING, aif.CLEAVING]:
                self[aif.ASP + armor][spbc + aif.ADJ] = self[aif.ASP + armor][spbc]
                if aif.GROUP not in armor and not self[aif.ASP + armor][aif.LOAD] == "-":
                    if ordered:
                        self[aif.ASP + armor][spbc + aif.ADJ] += self[aif.ASP + armor][aif.ORDER]
                    t_spbc = self[aif.ASP + aif.TOTAL + spbc].split("/")
                    if "helm" in armor.lower():
                        t_spbc[1] = int(t_spbc[1]) + int(self[aif.ASP + armor][spbc + aif.ADJ])
                    else:
                        t_spbc[0] = int(t_spbc[0]) + int(self[aif.ASP + armor][spbc + aif.ADJ])
                        t_spbc[1] = int(t_spbc[1]) + int(self[aif.ASP + armor][spbc + aif.ADJ])
                    self[aif.ASP + aif.TOTAL + spbc] = str(t_spbc[0]) + "/" + str(t_spbc[1])
            if not isinstance(self[aif.ASP + armor][aif.LOAD], str):
                if self[aif.ASP + armor][aif.LOAD] > 0:
                    self[aif.ASP + aif.TOTAL_LOAD] += self[aif.ASP + armor][aif.LOAD]
            if self[aif.ASP + armor][aif.MASTERED]:
                mastered_skills += 1

        for spbc in [aif.SLASHING, aif.PIERCING, aif.BLUDGEONING, aif.CLEAVING]:
            t_spbc = self[aif.ASP + aif.TOTAL + spbc].split("/")
            if int(t_spbc[0]) == int(t_spbc[1]):
                self[aif.ASP + aif.TOTAL + spbc] = t_spbc[0]

        self[aif.DEFENSE][aif.ADJ] += defense_adj

        self[aif.MASTERED] = mastered_skills

        nd = self[aif.TO_HIT + aif.DICE][aif.BUFF]
        dice_str = str(nd) + "d6" if nd > 0 else ""
        self[aif.TO_HIT + aif.ADJ] = dice_str + \
            Fn.dice_mod_string(self[aif.TO_HIT + aif.MODIFIERS][aif.BASE] + self[aif.TO_HIT + aif.MODIFIERS][aif.BUFF])

        nd = self[aif.DAMAGE + aif.DICE][aif.BUFF]
        dice_str = str(nd) + "d6" if nd > 0 else ""
        self[aif.DAMAGE + aif.ADJ] = dice_str + \
            Fn.dice_mod_string(self[aif.DAMAGE + aif.MODIFIERS][aif.BASE] + self[aif.DAMAGE + aif.MODIFIERS][aif.BUFF])


        '''

        self.total_slashing_protection = total_spbc[aif.SLASHING]
        self.total_piercing_protection = total_spbc[aif.PIERCING]
        self.total_bludgeoning_protection = total_spbc[aif.BLUDGEONING]
        self.total_cleaving_protection = total_spbc[aif.CLEAVING]

        self.defense_display += defense_adj

        self.mastered_count = mastered_skills
        
        '''

        nd = self[aif.TO_HIT + aif.DICE][aif.BUFF]
        dice_str = str(nd) + "d6" if nd > 0 else ""
        self[aif.TO_HIT + aif.ADJ] = dice_str + \
            Fn.dice_mod_string(self[aif.TO_HIT + aif.MODIFIERS][aif.BASE] + self[aif.TO_HIT + aif.MODIFIERS][aif.BUFF])

        nd = self[aif.DAMAGE + aif.DICE][aif.BUFF]
        dice_str = str(nd) + "d6" if nd > 0 else ""
        self[aif.DAMAGE + aif.ADJ] = dice_str + \
            Fn.dice_mod_string(self[aif.DAMAGE + aif.MODIFIERS][aif.BASE] + self[aif.DAMAGE + aif.MODIFIERS][aif.BUFF])

        _containers = {aif.CONTAINER_1: aif.C1P, aif.CONTAINER_2: aif.C2P, aif.CONTAINER_3: aif.C3P,
                       aif.CONTAINER_4: aif.C4P}
        for container in self[aif.CONTAINER_LIST]:
            if any(key.startswith(_containers[container]) for key in self):
                _total_load = 0
                for k2 in self:
                    if k2.startswith(_containers[container]):
                        if isinstance(self[k2], dict):
                            if aif.WORN in self[k2] and self[k2][aif.WORN]:
                                pass
                            elif aif.IN_CONTAINER in self[k2] and self[k2][aif.IN_CONTAINER]:
                                pass
                            else:
                                _total_load += self[k2][aif.LOAD]
                self[_containers[container] + aif.TOTAL_LOAD] = _total_load

        self[aif.ENCUMBRANCE] = (self[aif.STR][aif.ADJ] * 2) + self[aif.MODIFIERS]
        self[aif.BURDENED] = self[aif.STR][aif.ADJ] + self[aif.MODIFIERS]
        self[aif.TOTAL_LOAD] = self[aif.WSP + aif.TOTAL_LOAD] + self[aif.ASP + aif.TOTAL_LOAD]
        self[aif.TOTAL_LOAD] += self[aif.GP][aif.LOAD] + self[aif.SP][aif.LOAD] + self[aif.CP][aif.LOAD]
        for container in self[aif.CONTAINER_LIST]:
            if (_containers[container] + aif.TOTAL_LOAD) in self:
                self[aif.TOTAL_LOAD] += self[_containers[container] + aif.TOTAL_LOAD]
        
        '''

        self.money_total_load = d0
        self.gold_load = self.gold_amount / d100
        self.silver_load = self.silver_amount / d100
        self.copper_load = self.copper_amount / d100
        self.money_total_load = self.gold_load + self.silver_load + self.copper_load

        self.total_load = self.armor_total_load + self.money_total_load + self.weapons_total_load
        self.save()

    def get_class_skills(self):
        return self.skills_set.filter(skill_type=aif.CLASS)

    def get_racial_skills(self):
        return self.skills_set.filter(skill_type=aif.RACIAL)

    def get_spell_skills(self):
        return self.skills_set.filter(skill_type=aif.SPELL)

    def get_honor_skills(self):
        return self.skills_set.filter(skill_type=aif.HONOR)

    def get_weapon_skills(self):
        return self.skills_set.filter(skill_type=aif.WEAPON)

    def get_armor_skills(self):
        return self.skills_set.filter(skill_type=aif.ARMOR)

    def add_buff(self, name, start, end, buff):
        b = self.buffs_set.create(name=name)
        self.save()
        b.start_round = start
        b.end_round = end
        b.buff = buff
        b.save()
        self.save()

    def add_container(self, name, description="", capacity=0):
        c = self.container_set.create(name=name)
        c.description = description if description != "" else name
        c.max_load_capacity = capacity if capacity > 0 else 0
        self.save()
        c.save()

        if EquipmentCatalog.objects.filter(name=name).count() > 0:
            eq = EquipmentCatalog.objects.get(name=name)
            c.equipment_pk = eq.pk
            c.max_load_capacity = eq.capacity
        c.save()

    def add_equipment(self, container, name, quantity, load, durability, in_container=False, worn=False):
        c = self.container_set.get(name=container)
        e = c.equipment_set.create(description=name)
        c.save()
        e.quantity = quantity
        e.load = load
        e.durability = durability
        e.in_container = in_container
        e.worn = worn
        e.save()
        c.save()
        self.save()

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/character", Character)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/character", Character)

    @staticmethod
    def load_to_num(load):
        if load.isnumeric():
            return int(load)
        elif "/" in load:
            nd = load.split("/")
            return nd[1] / nd[0]
        else:
            return 0

    @staticmethod
    def dice_mod_string(_number):
        number = str(_number)
        return "" if number == "0" else (("" if number[:1] == "-" else "+") + number)

    @staticmethod
    def variance(number_in):
        ten_pct = round(number_in / 10)
        var = random.randint((-1 * ten_pct), ten_pct)
        return number_in + var

    @staticmethod
    def ability_score_mod(ability):
        if ability < 4:
            return -3
        elif ability < 6:
            return -2
        elif ability < 8:
            return -1
        elif ability < 14:
            return 0
        else:
            i = 1
            while ability > (13 + (i * 2)):
                i += 1
            return i

    @staticmethod
    def generate_xp_dict():
        xp = 0
        xp_dict = {}
        xp_list = []
        for level in range(31):
            steps = 5 + level
            multiple = 2 * (level + 1)
            for step in range(steps):
                xp += multiple
                xp_list.append(xp)
                
            _last = xp_list[-1]
            del xp_list[-1]
            xp_list.append(_last - 1)
            xp_dict[level + 1] = xp_list
            xp_list = [_last]
        return xp_dict


class Armor(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill = models.IntegerField(default=0)
    skill_pk = models.IntegerField(default=0)
    weapon_pk = models.IntegerField(default=0)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    type = models.CharField(max_length=5, default="")
    durability = models.CharField(max_length=5, default="")
    slashing = models.CharField(max_length=5, default="")
    slashing_display = models.CharField(max_length=5, default="")
    piercing = models.CharField(max_length=5, default="")
    piercing_display = models.CharField(max_length=5, default="")
    bludgeoning = models.CharField(max_length=5, default="")
    bludgeoning_display = models.CharField(max_length=5, default="")
    cleaving = models.CharField(max_length=5, default="")
    cleaving_display = models.CharField(max_length=5, default="")
    load = models.CharField(max_length=5, default="")
    carried = models.CharField(max_length=5, default="")
    rank = models.IntegerField(default=0)
    display = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/armor", Armor)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/armor", Armor)


class Buffs(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    start_round = models.IntegerField(default=0)
    end_round = models.IntegerField(default=0)
    buff = models.CharField(max_length=200)

    # {aif.METHOD: method, aif.START: start, aif.DURATION: duration, aif.BASE + aif.DURATION: duration,
    #        aif.EFFECTS: effects, aif.DESC: desc[:-2], aif.RANK: rank,
    #        aif.DATE: char[aif.DATE], aif.TIME: char[aif.TIME]}

    class Meta:
        app_label = application_label

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/buffs", Buffs)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/buffs", Buffs)


class Container(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    equipment_pk = models.IntegerField(default=0)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    max_load_capacity = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    current_load = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    class Meta:
        app_label = application_label

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/container", Container)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/container", Container)


class Equipment(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    equipment_pk = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default="")
    durability = models.CharField(max_length=5, default="")
    display = models.CharField(max_length=5, default="")
    load = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    quantity = models.IntegerField(default=0)
    worn = models.BooleanField(default=False)
    in_container = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['description']

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/equipment", Equipment)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/equipment", Equipment)


class Skills(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default="")
    sort_order = models.IntegerField(default=0)
    skill_type = models.CharField(max_length=10, default="")
    skill_class = models.CharField(max_length=20, default="")
    description = models.CharField(max_length=200, default="")
    rank = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    display = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['skill_type', 'sort_order', 'name']

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/skills", Skills)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/skills", Skills)


class Spells(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default="")
    circle = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    display = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    vessel = models.BooleanField(default=False)
    vessel_power = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['name']

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/spells", Spells)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/spells", Spells)


class Tips(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    tip = models.TextField()

    class Meta:
        app_label = application_label

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/tips", Tips)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/tips", Tips)


class Weapons(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    skill_pk = models.IntegerField(default=0)
    weapon_pk = models.IntegerField(default=0)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    size = models.CharField(max_length=5, default="")
    type = models.CharField(max_length=5, default="")
    damage = models.CharField(max_length=5, default="")
    range = models.CharField(max_length=5, default="")
    durability = models.CharField(max_length=5, default="")
    load = models.CharField(max_length=5, default="")
    rank = models.IntegerField(default=0)
    display = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)
    to_hit_display = models.CharField(max_length=15, default="")
    damage_display = models.CharField(max_length=15, default="")
    is_melee = models.BooleanField(default=False)
    melee_modifier = models.IntegerField(default=0)
    melee_display = models.CharField(max_length=15, default="")
    is_missile = models.BooleanField(default=False)
    missile_modifier = models.IntegerField(default=0)
    missile_display = models.CharField(max_length=15, default="")

    class Meta:
        app_label = application_label

    @staticmethod
    def deserialize():
        data_serializer.deserialize_object(__file__, "/data/weapons", Weapons)

    @staticmethod
    def serialize():
        data_serializer.serialize_object(__file__, "/data/weapons", Weapons)


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        # fields = ['name', 'race', 'gender', 'age', 'weight', 'height', 'experience',
        fields = ['gender', 'age', 'weight', 'height', 'experience',
                  'str_base', 'dex_base', 'int_base', 'health_base',
                  'knockdown_display', 'defense_display', 'stun_display', 'endurance_display',
                  'gold_amount', 'silver_amount', 'copper_amount']


class CharacterForm2(ModelForm):
    class Meta:
        model = Character
        # fields = ['name', 'race', 'gender', 'age', 'weight', 'height', 'experience',
        fields = ['gender', 'age', 'weight', 'height', 'experience',
                  'str_base', 'dex_base', 'int_base', 'health_base',
                  'knockdown_cf_points', 'defense_cf_points', 'stun_cf_points', 'endurance_cf_points',
                  'gold_amount', 'silver_amount', 'copper_amount']


class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = ['skill_type', 'name', 'rank', 'mastered']
        
        
'''
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
