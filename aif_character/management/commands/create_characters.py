from django.core.management.base import BaseCommand, CommandError
from aif_character.models import Character
from aif_playerstome.models import ArmorCatalog, SkillsList, WeaponsCatalog


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
        WeaponsCatalog.add_to_character(char, 'War Hammer')
        ArmorCatalog.add_to_character(char, 'helmet', 'Leather', 'Leather Helmet')
        ArmorCatalog.add_to_character(char, 'shield', 'Buckler')
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
        WeaponsCatalog.add_to_character(char, 'Ironshod Staff (a)')
        ArmorCatalog.add_to_character(char, 'armor', 'Wool Robe')
        ArmorCatalog.add_to_character(char, 'helmet', 'Wizard Hat')
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
        WeaponsCatalog.add_to_character(char, 'Maul')
        ArmorCatalog.add_to_character(char, 'armor', 'Full plate', 'Full Plate')
        ArmorCatalog.add_to_character(char, 'shield', 'Buckler')
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
        _user = 'john'
        _name = 'Florian'
        if Character.objects.filter(name=_name).count() != 0:
            self.stdout.write("Deleting Character " + _name)
            c = Character.objects.get(name=_name)
            c.delete()

        self.stdout.write("Creating Character " + _name)
        char = Character()
        char.new(_name, 'Elf', 'Male', 'Charlatan', 10, 15, 18, 15)
        char.player = _user
        char.open = True
        char.add_buff('Boon', 1, 5, '+1 to hit')
        char.age = 117
        char.spell_points_base = 4
        char.spell_points_current = char.spell_points_base
        char.height = "6' 1\""
        char.weight = "120 lb"
        char.silver_amount = 132
        char.copper_amount = 12
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
        WeaponsCatalog.add_to_character(char, 'Ironshod Staff (a)')
        ArmorCatalog.add_to_character(char, 'armor', 'Wool Robe')
        ArmorCatalog.add_to_character(char, 'helmet', 'Wizard Hat')
        char.adjust()
        char.save()

        _name = 'Pindar'
        if Character.objects.filter(name=_name).count() != 0:
            self.stdout.write("Deleting Character " + _name)
            c = Character.objects.get(name=_name)
            c.delete()

        self.stdout.write("Creating Character " + _name)
        char = Character()
        char.new(_name, 'Gnome', 'Male', 'Illusionist', 12, 14, 16, 14)
        char.player = _user
        char.open = True
        char.age = 52
        char.height = "3' 11\""
        char.weight = "68 lb"
        char.silver_amount = 140
        char.copper_amount = 20
        char.spell_cards_current = 3
        char.spell_cards_base = 3

        SkillsList.add_to_character(char, 'Concealed Carry', 'Class', 1)
        SkillsList.add_to_character(char, 'Imprint', 'Class', 1)
        SkillsList.add_to_character(char, 'Shuffle', 'Class', 1)
        SkillsList.add_to_character(char, 'Sleight of Hand', 'Class', 1)
        SkillsList.add_to_character(char, 'Vanish', 'Class', 1)
        SkillsList.add_to_character(char, 'Jewel Crafting', 'Racial', 1)
        SkillsList.add_to_character(char, 'Petriform', 'Racial', 1)
        SkillsList.add_to_character(char, 'Circle 1 Affinity', 'Spell', 2)
        SkillsList.add_to_character(char, 'Circle 1 Spell Group', 'Spell', 1)
        SkillsList.add_to_character(char, 'Circle 2 Affinity', 'Spell', 2)
        SkillsList.add_to_character(char, 'Short Sword', 'Weapon', 1)
        SkillsList.add_to_character(char, 'Unarmed Group', 'Armor', 1)
        SkillsList.add_to_character(char, 'Wool Robe', 'Armor', 1)
        # WeaponsCatalog.add_to_character(char, 'Short Sword')
        WeaponsCatalog.add_to_character(char, 'Dagger')
        ArmorCatalog.add_to_character(char, 'armor', 'Wool Robe')
        ArmorCatalog.add_to_character(char, 'helmet', 'Wizard Hat')
        char.add_container('Worn')
        char.add_equipment('Worn', 'Belt', 1, 10/1, 60, True, True)
        char.add_equipment('Worn', 'Pants', 1, 1, 40, True, True)
        char.add_equipment('Worn', 'Boots', 1, 1, 30, True, True)
        char.add_equipment('Worn', 'Gloves', 1, 10/1, 40, True, True)
        char.add_equipment('Worn', 'Cloak', 1, 1, 30, True, True)
        char.add_equipment('Worn', 'Waterskin', 1, 2/1, 30, True)
        char.add_container('Small Belt Pouch')
        char.add_equipment('Small Belt Pouch', 'Spell Cards', 9, 10/1, '-', True)
        char.adjust()
        char.save()

        _name = 'Torburn'
        if Character.objects.filter(name=_name).count() != 0:
            self.stdout.write("Deleting Character " + _name)
            c = Character.objects.get(name=_name)
            c.delete()

        self.stdout.write("Creating Character " + _name)
        char = Character()
        char.new(_name, 'Dwarf', 'Male', 'Paladin/Warrior', 18, 17, 11, 14)
        char.player = _user
        char.open = True
        char.health_base = 57
        char.health_current = 57
        char.age = 42
        char.height = "4' 1\""
        char.weight = "140 lb"
        char.experience = 624
        char.gold_amount = 2
        char.silver_amount = 64
        char.copper_amount = 26

        SkillsList.add_to_character(char, 'Armorer', 'Class', 7)
        SkillsList.add_to_character(char, 'Avenging Smite', 'Class', 2)
        SkillsList.add_to_character(char, 'Awareness', 'Class', 3)
        SkillsList.add_to_character(char, 'Balance', 'Class', 4)
        SkillsList.add_to_character(char, 'Block', 'Class', 2)
        SkillsList.add_to_character(char, 'Disarm', 'Class', 2)
        SkillsList.add_to_character(char, 'Guard', 'Class', 2)
        SkillsList.add_to_character(char, 'Lay on Hands', 'Class', 6)
        SkillsList.add_to_character(char, 'Melee', 'Class', 6)
        SkillsList.add_to_character(char, 'Missile', 'Class', 6)
        SkillsList.add_to_character(char, 'Mounted Battle', 'Class', 2)
        SkillsList.add_to_character(char, 'Radiant Shield', 'Class', 3)
        SkillsList.add_to_character(char, 'Righteous Faith', 'Class', 5)
        SkillsList.add_to_character(char, 'Scrapping', 'Class', 5)
        SkillsList.add_to_character(char, 'Stalwart Stance', 'Class', 5)
        SkillsList.add_to_character(char, 'Stamina', 'Class', 5)
        SkillsList.add_to_character(char, 'Valiant Aura', 'Class', 5, False, 4)
        SkillsList.add_to_character(char, 'Weaponsmith', 'Class', 7)
        SkillsList.add_to_character(char, 'Direction Sense', 'Racial', 3)
        SkillsList.add_to_character(char, 'Dwarven History', 'Racial', 5)
        SkillsList.add_to_character(char, 'Infravision', 'Racial', 2)
        SkillsList.add_to_character(char, 'Mountaineering', 'Racial', 5)
        SkillsList.add_to_character(char, 'Stone Speak', 'Racial', 2)
        SkillsList.add_to_character(char, 'Toughness', 'Racial', 9, True, 5)
        SkillsList.add_to_character(char, 'Yawp', 'Racial', 9, True, 4)
        SkillsList.add_to_character(char, 'Increase Strength', 'Honor', 6)
        SkillsList.add_to_character(char, 'Increase Dexterity', 'Honor', 6)
        SkillsList.add_to_character(char, 'Increase Intelligence', 'Honor', 2)
        SkillsList.add_to_character(char, 'Increase Health', 'Honor', 2)
        SkillsList.add_to_character(char, 'Increase Knockdown', 'Honor', 2)
        SkillsList.add_to_character(char, 'Increase Defense', 'Honor', 5)
        SkillsList.add_to_character(char, 'Increase Stun', 'Honor', 2)
        SkillsList.add_to_character(char, 'Increase Endurance', 'Honor', 2)
        SkillsList.add_to_character(char, 'Recover Health', 'Honor', 6)
        SkillsList.add_to_character(char, 'Recover Stun', 'Honor', 6)
        SkillsList.add_to_character(char, 'Recover Fatigue', 'Honor', 6)
        SkillsList.add_to_character(char, 'Slashing Group', 'Weapon', 2)
        SkillsList.add_to_character(char, 'Piercing Group', 'Weapon', 8)
        SkillsList.add_to_character(char, 'Bludgeoning Group', 'Weapon', 6)
        SkillsList.add_to_character(char, 'Cleaving Group', 'Weapon', 2)
        SkillsList.add_to_character(char, 'Bow Group', 'Weapon', 5)
        SkillsList.add_to_character(char, 'Maul', 'Weapon', 5)
        SkillsList.add_to_character(char, 'Hand Axe', 'Weapon', 3)
        SkillsList.add_to_character(char, 'Pike', 'Weapon', 8)
        SkillsList.add_to_character(char, 'Medium Crossbow', 'Weapon', 8)
        SkillsList.add_to_character(char, 'Light Armor Group', 'Armor', 2)
        SkillsList.add_to_character(char, 'Medium Armor Group', 'Armor', 2)
        SkillsList.add_to_character(char, 'Heavy Armor Group', 'Armor', 8)
        SkillsList.add_to_character(char, 'Helmet Group', 'Armor', 6)
        SkillsList.add_to_character(char, 'Unarmed Group', 'Armor', 2)
        SkillsList.add_to_character(char, 'Shield Group', 'Armor', 5)
        SkillsList.add_to_character(char, 'Studded Leather', 'Armor', 2)
        SkillsList.add_to_character(char, 'Open-faced', 'Armor', 5)
        SkillsList.add_to_character(char, 'Plate mail', 'Armor', 8)
        SkillsList.add_to_character(char, 'Buckler', 'Armor', 5)
        WeaponsCatalog.add_to_character(char, 'Pike', 'Pike +2, Yawp +4, Monster Hatred vs. Ogres')
        WeaponsCatalog.add_to_character(char, 'Medium Crossbow', 'Medium Crossbow +3, Toughness + 5')
        w = char.weapons_set.get(name='Medium Crossbow')
        w.damage = "2d6"
        w.type = 'P'
        w.size = 'M'
        w.load = '3'
        w.range = '135'
        w.is_missile = True
        w.durability = '30'
        w.save()
        ArmorCatalog.add_to_character(char, 'armor', 'Plate mail',
                                      'Plate Mail +1/1/1/1, +2 block, +2 disarm, +1 defense')
        ArmorCatalog.add_to_character(char, 'helmet', 'Open-faced', 'Open Faced Helmet')
        ArmorCatalog.add_to_character(char, 'shield', 'Buckler')
        char.add_container('Worn')
        char.add_equipment('Worn', 'Belt', 1, 10/1, 60, True, True)
        char.add_equipment('Worn', 'Pants', 1, 1, 40, True, True)
        char.add_equipment('Worn', 'Boots', 1, 1, 30, True, True)
        char.add_equipment('Worn', 'Gloves', 1, 10/1, 40, True, True)
        char.add_equipment('Worn', 'Cloak', 1, 1, 30, True, True)
        char.add_equipment('Worn', 'Waterskin', 1, 2/1, 30, True)
        char.add_equipment('Worn', 'Blue Topaz Pendant health +13', 1, 1, 30, True)
        char.add_container('Backpack', 'Backpack +4 Valiant Aura')
        char.add_equipment('Backpack', '1 week Rations', 2, 2, '-', True)
        char.add_equipment('Backpack', 'Bedroll', 1, 3, 50, True)
        char.add_equipment('Backpack', 'Flint & Tinder', 1, 10/1, 40, True)
        char.add_equipment('Backpack', 'Magic Light Stick', 1, 1, '-', True)
        char.add_equipment('Backpack', 'Crafting Kit', 1, 2, 30, True)
        char.add_equipment('Backpack', 'Salve of Regeneration', 1, 1, '-', True)
        char.add_container('Bolt Case 1', '', 1)
        char.add_equipment('Bolt Case 1', 'Medium Quarrel', 10, 10/1, 30, True)
        char.add_container('Bolt Case 2', '', 1)
        char.add_equipment('Bolt Case 2', 'Medium Quarrel', 7, 10/1, 30, True)
        char.add_container('Storage Locker', "", 20)
        char.add_equipment('Storage Locker', 'Maul +3', 1, 7, 180, True)
        char.add_equipment('Storage Locker', 'Crafting Kit', 4, 2, 30, True)
        char.add_equipment('Storage Locker', 'Enchanting Kit', 4, 2, 30, True)
        char.add_static_buff('Blue Topaz Pendant', 'Equipment', 'Health', 'Stat', 13)
        char.add_static_buff('Pike', 'Weapon', 'To Hit', 'Attack', 2)
        char.add_static_buff('Pike', 'Weapon', 'Yawp', 'Skill', 4)
        char.add_static_buff('Backpack', 'Equipment', 'Valiant Aura', 'Skill', 4)
        char.add_static_buff('Medium Crossbow', 'Weapon', 'To Hit', 'Attack', 3)
        char.add_static_buff('Medium Crossbow', 'Weapon', 'Toughness', 'Skill', 5)
        char.add_static_buff('Plate Mail', 'Armor', 'Slashing', 'SPBC', 1)
        char.add_static_buff('Plate Mail', 'Armor', 'Piercing', 'SPBC', 1)
        char.add_static_buff('Plate Mail', 'Armor', 'Bludgeoning', 'SPBC', 1)
        char.add_static_buff('Plate Mail', 'Armor', 'Cleaving', 'SPBC', 1)
        char.add_static_buff('Plate Mail', 'Armor', 'Block', 'Skill', 2)
        char.add_static_buff('Plate Mail', 'Armor', 'Disarm', 'Skill', 2)
        char.add_static_buff('Plate Mail', 'Armor', 'Defense', 'Skill', 1)
        char.adjust()
        char.save()
