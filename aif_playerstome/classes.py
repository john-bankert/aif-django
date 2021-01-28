from aif import constants as aif

max_length = 100

class Classes:

    def __init__(self, *args, **kwargs):
        self._skills_list = {"Priest": ["Commune", "Holiness", "Holy Touch", "Relics", "Religion", "Salves", "Subdue"],
                             "Rogue": ["Acrobatics", "Backstab", "Climb", "Decipher Codes", "Listen", "Locks",
                                       "Pick Pockets", "Precision", "Skulk", "Traps"],
                             "Warrior": ["Armorer", "Awareness", "Balance", "Block", "Disarm", "Melee", "Missile",
                                         "Mounted Battle", "Scrapping", "Stamina", "Weaponsmith"],
                             "Wizard": ["Accuracy", "Brew", "Diminish", "Focus", "Item", "Lore", "Scribe"],
                             "Barbarian": ["Evasion", "Constitution", "Cunning", "Diehard", "Ferocity", "Liveliness",
                                           "Savagery", "Sense Occult", "Sleep Tolerance", "Tenacity", "Vital Force"],
                             "Bard": ["Arcana", "Charisma", "Combat Logistics", "Crescendo", "Dance Fighting", "Feing",
                                      "Finesse", "General Inspection", "Herbalism", "Instruments", "Juggling",
                                      "Power of Observation", "Tap", "Twiddle", "Twisting"],
                             "Buccaneer": ["Bravado", "Cutthroat", "Deep Breath", "Fortuity", "Rope Work", "Roving",
                                           "Sailing", "Sea Legs", "Sea Lore", "Sword Play", "Water Sense"],
                             "Druid": ["Dayglow", "Imbue", "Leap", "Moonglow", "Poultices", "Renewing Touch", "Smell",
                                       "Walkabout"],
                             "Magician": ["Alchemy", "Conflux", "Derivation", "Harness", "Legerdemain", "Mathematics",
                                          "Science"],
                             "Paladin": ["Avenging Smite", "Guard", "Lay on Hands", "Radiant Shield", "Righteous Faith",
                                         "Stalwart Stance", "Valiant Aura"],
                             "Ranger": ["Agility", "Ambush", "Booby Trap", "Disengage", "First Blood", "Marksmanship",
                                        "Medic", "Nature Craft", "Pathfinding", "Reconnoiter", "Split Shot",
                                        "Tame", "Vigilance"],
                             "Witch": ["Concot", "Drain Life", "Familiar", "Harvest", "Hex", "Trance", "Transference",
                                       "Trinketry", "Void Walk"],
                             "Illusionist": ["Concealed Carry", "Dupery", "Feign Death", "Imprint", "Sense Intention", 
                                                "Shuffle", "Sleight of Hand", "Theatrics", "Vanish", "Ventriloquism"],
                             "Prophet": "Priest/Rogue",
                             "Templar": "Priest/Warrior",
                             "Theurgist": "Priest/Wizard",
                             "Swashbuckler": "Rogue/Warrior",
                             "Charlatan": "Rogue/Wizard",
                             "Warlock": "Warrior/Wizard",
                             "Monk": "Priest/Rogue/Warrior",
                             "Gypsy": "Priest/Rogue/Wizard",
                             "Diviner": "Priest/Warrior/Wizard",
                             "Scout": "Rogue/Warrior/Wizard",
                             "Paragon": "Priest/Rogue/Warrior/Wizard"}
                                
        self._skills_buff_list = {"Paladin": ["classes.Paladin.Increase Strength",
                                              "classes.Paladin.Increase Dexterity",
                                              "classes.Paladin.Increase Intelligence",
                                              "classes.Paladin.Increase Health",
                                              "classes.Paladin.Increase Movement",
                                              "classes.Paladin.Increase Knockdown",
                                              "classes.Paladin.Increase Defense",
                                              "classes.Paladin.Increase Stun",
                                              "classes.Paladin.Increase Endurance",
                                              "classes.Paladin.Recover Health",
                                              "classes.Paladin.Recover Stun",
                                              "classes.Paladin.Recover Fatigue"]}

        class_name = self.__class__.__name__
        self.honor_skills_list = []
        self.spell_skills_list = []
        self.buffs_list = []

        # if class name is Classes don't do this. Only do it for sub classes
        if not class_name == "Classes":
            _class_name = class_name
            if args:
                if args[0] == 'multiclass':
                    _class_name = self._skills_list[class_name]

            self.skills_list = self.get_skills_list(_class_name)
            # self.honor_skills_list = []
            if class_name in self._skills_buff_list:
                self.buffs_list = self._skills_buff_list[class_name]
            if class_name == "Paladin":
                self.honor_skills_list = ["Increase Strength", "Increase Dexterity", "Increase Intelligence",
                                          "Increase Health", "Increase Movement", "Increase Knockdown",
                                          "Increase Defense", "Increase Stun", "Increase Endurance",
                                          "Recover Health", "Recover Stun", "Recover Fatigue"]
            if aif.ILLUSIONIST in class_name or aif.BARD in class_name or self.is_spellcaster():
                self.spell_skills_list = ["Circle 1 Spell Group", "Circle 2 Spell Group", "Circle 3 Spell Group",
                                          "Circle 4 Spell Group", "Circle 5 Spell Group", "Circle 6 Spell Group"]
                if aif.ILLUSIONIST in class_name:
                    self.spell_skills_list.extend(["Circle 1 Affinity", "Circle 2 Affinity", "Circle 3 Affinity",
                                                    "Circle 4 Affinity", "Circle 5 Affinity", "Circle 6 Affinity"])

    def is_spellcaster(self, cn=""):
        if cn == "":
            cn = self.__class__.__name__
        is_sc = cn in aif.spell_casters
        if "/" in cn:
            for _cn in cn.split("/"):
                if _cn in aif.spell_casters:
                    is_sc = True
                    break
        return is_sc

    def apply_skills(self, char):
        for skill in char[aif.CLASS_SKILLS]:
            try:
                method = getattr(self, skill.replace(" ", "_").lower())
                method(char)
            except AttributeError:
                pass  # swallow the error

    def get_skills_list(self, class_name=""):
        if class_name == "":
            class_name = self.__class__.__name__
        class_name = self.validate_class_name(class_name)
        class_list = [class_name]
        if "/" in class_name:
            class_list = class_name.split("/")

        skills_list = []
        for key in class_list:
            skill_list = self._skills_list[key]
            skills_list.extend(skill_list)
        return sorted(skills_list)

    def validate_class_name(self, class_name):
        class_names = [class_name]
        splitters = [" ", "/", "+", "-"]
        for splitter in splitters:
            items = []
            for str_1 in class_names:
                splits = str_1.split(splitter)
                for str_2 in splits:
                    items.append(str_2)
            class_names.clear()
            for item in items:
                class_names.append(item)

        rv = ""
        for string in class_names:
            string = string.capitalize()
            if string in self._skills_list:
                if string not in rv:
                    rv += "/" if len(rv) > 0 else ""
                    rv += string
        return rv

    def get_class_name(self):
        return self.class_name
        
    @staticmethod
    def update_args(args, param):
        t_args = tuple()
        if args:
            _args = list(args)
            if args[0] == 'multiclass':
                _args.append(param)
            t_args = tuple(_args)
        return t_args


class Priest(Classes):
    def __init__(self, *args, **kwargs):
        t_args = Classes.update_args(args, 'Priest')
        super(Priest, self).__init__(*t_args, **kwargs)


class Rogue(Classes):
    def __init__(self, *args, **kwargs):
        t_args = Classes.update_args(args, 'Rogue')
        super(Rogue, self).__init__(*t_args, **kwargs)


class Warrior(Classes):
    def __init__(self, *args, **kwargs):
        t_args = Classes.update_args(args, 'Warrior')
        super(Warrior, self).__init__(*t_args, **kwargs)


class Wizard(Classes):
    def __init__(self, *args, **kwargs):
        t_args = Classes.update_args(args, 'Wizard')
        super(Wizard, self).__init__(*t_args, **kwargs)


class Barbarian(Classes):
    def __init__(self, *args, **kwargs):
        super(Barbarian, self).__init__(*args, **kwargs)


class Bard(Classes):
    def __init__(self, *args, **kwargs):
        super(Bard, self).__init__(*args, **kwargs)


class Buccaneer(Classes):
    def __init__(self, *args, **kwargs):
        super(Buccaneer, self).__init__(*args, **kwargs)


class Druid(Classes):
    def __init__(self, *args, **kwargs):
        super(Druid, self).__init__(*args, **kwargs)


class Illusionist(Classes):
    def __init__(self, *args, **kwargs):
        super(Illusionist, self).__init__(*args, **kwargs)


class Magician(Classes):
    def __init__(self, *args, **kwargs):
        super(Magician, self).__init__(*args, **kwargs)


class Paladin(Classes):
    def __init__(self, *args, **kwargs):
        super(Paladin, self).__init__(*args, **kwargs)


class Ranger(Classes):
    def __init__(self, *args, **kwargs):
        super(Ranger, self).__init__(*args, **kwargs)


class Witch(Classes):
    def __init__(self, *args, **kwargs):
        super(Witch, self).__init__(*args, **kwargs)


class Prophet(Priest, Rogue):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Prophet, self).__init__('multiclass')


class Templar(Priest, Warrior):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Templar, self).__init__('multiclass')


class Theurgist(Priest, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Theurgist, self).__init__('multiclass')


class Swashbuckler(Rogue, Warrior):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Swashbuckler, self).__init__('multiclass')


class Charlatan(Rogue, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Charlatan, self).__init__('multiclass')


class Warlock(Warrior, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Warlock, self).__init__('multiclass')


class Monk(Priest, Rogue, Warrior):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Monk, self).__init__('multiclass')


class Gypsy(Priest, Rogue, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Gypsy, self).__init__('multiclass')


class Diviner(Priest, Warrior, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Diviner, self).__init__('multiclass')


class Scout(Rogue, Warrior, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Scout, self).__init__('multiclass')


class Paragon(Priest, Rogue, Warrior, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Paragon, self).__init__('multiclass')
