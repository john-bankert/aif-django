from django.core.management.base import BaseCommand, CommandError
from aif_character.models import Character
from aif_playerstome.models import Weapons, Armor, Skills


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        char = self.add_demo_character('Chauncy', 'Human', 'Male', 'Warrior', 16, 14, 11, 16)
        char.add_buff('Boon', 1, 5, '+1 to hit')
        char.add_container('Worn')
        char.add_equipment('Worn', 'Pants', 1, 1, 40, True, True)
        char.add_container('Backpack')
        char.add_equipment('Backpack', 'Flask of Oil', 1, 1, 10, True)
        char.add_equipment('Backpack', '50ft Rope', 1, 4, 40, True)
        char.add_container('Small Belt Pouch')
        char.add_equipment('Small Belt Pouch', 'Bottle of Ink', 1, 1, 10, True)
        Weapons.add_to_character(char, 'War Hammer')
        Armor.add_to_character(char, 'helmet', 'Leather', 'Leather Helmet')
        Armor.add_to_character(char, 'shield', 'Buckler')
        char.adjust()
        char.save()

        char = self.add_demo_character('Zandor', 'Elf', 'Male', 'Wizard', 10, 12, 18, 15)
        char.add_buff('Boon', 1, 5, '+1 to hit')
        char.add_container('Worn')
        char.add_equipment('Worn', 'Pants', 1, 1, 40, True, True)
        char.add_container('Backpack')
        char.add_equipment('Backpack', 'Flask of Oil', 1, 1, 10, True)
        char.add_equipment('Backpack', '50ft Rope', 1, 4, 40, True)
        char.add_container('Small Belt Pouch')
        char.add_equipment('Small Belt Pouch', 'Bottle of Ink', 1, 1, 10, True)
        Weapons.add_to_character(char, 'Ironshod Staff (a)')
        Armor.add_to_character(char, 'armor', 'Wool Robe')
        Armor.add_to_character(char, 'helmet', 'Wizard Hat')
        char.adjust()
        char.save()

        char = self.add_demo_character('Fredo', 'Halfling', 'Male', 'Rogue', 12, 17, 10, 14)
        char.add_buff('Boon', 1, 5, '+1 to hit')
        char.add_container('Worn')
        char.add_equipment('Worn', 'Pants', 1, 1, 40, True, True)
        char.add_container('Backpack')
        char.add_equipment('Backpack', 'Flask of Oil', 1, 1, 10, True)
        char.add_equipment('Backpack', '50ft Rope', 1, 4, 40, True)
        char.add_container('Small Belt Pouch')
        char.add_equipment('Small Belt Pouch', 'Bottle of Ink', 1, 1, 10, True)
        char.adjust()
        char.save()

        char = self.add_demo_character('Brunie', 'Dwarf', 'Female', 'Priest', 12, 13, 16, 16)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('Elanor', 'Half Elf', 'Female', 'Bard', 14, 11, 16, 15)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('Zax', 'Gnome', 'Male', 'Illusionist', 14, 11, 16, 15)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('Prosser', 'Human', 'Male', 'Paladin', 17, 13, 12, 14)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('Boudica', 'Human', 'Female', 'Paladin/Priest', 17, 14, 16, 15)
        char.add_buff('Boon', 1, 5, '+1 to hit')
        Weapons.add_to_character(char, 'Maul')
        Armor.add_to_character(char, 'armor', 'Full plate', 'Full Plate')
        Armor.add_to_character(char, 'shield', 'Buckler')
        char.adjust()
        char.save()

        char = self.add_demo_character('Rosie', 'Halfling', 'Female', 'Theurgist', 11, 14, 17, 15)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('Flanders', 'Human', 'Male', 'Witch', 12, 12, 17, 15)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('Trisha', 'Half Elf', 'Female', 'Druid', 10, 10, 18, 16)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('Glinka', 'Gnome', 'Female', 'Magician', 10, 14, 16, 16)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('Horanda', 'Dwarf', 'Female', 'Barbarian', 17, 13, 13, 17)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        char = self.add_demo_character('George', 'Human', 'Male', 'Buccaneer', 17, 15, 9, 15)
        char.add_buff('Boon', 1, 5, '+1 to hit')

        # [CHARLATAN, DIVINER, GYPSY, MONK, PARAGON, PROPHET, RANGER, SCOUT, THEURGIST, TEMPLAR, WARLOCK]
        self.add_johns_characters()

    def add_demo_character(self, _name, _race, _gender, _class, _str, _dex, _int, _health):
        if Character.objects.filter(name=_name).count() != 0:
            self.stdout.write("Deleting Character " + _name)
            c = Character.objects.get(name=_name)
            c.delete()

        self.stdout.write("Creating Character " + _name)
        c = Character()
        c.new(_name, _race, _gender, _class, _str, _dex, _int, _health)
        c.random_attributes()
        c.player = 'demo'
        c.open = True
        c.save()
        return c

    def add_johns_characters(self):
        char = self.add_demo_character('Florian', 'Elf', 'Male', 'Charlatan', 10, 15, 18, 15)
        char.player = 'John'
        char.add_buff('Boon', 1, 5, '+1 to hit')
        char.add_container('Worn')
        char.add_equipment('Worn', 'Belt', 1, 10/1, 60, True, True)
        char.add_equipment('Worn', 'Pants', 1, 1, 40, True, True)
        char.add_equipment('Worn', 'Boots', 1, 1, 30, True, True)
        char.add_equipment('Worn', 'Gloves', 1, 10/1, 40, True, True)
        char.add_equipment('Worn', 'Cloak', 1, 1, 30, True, True)
        char.add_container('Backpack')
        char.add_equipment('Backpack', 'Flask of Oil', 1, 1, 10, True)
        char.add_equipment('Backpack', '50ft Rope', 1, 4, 40, True)
        char.add_container('Small Belt Pouch')
        char.add_equipment('Small Belt Pouch', 'Bottle of Ink', 1, 1, 10, True)
        Weapons.add_to_character(char, 'Ironshod Staff (a)')
        Armor.add_to_character(char, 'armor', 'Wool Robe')
        Armor.add_to_character(char, 'helmet', 'Wizard Hat')
        char.adjust()
        char.save()

        char = self.add_demo_character('Pindar', 'Gnome', 'Male', 'Illusionist', 14, 11, 16, 15)
        char.player = 'John'
        char.save()

        _name = 'Torburn'
        if Character.objects.filter(name=_name).count() != 0:
            self.stdout.write("Deleting Character " + _name)
            c = Character.objects.get(name=_name)
            c.delete()

        self.stdout.write("Creating Character " + _name)
        char = Character()
        char.new(_name, 'Dwarf', 'Male', 'Paladin/Warrior', 18, 17, 11, 14)
        char.player = 'John'
        char.open = True
        char.health_base = 57
        char.health_current = 57
        char.age = 42
        char.height = "4' 1\""
        char.weight = "140 lb"
        char.experience = 536
        char.gold_amount = 575
        char.silver_amount = 55
        char.copper_amount = 20

        Skills.add_to_character(char, 'Armorer', 'Class', 7)
        Skills.add_to_character(char, 'Avenging Smite', 'Class', 2)
        Skills.add_to_character(char, 'Awareness', 'Class', 3)
        Skills.add_to_character(char, 'Balance', 'Class', 4)
        Skills.add_to_character(char, 'Block', 'Class', 2)
        Skills.add_to_character(char, 'Disarm', 'Class', 2)
        Skills.add_to_character(char, 'Guard', 'Class', 2)
        Skills.add_to_character(char, 'Lay on Hands', 'Class', 6)
        Skills.add_to_character(char, 'Melee', 'Class', 5)
        Skills.add_to_character(char, 'Missile', 'Class', 5)
        Skills.add_to_character(char, 'Mounted Battle', 'Class', 2)
        Skills.add_to_character(char, 'Radiant Shield', 'Class', 2)
        Skills.add_to_character(char, 'Righteous Faith', 'Class', 3)
        Skills.add_to_character(char, 'Scrapping', 'Class', 5)
        Skills.add_to_character(char, 'Stalwart Stance', 'Class', 5)
        Skills.add_to_character(char, 'Stamina', 'Class', 5)
        Skills.add_to_character(char, 'Valiant Aura', 'Class', 5)
        Skills.add_to_character(char, 'Weaponsmith', 'Class', 7)
        Skills.add_to_character(char, 'Direction Sense', 'Racial', 3)
        Skills.add_to_character(char, 'Dwarven History', 'Racial', 5)
        Skills.add_to_character(char, 'Infravision', 'Racial', 2)
        Skills.add_to_character(char, 'Mountaineering', 'Racial', 5)
        Skills.add_to_character(char, 'Stone Speak', 'Racial', 2)
        Skills.add_to_character(char, 'Toughness', 'Racial', 9, True)
        Skills.add_to_character(char, 'Yawp', 'Racial', 9, True)
        Skills.add_to_character(char, 'Increase Strength', 'Honor', 6)
        Skills.add_to_character(char, 'Increase Dexterity', 'Honor', 6)
        Skills.add_to_character(char, 'Increase Intelligence', 'Honor', 2)
        Skills.add_to_character(char, 'Increase Health', 'Honor', 2)
        Skills.add_to_character(char, 'Increase Knockdown', 'Honor', 2)
        Skills.add_to_character(char, 'Increase Defense', 'Honor', 2)
        Skills.add_to_character(char, 'Increase Stun', 'Honor', 2)
        Skills.add_to_character(char, 'Increase Endurance', 'Honor', 2)
        Skills.add_to_character(char, 'Recover Health', 'Honor', 6)
        Skills.add_to_character(char, 'Recover Stun', 'Honor', 6)
        Skills.add_to_character(char, 'Recover Fatigue', 'Honor', 6)
        Skills.add_to_character(char, 'Slashing Group', 'Weapon', 2)
        Skills.add_to_character(char, 'Piercing Group', 'Weapon', 8)
        Skills.add_to_character(char, 'Bludgeoning Group', 'Weapon', 6)
        Skills.add_to_character(char, 'Cleaving Group', 'Weapon', 2)
        Skills.add_to_character(char, 'Bow Group', 'Weapon', 4)
        Skills.add_to_character(char, 'Maul', 'Weapon', 6)
        Skills.add_to_character(char, 'Hand Axe', 'Weapon', 3)
        Skills.add_to_character(char, 'Pike', 'Weapon', 8)
        Skills.add_to_character(char, 'Medium Crossbow', 'Weapon', 8)
        Skills.add_to_character(char, 'Light Armor Group', 'Armor', 2)
        Skills.add_to_character(char, 'Medium Armor Group', 'Armor', 2)
        Skills.add_to_character(char, 'Heavy Armor Group', 'Armor', 8)
        Skills.add_to_character(char, 'Helmet Group', 'Armor', 6)
        Skills.add_to_character(char, 'Unarmed Group', 'Armor', 2)
        Skills.add_to_character(char, 'Shield Group', 'Armor', 5)
        Skills.add_to_character(char, 'Studded Leather', 'Armor', 2)
        Skills.add_to_character(char, 'Open-faced', 'Armor', 5)
        Skills.add_to_character(char, 'Plate mail', 'Armor', 8)
        Skills.add_to_character(char, 'Buckler', 'Armor', 4)
        Weapons.add_to_character(char, 'Pike', 'Pike +2, Yawp +4')
        Weapons.add_to_character(char, 'Medium Crossbow', 'Medium Crossbow +3, Toughness + 5')
        w = char.weapons_set.get(name='Medium Crossbow')
        w.damage = "2d6"
        w.type = 'P'
        w.size = 'M'
        w.load = '3'
        w.range = '135'
        w.durability = '30'
        w.save()
        Armor.add_to_character(char, 'armor', 'Plate mail', 'Plate Mail +1/2/1/1')
        Armor.add_to_character(char, 'helmet', 'Open-faced', 'Open Faced Helmet')
        Armor.add_to_character(char, 'shield', 'Buckler')
        char.add_container('Worn')
        char.add_equipment('Worn', 'Belt', 1, 10/1, 60, True, True)
        char.add_equipment('Worn', 'Pants', 1, 1, 40, True, True)
        char.add_equipment('Worn', 'Boots', 1, 1, 30, True, True)
        char.add_equipment('Worn', 'Gloves', 1, 10/1, 40, True, True)
        char.add_equipment('Worn', 'Cloak', 1, 1, 30, True, True)
        # char.add_container('Backpack')
        # char.add_equipment('Backpack', 'Flask of Oil', 1, 1, 10, True)
        # char.add_equipment('Backpack', '50ft Rope', 1, 4, 40, True)
        # char.add_container('Small Belt Pouch')
        # char.add_equipment('Small Belt Pouch', 'Bottle of Ink', 1, 1, 10, True)
        char.adjust()
        char.save()

        '''
        try:
            djc = c_model.Character.objects.get(char_name=self.char[aif.NAME])
            print(self.char[aif.NAME] + " found")
        except ObjectDoesNotExist:
            print(self.char[aif.NAME] + " not found")
            djc = c_model.Character(char_name=self.char[aif.NAME])

        djc.char_race = self.char[aif.RACE]
        djc.char_class = self.char[aif.CLASS]
        djc.char_gender = self.char[aif.GENDER]
        djc.char_age = self.char[aif.AGE]
        djc.char_height = self.char[aif.HEIGHT]
        djc.char_weight = self.char[aif.WEIGHT]
        djc.char_notes = self.char[aif.NOTES]
        djc.char_open = self.char[aif.OPEN]

        djc.char_movement = self.char[aif.MOVEMENT]
        djc.char_walking_base = self.char[aif.WALKING][aif.BASE]
        djc.char_walking_adjusted = self.char[aif.WALKING][aif.ADJ]
        djc.char_walking_buff = self.char[aif.WALKING][aif.BUFF]
        djc.char_running_base = self.char[aif.RUNNING][aif.BASE]
        djc.char_running_adjusted = self.char[aif.RUNNING][aif.ADJ]
        # djc.char_running_buff = self.char[aif.RUNNING][aif.BUFF]
        djc.char_swimming_base = self.char[aif.SWIMMING][aif.BASE]
        djc.char_swimming_adjusted = self.char[aif.SWIMMING][aif.ADJ]
        # djc.char_swimming_buff = self.char[aif.SWIMMING][aif.BUFF]

        djc.char_encumbrance = self.char[aif.ENCUMBRANCE]
        djc.char_total_load = self.char[aif.TOTAL_LOAD]
        djc.char_modifiers = self.char[aif.MODIFIERS]
        djc.char_burdened = self.char[aif.BURDENED]

        djc.char_level = self.char[aif.LEVEL]
        djc.char_experience = self.char[aif.EXPERIENCE]
        djc.char_next_level = self.char[aif.NEXT_LEVEL]

        djc.char_str_base = self.char[aif.STR][aif.BASE]
        djc.char_str_adjusted = self.char[aif.STR][aif.ADJ]
        djc.char_str_modifiers = self.char[aif.STR][aif.MODIFIERS]
        djc.char_str_buff = self.char[aif.STR][aif.BUFF]

        djc.char_dex_base = self.char[aif.DEX][aif.BASE]
        djc.char_dex_adjusted = self.char[aif.DEX][aif.ADJ]
        djc.char_dex_modifiers = self.char[aif.DEX][aif.MODIFIERS]
        djc.char_dex_buff = self.char[aif.DEX][aif.BUFF]

        djc.char_int_base = self.char[aif.INT][aif.BASE]
        djc.char_int_adjusted = self.char[aif.INT][aif.ADJ]
        djc.char_int_modifiers = self.char[aif.INT][aif.MODIFIERS]
        djc.char_int_buff = self.char[aif.INT][aif.BUFF]

        djc.char_health_base = self.char[aif.HLTH][aif.BASE]
        djc.char_health_adjusted = self.char[aif.HLTH][aif.ADJ]
        djc.char_health_modifiers = self.char[aif.HLTH][aif.MODIFIERS]
        djc.char_health_buff = self.char[aif.HLTH][aif.BUFF]
        djc.char_health_current = self.char[aif.HLTH][aif.CURRENT]

        djc.char_knockdown_base = self.char[aif.KNOCKDOWN][aif.BASE]
        djc.char_knockdown_adjusted = self.char[aif.KNOCKDOWN][aif.ADJ]
        djc.char_knockdown_cf_points = self.char[aif.KNOCKDOWN][aif.CF_ADJ]
        djc.char_knockdown_buff = self.char[aif.KNOCKDOWN][aif.BUFF]

        djc.char_defense_base = self.char[aif.DEFENSE][aif.BASE]
        djc.char_defense_adjusted = self.char[aif.DEFENSE][aif.ADJ]
        djc.char_defense_cf_points = self.char[aif.DEFENSE][aif.CF_ADJ]
        djc.char_defense_buff = self.char[aif.DEFENSE][aif.BUFF]

        djc.char_stun_base = self.char[aif.STUN][aif.BASE]
        djc.char_stun_adjusted = self.char[aif.STUN][aif.ADJ]
        djc.char_stun_cf_points = self.char[aif.STUN][aif.CF_ADJ]
        djc.char_stun_buff = self.char[aif.STUN][aif.BUFF]
        djc.char_stun_current = self.char[aif.STUN][aif.CURRENT]

        djc.char_endurance_base = self.char[aif.ENDURANCE][aif.BASE]
        djc.char_endurance_adjusted = self.char[aif.ENDURANCE][aif.ADJ]
        djc.char_endurance_cf_points = self.char[aif.ENDURANCE][aif.CF_ADJ]
        djc.char_endurance_buff = self.char[aif.ENDURANCE][aif.BUFF]

        djc.char_fatigue = self.char[aif.FATIGUE]
        djc.char_extra_fatigue = self.char[aif.EXTRA_FATIGUE]

        djc.char_withstand_dice = self.char[aif.WITHSTAND][aif.DICE]
        djc.char_withstand_modifiers = self.char[aif.WITHSTAND][aif.MODIFIERS]
        djc.char_withstand_adjusted = self.char[aif.WITHSTAND][aif.ADJ]

        djc.char_dodge_dice = self.char[aif.DODGE][aif.DICE]
        djc.char_dodge_modifiers = self.char[aif.DODGE][aif.MODIFIERS]
        djc.char_dodge_adjusted = self.char[aif.DODGE][aif.ADJ]

        djc.char_resist_dice = self.char[aif.RESIST][aif.DICE]
        djc.char_resist_modifiers = self.char[aif.RESIST][aif.MODIFIERS]
        djc.char_resist_adjusted = self.char[aif.RESIST][aif.ADJ]

        djc.char_honor_points_base = self.char[aif.HONOR_POINTS][aif.BASE]
        djc.char_honor_points_current = self.char[aif.HONOR_POINTS][aif.CURRENT]

        djc.char_spell_points_base = self.char[aif.SPELL_POINTS][aif.BASE]
        djc.char_spell_points_current = self.char[aif.SPELL_POINTS][aif.CURRENT]
        djc.char_spell_effectiveness_modifier = self.char[aif.SPELL_EFF_MOD]

        djc.char_damage_dice_base = self.char[aif.DAMAGE + aif.DICE][aif.BASE]
        djc.char_damage_dice_buff = self.char[aif.DAMAGE + aif.DICE][aif.BUFF]
        djc.char_damage_dice_adjusted = self.char[aif.DAMAGE + aif.DICE][aif.ADJ]

        djc.char_damage_mods_base = self.char[aif.DAMAGE + aif.MODIFIERS][aif.BASE]
        djc.char_damage_mods_buff = self.char[aif.DAMAGE + aif.MODIFIERS][aif.BUFF]
        djc.char_damage_mods_adjusted = self.char[aif.DAMAGE + aif.MODIFIERS][aif.ADJ]

        djc.char_damage_adjusted = self.char[aif.DAMAGE + aif.ADJ]

        djc.char_to_hit_dice_base = self.char[aif.TO_HIT + aif.DICE][aif.BASE]
        djc.char_to_hit_dice_buff = self.char[aif.TO_HIT + aif.DICE][aif.BUFF]
        djc.char_to_hit_dice_adjusted = self.char[aif.TO_HIT + aif.DICE][aif.ADJ]

        djc.char_to_hit_mods_base = self.char[aif.TO_HIT + aif.MODIFIERS][aif.BASE]
        djc.char_to_hit_mods_buff = self.char[aif.TO_HIT + aif.MODIFIERS][aif.BUFF]
        djc.char_to_hit_mods_adjusted = self.char[aif.TO_HIT + aif.MODIFIERS][aif.ADJ]

        djc.char_to_hit_adjusted = self.char[aif.TO_HIT + aif.ADJ]

        djc.char_actions_base = self.char[aif.ACTIONS][aif.BASE]
        djc.char_actions_buff = self.char[aif.ACTIONS][aif.BUFF]
        djc.char_actions_adjusted = self.char[aif.ACTIONS][aif.ADJ]

        djc.char_outside_search_dice = self.char[aif.OUTSIDE][aif.DICE]
        djc.char_outside_search_modifiers = self.char[aif.OUTSIDE][aif.MODIFIERS]
        djc.char_outside_search_adjusted = self.char[aif.OUTSIDE][aif.ADJ]

        djc.char_underground_search_dice = self.char[aif.UNDERGROUND][aif.DICE]
        djc.char_underground_search_modifiers = self.char[aif.UNDERGROUND][aif.MODIFIERS]
        djc.char_underground_search_adjusted = self.char[aif.UNDERGROUND][aif.ADJ]

        djc.char_spbc_buff = self.char[aif.SPBC_BUFF]

        djc.char_gold_amount = self.char[aif.GP][aif.AMOUNT]
        djc.char_gold_load = self.char[aif.GP][aif.LOAD]

        djc.char_silver_amount = self.char[aif.SP][aif.AMOUNT]
        djc.char_silver_load = self.char[aif.SP][aif.LOAD]

        djc.char_copper_amount = self.char[aif.CP][aif.AMOUNT]
        djc.char_copper_load = self.char[aif.CP][aif.LOAD]

        djc.char_current_round = self.char[aif.ROUND]
        djc.char_mastered_count = self.char[aif.MASTERED]
        djc.char_game_day = self.char[aif.DATE]
        djc.char_game_time = self.char[aif.TIME]

        djc.save()

        for skill in self.char[aif.CLASS_SKILLS]:
            try:
                cs = djc.classskills_set.get(item_name=skill)
                # print(skill + " found")
            except ObjectDoesNotExist:
                cs = djc.classskills_set.create(item_name=skill)
                # print(skill + " not found")
            cs.rank = self.char[aif.CSP + skill][aif.RANK]
            cs.order = int(cs.rank / 4)
            cs.buff = self.char[aif.CSP + skill][aif.MODIFIERS]
            cs.adjusted = self.char[aif.CSP + skill][aif.ADJ]
            cs.mastered = self.char[aif.CSP + skill][aif.MASTERED]
            cs.description = self.char[aif.CSP + skill][aif.DESC]
            cs.save()

        for skill in self.char[aif.RACIAL_SKILLS]:
            try:
                rs = djc.racialskills_set.get(item_name=skill)
                # print(skill + " found")
            except ObjectDoesNotExist:
                rs = djc.racialskills_set.create(item_name=skill)
                # print(skill + " not found")
            rs.rank = self.char[aif.RSP + skill][aif.RANK]
            rs.order = int(cs.rank / 4)
            rs.buff = self.char[aif.RSP + skill][aif.MODIFIERS]
            rs.adjusted = self.char[aif.RSP + skill][aif.ADJ]
            rs.mastered = self.char[aif.RSP + skill][aif.MASTERED]
            rs.description = self.char[aif.RSP + skill][aif.DESC]
            rs.save()

        if self.char[aif.HONOR_SKILLS]:
            for skill in self.char[aif.HONOR_SKILLS]:
                try:
                    hs = djc.honorskills_set.get(item_name=skill)
                    # print(skill + " found")
                except ObjectDoesNotExist:
                    hs = djc.honorskills_set.create(item_name=skill)
                    # print(skill + " not found")
                hs.rank = self.char[aif.HSP + skill][aif.RANK]
                hs.order = int(cs.rank / 4)
                hs.buff = self.char[aif.HSP + skill][aif.MODIFIERS]
                hs.adjusted = self.char[aif.HSP + skill][aif.ADJ]
                hs.mastered = self.char[aif.HSP + skill][aif.MASTERED]
                hs.description = self.char[aif.HSP + skill][aif.DESC]
                hs.save()

        for weapon in self.char[aif.WEAPONS_LIST]:
            try:
                w = djc.weapons_set.get(item_name=weapon)
                # print(weapon + " found")
            except ObjectDoesNotExist:
                w = djc.weapons_set.create(item_name=weapon)
                # print(weapon + " not found")

            w.size = self.char[aif.WSP + weapon][aif.SIZE]
            w.type = self.char[aif.WSP + weapon][aif.TYPE]
            w.damage = self.char[aif.WSP + weapon][aif.DAMAGE]
            w.range = self.char[aif.WSP + weapon][aif.RANGE]
            w.durability = self.char[aif.WSP + weapon][aif.DURABILITY]
            w.load = self.char[aif.WSP + weapon][aif.LOAD]
            w.rank = self.char[aif.WSP + weapon][aif.RANK]
            w.order = int(w.rank / 4)
            w.mastered = self.char[aif.WSP + weapon][aif.MASTERED]
            w.save()

        for armor in self.char[aif.ARMOR_LIST]:
            try:
                a = djc.armor_set.get(item_name=armor)
                # print(armor + " found")
            except ObjectDoesNotExist:
                a = djc.armor_set.create(item_name=armor)
                # print(armor + " not found")

            a.type = self.char[aif.ASP + armor][aif.TYPE]
            a.durability = self.char[aif.ASP + armor][aif.DURABILITY]
            a.slashing = self.char[aif.ASP + armor][aif.SLASHING]
            a.piercing = self.char[aif.ASP + armor][aif.PIERCING]
            a.bludgeoning = self.char[aif.ASP + armor][aif.BLUDGEONING]
            a.cleaving = self.char[aif.ASP + armor][aif.CLEAVING]
            a.load = self.char[aif.ASP + armor][aif.LOAD]
            if a.item_name != "Protection Spell":
                a.rank = self.char[aif.ASP + armor][aif.RANK]
                a.order = int(a.rank / 4)
            a.mastered = self.char[aif.ASP + armor][aif.MASTERED]
            a.save()

        djc.save()
        '''
