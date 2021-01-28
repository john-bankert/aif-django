import random
from aif import constants as aif

max_length = 100
race_list = [aif.HUMAN, aif.DWARF, aif.ELF, aif.HALFLING, aif.GNOME, aif.HALF_ELF]

class Races:

    def __init__(self, *args, **kwargs):
        # self.all_racial_skill_descriptions = Fn.load_properties("resources/races.properties", "=", "#")
        pass

    @staticmethod
    def update_args(args, param):
        t_args = tuple()
        if args:
            _args = list(args)
            if args[0] == 'multiracial':
                _args.append(param)
            t_args = tuple(_args)
        return t_args
        
        
class Human(Races):
    def __init__(self, *args, **kwargs):
        t_args = Races.update_args(args, 'Human')
        super(Human, self).__init__(*t_args, **kwargs)

        self.race_name = aif.HUMAN
        self.attributes = {aif.MALE: "72,180", aif.FEMALE: "66,120", aif.AGE: 20}
        self.search_dice = {aif.OUTSIDE: 3, aif.UNDERGROUND: 3}
        self.search_bonuses = {aif.OUTSIDE: 0, aif.UNDERGROUND: 0}
        self.save_dice = {aif.DODGE: 3, aif.RESIST: 3, aif.WITHSTAND: 3}
        self.save_bonuses = {aif.DODGE: 0, aif.RESIST: 0, aif.WITHSTAND: 0}
        self.racial_d6 = [aif.STR, aif.DEX, aif.INT, aif.HLTH]
        self.load = 30
        self.movement = 32
        self.skill_points = "+3 to any"
        self.racial_skills = ["Appraising", "Bartering", "History", "Instinct", "Leadership", "Linguistics", "Wisdom"]
        self.buffs_list = []


class Dwarf(Races):
    def __init__(self, *args, **kwargs):
        super(Dwarf, self).__init__(*args, **kwargs)

        self.race_name = aif.DWARF
        self.attributes = {aif.MALE: "48,150", aif.FEMALE: "48,130", aif.AGE: 75}
        self.search_dice = {aif.OUTSIDE: 3, aif.UNDERGROUND: 4}
        self.search_bonuses = {aif.OUTSIDE: 0, aif.UNDERGROUND: 0}
        self.save_dice = {aif.DODGE: 3, aif.RESIST: 3, aif.WITHSTAND: 4}
        self.save_bonuses = {aif.DODGE: 0, aif.RESIST: 0, aif.WITHSTAND: 0}
        self.racial_d6 = [aif.STR, aif.HLTH]
        self.load = 25
        self.movement = 28
        self.skill_points = "+1 weapon, +1 armor"
        self.racial_skills = ["Direction Sense", "Dwarven History", "Infravision", "Mountaineering", "Stone Speak",
                              "Toughness", "Yawp"]
        self.buffs_list = ["races.Dwarf.Yawp"]


class Elf(Races):
    def __init__(self, *args, **kwargs):
        t_args = Races.update_args(args, 'Elf')
        super(Elf, self).__init__(*t_args, **kwargs)

        self.race_name = aif.ELF
        self.attributes = {aif.MALE: "66,110", aif.FEMALE: "60,90", aif.AGE: 110}
        self.search_dice = {aif.OUTSIDE: 4, aif.UNDERGROUND: 4}
        self.search_bonuses = {aif.OUTSIDE: 0, aif.UNDERGROUND: 0}
        self.save_dice = {aif.DODGE: 3, aif.RESIST: 4, aif.WITHSTAND: 3}
        self.save_bonuses = {aif.DODGE: 0, aif.RESIST: 0, aif.WITHSTAND: 0}
        self.racial_d6 = [aif.DEX, aif.INT]
        self.load = 20
        self.movement = 36
        self.skill_points = "+2 to class skill, spells or long/short bow"
        self.racial_skills = ["Camouflage", "Elven History", "Faerie Flare", "Nightvision", "Plant Empathy",
                              "Sense Enchantment", "Tracking"]
        self.buffs_list = ["races.Elf.Faerie Flare"]


class Halfling(Races):
    def __init__(self, *args, **kwargs):
        super(Halfling, self).__init__(*args, **kwargs)

        self.race_name = aif.HALFLING
        self.attributes = {aif.MALE: "30,60", aif.FEMALE: "30,60", aif.AGE: 25}
        self.search_dice = {aif.OUTSIDE: 4, aif.UNDERGROUND: 3}
        self.search_bonuses = {aif.OUTSIDE: 0, aif.UNDERGROUND: 0}
        self.save_dice = {aif.DODGE: 4, aif.RESIST: 3, aif.WITHSTAND: 3}
        self.save_bonuses = {aif.DODGE: 0, aif.RESIST: 0, aif.WITHSTAND: 0}
        self.racial_d6 = [aif.DEX, aif.HLTH]
        self.load = 15
        self.movement = 24
        self.skill_points = "+2 to missile weapons, class skills"
        self.racial_skills = ["Animal Friend", "Chattering", "Escaping", "Far Sight", "Halfling History", "Lock",
                              "Map Sense"]
        self.buffs_list = []


class Gnome(Races):
    def __init__(self, *args, **kwargs):
        super(Gnome, self).__init__(*args, **kwargs)

        self.race_name = aif.GNOME
        self.attributes = {aif.MALE: "42,75", aif.FEMALE: "42,75", aif.AGE: 55}
        self.search_dice = {aif.OUTSIDE: 3, aif.UNDERGROUND: 4}
        self.search_bonuses = {aif.OUTSIDE: 0, aif.UNDERGROUND: 0}
        self.save_dice = {aif.DODGE: 3, aif.RESIST: 4, aif.WITHSTAND: 3}
        self.save_bonuses = {aif.DODGE: 0, aif.RESIST: 0, aif.WITHSTAND: 0}
        self.racial_d6 = [aif.STR, aif.DEX]
        self.load = 13
        self.movement = 30
        self.skill_points = "+1 to racial skills, +1 to class skills"
        self.racial_skills = ["Earth Light", "Jewel Crafting", "Petriform", "Rockroot", "Treasure Sense",
                              "Tremor Sense", "Ultravision"]
        self.buffs_list = []


class HalfElf(Human, Elf):
    def __init__(self, *args, **kwargs):
        super(HalfElf, self).__init__(*args, **kwargs)

        self.race_name = aif.HALF_ELF
        self.attributes = {aif.MALE: "69,145", aif.FEMALE: "63,105", aif.AGE: 35}
        self.search_dice = {aif.OUTSIDE: 3, aif.UNDERGROUND: 3}
        self.search_bonuses = {aif.OUTSIDE: 2, aif.UNDERGROUND: 2}
        self.save_dice = {aif.DODGE: 3, aif.RESIST: 3, aif.WITHSTAND: 3}
        self.save_bonuses = {aif.DODGE: 0, aif.RESIST: 2, aif.WITHSTAND: 0}
        self.racial_d6 = [aif.STR, aif.DEX, aif.INT, aif.HLTH]
        self.load = 24
        self.movement = 34
        self.skill_points = "+1 to racial skills, +1 to class skills"
        if random.randint(1, 6) < 4:
            dominant_skills = Human().racial_skills
            other_skills = Elf().racial_skills
        else:
            dominant_skills = Elf().racial_skills
            other_skills = Human().racial_skills
        _racial_skills = []
        while len(_racial_skills) < 4:
            idx = random.randint(0, 6)
            if not dominant_skills[idx] in _racial_skills:
                _racial_skills.append(dominant_skills[idx])
        while len(_racial_skills) < 7:
            idx = random.randint(0, 6)
            if not other_skills[idx] in _racial_skills:
                _racial_skills.append(other_skills[idx])
        self.racial_skills = sorted(_racial_skills)
        self.buffs_list = []

