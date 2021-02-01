import importlib
import os
import json
import decimal
from django.core import serializers
import random
from django.db import models
from django.forms import ModelForm
from aif import constants as aif
from aif_campaign import functions as fn
from aif_playerstome import races, classes, spells
from aif_playerstome.models import Spells as SpellsList
from aif_playerstome.models import Weapons as WeaponsCatalog

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
    walking_adjusted = models.IntegerField(default=0)
    running_base = models.IntegerField(default=0)
    running_buff = models.IntegerField(default=0)
    running_adjusted = models.IntegerField(default=0)
    swimming_base = models.IntegerField(default=0)
    swimming_buff = models.IntegerField(default=0)
    swimming_adjusted = models.IntegerField(default=0)

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
    str_adjusted = models.IntegerField(default=0)
    str_modifiers = models.CharField(max_length=10, default="")

    dex_base = models.IntegerField(default=0)
    dex_buff = models.IntegerField(default=0)
    dex_adjusted = models.IntegerField(default=0)
    dex_modifiers = models.CharField(max_length=10, default="")

    int_base = models.IntegerField(default=0)
    int_buff = models.IntegerField(default=0)
    int_adjusted = models.IntegerField(default=0)
    int_modifiers = models.CharField(max_length=10, default="")

    health_base = models.IntegerField(default=0)
    health_buff = models.IntegerField(default=0)
    health_adjusted = models.IntegerField(default=0)
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
    knockdown_adjusted = models.IntegerField(default=0)

    defense_base = models.IntegerField(default=0)
    defense_buff = models.IntegerField(default=0)
    defense_cf_points = models.IntegerField(default=0)
    defense_adjusted = models.IntegerField(default=0)

    stun_base = models.IntegerField(default=0)
    stun_buff = models.IntegerField(default=0)
    stun_cf_points = models.IntegerField(default=0)
    stun_adjusted = models.IntegerField(default=0)
    stun_current = models.IntegerField(default=0)

    endurance_base = models.IntegerField(default=0)
    endurance_cf_points = models.IntegerField(default=0)
    endurance_buff = models.IntegerField(default=0)
    endurance_adjusted = models.IntegerField(default=0)

    fatigue = models.IntegerField(default=0)
    extra_fatigue = models.IntegerField(default=0)

    withstand_dice = models.IntegerField(default=3)
    withstand_modifiers = models.CharField(max_length=10)
    withstand_adjusted = models.CharField(max_length=10)

    dodge_dice = models.IntegerField(default=3)
    dodge_modifiers = models.CharField(max_length=10)
    dodge_adjusted = models.CharField(max_length=10)

    resist_dice = models.IntegerField(default=3)
    resist_modifiers = models.CharField(max_length=10)
    resist_adjusted = models.CharField(max_length=10)

    damage_dice_base = models.IntegerField(default=0)
    damage_dice_buff = models.IntegerField(default=0)
    damage_dice_adjusted = models.CharField(max_length=15)

    damage_mods_base = models.IntegerField(default=0)
    damage_mods_buff = models.IntegerField(default=0)
    damage_mods_adjusted = models.CharField(max_length=15)

    damage_adjusted = models.CharField(max_length=15)

    to_hit_dice_base = models.IntegerField(default=0)
    to_hit_dice_buff = models.IntegerField(default=0)
    to_hit_dice_adjusted = models.CharField(max_length=15)

    to_hit_mods_base = models.IntegerField(default=0)
    to_hit_mods_buff = models.IntegerField(default=0)
    to_hit_mods_adjusted = models.CharField(max_length=15)

    to_hit_adjusted = models.CharField(max_length=15)

    actions_base = models.IntegerField(default=1)
    actions_buff = models.IntegerField(default=0)
    actions_adjusted = models.CharField(max_length=15)

    outside_search_dice = models.IntegerField(default=3)
    outside_search_modifiers = models.IntegerField(default=0)
    outside_search_adjusted = models.CharField(max_length=15)

    underground_search_dice = models.IntegerField(default=3)
    underground_search_modifiers = models.IntegerField(default=0)
    underground_search_adjusted = models.CharField(max_length=15)

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
                rs = self.racialskills_set.create(name=skill)
                rs.save()
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
                cs = self.classskills_set.create(name=skill)
                cs.save()
                sk = self.skills_set.create(name=skill, skill_type=aif.CLASS)
                sk.save()

            if aif.PALADIN in self.char_class:
                self.honor_points_base = 2
                self.honor_points_current = self.honor_points_base
                sort_order = 0
                for skill in _classes[aif.PALADIN].honor_skills_list:
                    hs = self.honorskills_set.create(name=skill)
                    hs.save()
                    sk = self.skills_set.create(name=skill, skill_type=aif.HONOR, sort_order=sort_order)
                    sk.save()
                    sort_order += 1

            if self.is_spellcaster():
                for circle in range(1, 6):
                    self.spellskills_set.create(name="Circle " + str(circle) + " Spell Group").save()
                    sk = self.skills_set.create(name="Circle " + str(circle) + " Spell Group",
                                                skill_type=aif.SPELL)
                    sk.save()
                    if aif.ILLUSIONIST in self.char_class:
                        self.spellskills_set.create(name="Circle " + str(circle) + " Affinity").save()
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
            w = self.weapons_set.create(name=weapon)
            w.description = weapon
            w.sort_order = sort_order
            w.size = "-"
            w.type = weapons_types[weapon]
            w.load = "-"
            w.save()
            sk = self.skills_set.create(name=weapon, skill_type=aif.WEAPON)
            sk.sort_order = sort_order
            sk.save()
            sort_order += 1

        armor_types = {aif.LIGHT_GRP: "L", aif.MEDIUM_GRP: "M", aif.HEAVY_GRP: "H", aif.HELMET_GRP: "-",
                        aif.UNARMED_GRP: "U", aif.SHIELD_GRP: "S"}
        sort_order = 0
        for armor in armor_types:
            a = self.armor_set.create(name=armor)
            a.description = armor
            a.sort_order = sort_order
            a.type = armor_types[armor]
            a.load = "-"
            a.save()
            sk = self.skills_set.create(name=armor, skill_type=aif.ARMOR)
            sk.sort_order = sort_order
            sk.save()
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
        _str = fn.roll_dice(dice[aif.STR])
        _dex = fn.roll_dice(dice[aif.DEX])
        _int = fn.roll_dice(dice[aif.INT])
        _health = fn.roll_dice(dice[aif.HLTH])
        _gender = "Male" if random.randint(0, 1) == 0 else "Female"

        self.new(_name, _race, _gender, _class, _str, _dex, _int, _health)
        self.random_attributes()
        self.save()

    def random_attributes(self):
        _race = getattr(importlib.import_module("aif_playerstome.races"), self.race.replace(" ", ""))()
        hw = _race.attributes[self.gender].split(",")
        self.age = self.variance(_race.attributes[aif.AGE])
        self.height = self.format_height(self.variance(int(hw[0])))
        self.weight = self.variance(int(hw[1]))

        self.silver_amount = random.randint(1, 20)
        self.copper_amount = random.randint(1, 20)
        self.save()
        
    def is_spellcaster(self):
        return self.check_spell_caster(aif.spell_casters)

    def is_wizard(self):
        return self.check_spell_caster(aif.wizards)
    
    def is_priest(self):
        return self.check_spell_caster(aif.priests)

    def check_spell_caster(self, _list):
        if not "/" in self.char_class:
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
        self.str_adjusted = self.str_base + self.str_buff
        asm = Character.ability_score_mod(self.str_adjusted)
        self.str_modifiers = ("+" if asm > 0 else "") + str(asm)
        move_mods += asm

        # dexterity
        self.dex_adjusted = self.dex_base + self.dex_buff
        asm = Character.ability_score_mod(self.dex_adjusted)
        self.dex_modifiers = ("+" if asm > 0 else "") + str(asm)
        move_mods += asm

        # intelligence
        self.int_adjusted = self.int_base + self.int_buff
        asm = Character.ability_score_mod(self.int_adjusted)
        self.int_modifiers = ("+" if asm > 0 else "") + str(asm)
        move_mods += asm

        # health
        self.health_adjusted = self.health_base + self.health_buff
        self.health_modifiers = "-"

        # adjust movement based on buffed stats
        self.walking_adjusted = self.walking_base + self.walking_buff + move_mods + fatigue_penalty

        # check for movement buff - right now only from speed,
        if self.movement != "":
            if "*" in self.movement:
                self.walking_adjusted = self.walking_adjusted * int(self.movement[1:])
        # running & swimming from walking
        self.running_adjusted = self.walking_adjusted * 2
        self.swimming_adjusted = round(self.walking_adjusted / 2)

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

        self.withstand_adjusted = str(self.withstand_dice + level_by_four) + "d6" + \
            (self.withstand_modifiers if not self.withstand_modifiers == "0" else "")
        self.dodge_adjusted = str(self.dodge_dice + level_by_four) + "d6" + \
            (self.dodge_modifiers if not self.dodge_modifiers == "0" else "")
        self.resist_adjusted = str(self.resist_dice + level_by_four) + "d6" + \
            (self.resist_modifiers if not self.resist_modifiers == "0" else "")

        # update combat factor base value on buffed stats
        self.knockdown_base = round(self.str_adjusted / 2)
        self.stun_base = round(self.int_adjusted / 2)
        self.defense_base = round((self.str_adjusted + self.dex_adjusted + self.int_adjusted) / 3)

        # add in combat factor adjustments from leveling
        self.knockdown_adjusted = self.knockdown_base + self.knockdown_cf_points + self.knockdown_buff
        self.stun_adjusted = self.stun_base + self.stun_cf_points + self.stun_buff
        self.defense_adjusted = self.defense_base + self.defense_cf_points + self.defense_buff
        self.endurance_adjusted = self.endurance_base + self.endurance_cf_points + self.endurance_buff

        # update to hit/damage modifier display values
        # This should include dice bonuses from things like onslaught spell. Needs to be fixed.
        self.to_hit_mods_base = int(self.dex_modifiers)
        self.to_hit_mods_adjusted = self.to_hit_mods_base
        self.damage_mods_base = int(self.str_modifiers)
        self.damage_mods_adjusted = self.damage_mods_base
        self.to_hit_mods_buff += fatigue_penalty
        # check on this
        # self.damage_mods_buff += fatigue_penalty

        # include action modifiers from things like speed spell
        self.actions_adjusted = str(self.actions_base + self.actions_buff)

        # set search roll display strings
        self.outside_search_adjusted = str(self.outside_search_dice) + "d6" + \
            Character.dice_mod_string(self.outside_search_modifiers + fatigue_penalty)
        self.underground_search_adjusted = str(self.underground_search_dice) + "d6" + \
            Character.dice_mod_string(self.underground_search_modifiers + fatigue_penalty)

        # get racial skill descriptions. Refactor so it's not constantly being called.
        # descriptions = self.race.get_racial_skill_descriptions(self[aif.RACIAL_SKILLS])
        # for skill in descriptions:
        #    self[aif.RSP + skill][aif.DESC] = descriptions[skill]

        # initialize var to track number of mastered skills
        mastered_skills = 0

        # calculate racial skill order values from rank
        for skill in self.skills_set.all():
            skill.adjusted = skill.rank + skill.buff
            skill.order = int(skill.adjusted / 4)
            skill.save()
            if skill.name == 'Toughness':
                if self.armor_set.filter(name='Toughness').count() == 0:
                    a = self.armor_set.create(name='Toughness', rank=skill.rank, adjusted=skill.adjusted)
                    a.description = a.name
                    a.load = "-"
                    a.save()
            if skill.mastered:
                mastered_skills += 1

        # calculate racial skill order values from rank
        for skill in self.racialskills_set.all():
            skill.adjusted = skill.rank + skill.buff
            skill.order = int(skill.adjusted / 4)
            skill.save()
            if skill.name == 'Toughness':
                if self.armor_set.filter(name='Toughness').count() == 0:
                    a = self.armor_set.create(name='Toughness', rank=skill.rank, adjusted=skill.adjusted)
                    a.description = a.name
                    a.load = "-"
                    a.save()
            if skill.mastered:
                mastered_skills += 1

        # calculate class skill order values from rank
        for skill in self.classskills_set.all():
            skill.adjusted = skill.rank + skill.buff
            skill.order = int(skill.adjusted / 4)
            skill.save()
            if skill.mastered:
                mastered_skills += 1

        # calculate honor skill order values from rank
        for skill in self.honorskills_set.all():
            skill.adjusted = skill.rank + skill.buff
            skill.order = int(skill.adjusted / 4)
            skill.save()
            if skill.mastered:
                mastered_skills += 1

        # calculate spell skill order values from rank
        for skill in self.spellskills_set.all():
            skill.adjusted = skill.rank + skill.buff
            skill.order = int(skill.adjusted / 4)
            skill.save()
            if skill.mastered:
                mastered_skills += 1

        # calculate spell order values from rank
        for skill in self.spells_set.all():
            skill.adjusted = skill.rank + skill.buff
            skill.order = int(skill.adjusted / 4)
            skill.save()
            if skill.mastered:
                mastered_skills += 1

        # apply racial skill buffs/get racial skill tips
        # self.race.apply_skills(self)

        # apply class skill buffs/get class skill tips
        # for cls in self.classes:
        #    self.classes[cls].apply_skills(self)

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
            weapon.to_hit_adjusted = ""
            weapon.damage_adjusted = ""
            if aif.GROUP in weapon.name or weapon.size == '-':
                weapon.save()
                continue
            weapon.melee_adjusted = ""
            weapon.missile_adjusted = ""

            # factor in modifiers for melee and missile to hit
            thmodstr = ""

            to_hit_mods = self.to_hit_mods_base + self.to_hit_mods_buff
            if weapon.is_melee:
                weapon.melee_adjusted = Character.dice_mod_string(weapon.melee_modifier + to_hit_mods)
                thmodstr = weapon.melee_adjusted
            if weapon.is_missile:
                weapon.missile_adjusted = Character.dice_mod_string(weapon.missile_modifier + to_hit_mods)
                thmodstr += "" if thmodstr == "" else "/"
                thmodstr += weapon.missile_adjusted

            # calculate to hit dice - base + any buffs.
            nd = self.to_hit_dice_base + self.to_hit_dice_buff

            weapon.to_hit_adjusted = str(nd + weapon.order) + "d6" + thmodstr
            dmg = weapon.damage.split("d6")
            dmg[0] = int(dmg[0]) + spbc[weapon.type] + self.damage_dice_buff
            if len(dmg) == 1:
                dmg.append(0)
            if dmg[1] == '':
                dmg[1] = 0
            dmg[1] = int(dmg[1]) + int(self.str_modifiers if not self.str_modifiers == "" else "0")
            weapon.damage_adjusted = str(dmg[0]) + "d6" + Character.dice_mod_string(dmg[1])
            if weapon.is_melee:
                d6 = str(nd + weapon.order + dmg[0]) + "d6"
                ms = dmg[1] + (0 if weapon.melee_adjusted == "" else int(weapon.melee_adjusted))
                weapon.melee_adjusted = d6 + Character.dice_mod_string(ms)
            if weapon.is_missile:
                d6 = str(nd + weapon.order + dmg[0]) + "d6"
                ms = dmg[1] + (0 if weapon.missile_adjusted == "" else int(weapon.missile_adjusted))
                weapon.missile_adjusted = d6 + Character.dice_mod_string(ms)
            weapon.save()

        # calculate armor order values, total armor load
        self.armor_total_load = d0
        defense_adj = 0
        t_spbc = str(self.spbc_buff) + "/" + str(self.spbc_buff)
        total_spbc = {aif.SLASHING: t_spbc, aif.PIERCING: t_spbc, aif.BLUDGEONING: t_spbc, aif.CLEAVING: t_spbc}

        for armor in self.armor_set.all():
            armor.order = ""
            ordered = False
            if isinstance(armor.rank, int):
                armor.order = int(armor.rank / 4)
                ordered = True
                if aif.GROUP in armor.name:
                    defense_adj += armor.order

            spbc_adjusted = {aif.SLASHING: armor.slashing, aif.PIERCING: armor.piercing,
                             aif.BLUDGEONING: armor.bludgeoning, aif.CLEAVING: armor.cleaving}
            if aif.GROUP not in armor.name and not armor.load == "-":
                if ordered:
                    spbc_adjusted = {aif.SLASHING: int(armor.slashing), aif.PIERCING: int(armor.piercing),
                                     aif.BLUDGEONING: int(armor.bludgeoning), aif.CLEAVING: int(armor.cleaving)}
                    for spbc in [aif.SLASHING, aif.PIERCING, aif.BLUDGEONING, aif.CLEAVING]:
                        spbc_adjusted[spbc] += armor.order
                        t_spbc = total_spbc[spbc].split("/")
                        if "helm" in armor.name.lower():
                            t_spbc[1] = int(t_spbc[1]) + int(spbc_adjusted[spbc])
                        else:
                            t_spbc[0] = int(t_spbc[0]) + int(spbc_adjusted[spbc])
                            t_spbc[1] = int(t_spbc[1]) + int(spbc_adjusted[spbc])
                        total_spbc[spbc] = str(t_spbc[0]) + "/" + str(t_spbc[1])
            self.armor_total_load += Character.load_to_num(armor.load)
            armor.slashing_adjusted = spbc_adjusted[aif.SLASHING]
            armor.piercing_adjusted = spbc_adjusted[aif.PIERCING]
            armor.bludgeoning_adjusted = spbc_adjusted[aif.BLUDGEONING]
            armor.cleaving_adjusted = spbc_adjusted[aif.CLEAVING]
            if armor.mastered:
                mastered_skills += 1
            armor.save()

        for spbc in [aif.SLASHING, aif.PIERCING, aif.BLUDGEONING, aif.CLEAVING]:
            t_spbc = total_spbc[spbc].split("/")
            if int(t_spbc[0]) == int(t_spbc[1]):
                total_spbc[spbc] = t_spbc[0]

        self.total_slashing_protection = total_spbc[aif.SLASHING]
        self.total_piercing_protection = total_spbc[aif.PIERCING]
        self.total_bludgeoning_protection = total_spbc[aif.BLUDGEONING]
        self.total_cleaving_protection = total_spbc[aif.CLEAVING]

        self.defense_adjusted += defense_adj

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

    def add_buff(self, name, start, end, buff):
        b = self.buffs_set.create(name=name)
        self.save()
        b.start_round = start
        b.end_round = end
        b.buff = buff
        b.save()
        self.save()

    def add_container(self, name):
        c = self.container_set.create(name=name)
        self.save()
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
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/character.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Character.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")

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
    def format_height(number_in):
        feet = int(number_in / 12)
        inches = number_in - (feet * 12)
        return str(feet) + "' " + str(inches) + "\""

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
            # if _debug:
            #    print(str(level + 1) + ": " + str(xp_dict[level + 1][0]) + " - " + str(xp_dict[level + 1][-1]) +
            #          " : " + str(steps) + " steps,  multiple = " + str(multiple))
        return xp_dict

    @staticmethod
    def order(rank):
        return int(rank / 4)


class Spells(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default="")
    circle = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    adjusted = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    vessel = models.BooleanField(default=False)
    vessel_power = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['name']

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/spells.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Spells.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


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
    adjusted = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['skill_type', 'sort_order', 'name']

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/class_skills.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(ClassSkills.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class ClassSkills(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    rank = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    adjusted = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['name']

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/class_skills.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(ClassSkills.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class RacialSkills(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    rank = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    adjusted = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['name']

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/racial_skills.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(RacialSkills.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class HonorSkills(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    rank = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    adjusted = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['name']

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/honor_skills.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(HonorSkills.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class SpellSkills(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    rank = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    adjusted = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['name']

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/spell_skills.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(SpellSkills.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class Weapons(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
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
    adjusted = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)
    to_hit_adjusted = models.CharField(max_length=15, default="")
    damage_adjusted = models.CharField(max_length=15, default="")
    is_melee = models.BooleanField(default=False)
    melee_modifier = models.IntegerField(default=0)
    melee_adjusted = models.CharField(max_length=15, default="")
    is_missile = models.BooleanField(default=False)
    missile_modifier = models.IntegerField(default=0)
    missile_adjusted = models.CharField(max_length=15, default="")

    class Meta:
        app_label = application_label

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/weapons.json"
            json_serializer = serializers.get_serializer("json")()
            json_serializer.serialize(Weapons.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class Armor(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill = models.IntegerField(default=0)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    type = models.CharField(max_length=5, default="")
    durability = models.CharField(max_length=5, default="")
    slashing = models.CharField(max_length=5, default="")
    slashing_adjusted = models.CharField(max_length=5, default="")
    piercing = models.CharField(max_length=5, default="")
    piercing_adjusted = models.CharField(max_length=5, default="")
    bludgeoning = models.CharField(max_length=5, default="")
    bludgeoning_adjusted = models.CharField(max_length=5, default="")
    cleaving = models.CharField(max_length=5, default="")
    cleaving_adjusted = models.CharField(max_length=5, default="")
    load = models.CharField(max_length=5, default="")
    carried = models.CharField(max_length=5, default="")
    rank = models.IntegerField(default=0)
    adjusted = models.IntegerField(default=0)
    buff = models.IntegerField(default=0)
    order = models.IntegerField(default=0)
    mastered = models.BooleanField(default=False)

    class Meta:
        app_label = application_label

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/armor.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Armor.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class Container(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, default="")
    description = models.CharField(max_length=200, default="")
    max_load_capacity = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    current_load = models.DecimalField(max_digits=5, decimal_places=1, default=0)

    class Meta:
        app_label = application_label

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/container.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Container.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class Equipment(models.Model):
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default="")
    durability = models.CharField(max_length=5, default="")
    adjusted = models.CharField(max_length=5, default="")
    load = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    quantity = models.IntegerField(default=0)
    worn = models.BooleanField(default=False)
    in_container = models.BooleanField(default=False)

    class Meta:
        app_label = application_label
        ordering = ['description']

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/equipment.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Equipment.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class Tips(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    tip = models.TextField()

    class Meta:
        app_label = application_label

    @staticmethod
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/tips.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Tips.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


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
    def serialize():
        try:
            fn = os.path.dirname(os.path.realpath(__file__)) + "/data/buffs.json"
            JSONSerializer = serializers.get_serializer("json")
            json_serializer = JSONSerializer()
            json_serializer.serialize(Buffs.objects.all())
            with open(fn, "w") as out:
                out.write(json.dumps(json.loads(json_serializer.getvalue()), indent=4))
        except FileNotFoundError:
            print("file not found")


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'race', 'gender', 'age', 'weight', 'height', 'experience',
                  'str_base', 'dex_base', 'int_base', 'health_base', 'knockdown_adjusted',
                  'defense_adjusted', 'stun_adjusted', 'endurance_adjusted']


class ClassSkillsForm(ModelForm):
    class Meta:
        model = ClassSkills
        fields = ['name', 'rank', 'mastered']
