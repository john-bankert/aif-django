from django.core.management.base import BaseCommand, CommandError
from aif_character.models import Character
from aif_playerstome.models import Weapons, Armor


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
        Weapons.add_to_character(char, 'small_weapons', 'War Hammer')
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
