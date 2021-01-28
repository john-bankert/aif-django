import os

max_length = 100


class Spells:

    def __init__(self, *args, **kwargs):
        self._spells_list = {"Priest": {"Circle 1": ["Boon", "Darkness", "Descry Magic", "Feast", "Haven",
                                                     "Heal Wounds", "Ice Spike", "Know Intention", "Light",
                                                     "Mystic Hammer", "Push", "Solitude", "Stop", "Talk",
                                                     "Thermal Pillar", "Wind Burn"],
                                        "Circle 2": ["Calm", "Cure", "Descry Lie", "Descry Traps", "Goo", "Inventory",
                                                     "Laden", "Lift Curse", "Mystic Mace", "Mystic Shield",
                                                     "Neutralize", "Release", "Retribution", "Summon Animal", "Tremor",
                                                     "Wall of Wood"],
                                        "Circle 3": ["Assistance", "Blizzard", "Concussion", "Disrupt",
                                                     "Elemental Ward", "Galvanize Spirit", "Holy Rain", "Magic Ward",
                                                     "Mass Mend", "Mystic Sling", "Purify", "Retaliation", "Terror",
                                                     "Wall of Barbs", "Watershock", "Wings"],
                                        "Circle 4": ["Beacon", "Bola Swarm", "Circle of Warding", "Curse", "Delusion",
                                                     "Elemental Disruption", "Elemental Spray", "Healer", "Melt Rock",
                                                     "Move Water", "Pillar of Force", "Sanctify", "Truth",
                                                     "Wall of Winds", "Warding Mark", "Withstand Poison"],
                                        "Circle 5": ["Bodyguard", "Compass", "Create Lightning", "Descry Souls",
                                                     "Faith", "Holy Ground", "Holy Word", "Hush", "Missile Cube",
                                                     "Mystic Maul", "Overgrowth", "Plague", "Silver Grenade",
                                                     "Stone Death", "Vision", "Wall of Shards"],
                                        "Circle 6": ["Annihilate", "Astral Projection", "Banish", "Earthquake",
                                                     "Elemental Pillar", "Flood", "Miss", "Mystic Smite", "Netherspeak",
                                                     "Protector", "Regenerate", "Restore Life", "Shadow of Death",
                                                     "Shrine", "Travel", "Wrath"]},
                             "Wizard": {"Circle 1": ["Crushing Strike", "Darkness", "Descry Magic", "Eagle Sight",
                                                     "Flame", "Force Dagger", "Frog", "Illusion", "Light", "Mouse",
                                                     "Open", "Protection", "Sand Blast", "Shock Wave", "Slumber",
                                                     "Yell"],
                                        "Circle 2": ["Force Dart", "Force Staff", "Invigorate", "Languages", "Levitate",
                                                     "Lock", "Magnetize", "Night Vision", "Observer", "Resize",
                                                     "Roller", "Sight", "Speed", "Veil", "Water Breathing", "Whisper"],
                                        "Circle 3": ["Carrier", "Cloak", "Cocoon", "Displace Image", "Elemental Bolt",
                                                     "Flight", "Glass", "Hidden Passage", "Magic Space", "Mist",
                                                     "Second Bane", "Tentacle", "Timber Shards", "Toxin",
                                                     "Wall of Stone", "Weaken"],
                                        "Circle 4": ["Berserk", "Catch", "Climb", "Clumsy", "Elemental Sphere", "Grace",
                                                     "Magic Protection", "Mind Read", "Propel", "Suffocate", "Tornado",
                                                     "Toxic Sphere", "Transmute Being", "Trap", "Undo", "Wall of Ice"],
                                        "Circle 5": ["Bounce", "Bouncing Ball", "Crystal Ball", "Disintegrate",
                                                     "Dust Storm", "Energy of Life", "Exhaust", "Flaming Cloud",
                                                     "Flaming Star", "Force Militia", "Magic Sphere", "Mind Shield",
                                                     "Summon", "Switch", "Wall of Fire", "Wind"],
                                        "Circle 6": ["Avalanche", "Back Draft", "Change Shape", "Charm", "Duplicate",
                                                     "Elemental Protection", "Elicit Elemental", "Fortification",
                                                     "Magic Book", "Negate", "Sacrifice", "Sealing", "Steal",
                                                     "Teleport", "Walk", "Woe"]},
                             "Bard": ["Arcane Blade", "Arcane Nimbus", "Arcane Pulse", "Arcane Radiation",
                                      "Barrier Nimbus", "Beguile", "Blink", "Consider", "Copious Capacity",
                                      "Elemental Nimbus", "Extension", "Glimmer", "Incite", "Light Manipulation",
                                      "Mitigate", "Song of Grandeur", "Song of Reduction", "Sonic Blast", "Sorrow",
                                      "Soothe", "Vermin Jig", "Visualization"],
                             "Druid": {"Circle 1": ["Elemental Essence", "Dusk", "Gift of the Equinox",
                                                    "Living Daylights", "Plant Food", "Snowblind", "Speak Animal",
                                                    "Spirit of the Beast", "Thorn Spike", "Trail", "Vines"],
                                       "Circle 2": ["Animal Hide", "Claws", "Cobra Spit", "Engergize", "Fangs",
                                                    "Gift of the Eclipse", "Healing Mark", "Mana", "Squall", "Swim"
                                                                                                             "Treedance"],
                                       "Circle 3": ["Cinder Shower", "Dancing Shadows", "Elemental Hide", "Foliage",
                                                    "Gift of the Solstice", "Microburst", "Remedy", "Senses",
                                                    "Snow Ball", "Splinter Blade", "Wings of Service"],
                                       "Circle 4": ["Air Shield", "Call of the Wild", "Caustic Cloud", "Dehydrate",
                                                    "Magic Rock", "Net", "Sink Hole", "Static Shock", "Stone Hold",
                                                    "Victory Cry of the Bull Ape", "Water Walking"],
                                       "Circle 5": ["Draw", "Earth Work", "Greased Lightning", "Locust Swarm",
                                                    "Plant Haven", "Revive", "Smelt", "Treant", "Water Spout",
                                                    "Wind Jump", "Wood Statue"],
                                       "Circle 6": ["Decay", "Dry Lightning", "Elemental Nature", "Force of Nature",
                                                    "Neutral Zone", "Null Zone", "Rainbow Blast", "Spike Shower",
                                                    "Stampede", "Summon Fey", "Toxic Shock"]},
                             "Magician": {"Circle 1": ["Body Armor", "Cantrip", "Detect Magic", "Illumination",
                                                       "Power Grasp"],
                                          "Circle 2": ["Bend", "Levitation", "Object Manipulation", "Power Lance",
                                                       "Vanish"],
                                          "Circle 3": ["Conjure Power Weapon", "Equilibrium", "Fly",
                                                       "Read Impressions", "Size Alteration"],
                                          "Circle 4": ["Amphibian Nature", "Shove", "Telekinesis", "Telepathy",
                                                       "Thought Shield"],
                                          "Circle 5": ["Animal Telepathy", "Detect Life", "Dissipate Energy",
                                                       "Hypnosis", "Obliviate"],
                                          "Circle 6": ["Dominate Mind", "Madness", "Resistance", "Stop Time",
                                                       "Transport"]},
                             "Witch": {"Circle 1": ["Elemental Strike", "Knowledge", "Onslaught", "Shadow Bones",
                                                    "Shadow Mend", "Target", "Vex", "Void Cloak"],
                                       "Circle 2": ["Affliction", "Blood Blade", "Elemental Blast", "Holes",
                                                    "Shadow Denizens", "Shine", " Stretch", " Uncover"],
                                       "Circle 3": ["Elemental Blade", "Glamour", "Nether Protection", "Pain",
                                                    "Shadow Fiends", "Shadow Spike", " Stench", " Vroom"],
                                       "Circle 4": ["Cackle", "Convergence", "Fate", "Shadow Cage",
                                                    "Shadow Creatures", "Shadow Mirror", "Steel Skin",
                                                    "Wall of Bones"],
                                       "Circle 5": ["Blaze", "Explode", "Flimsy", "Magic Skulls", "Shadow Blade",
                                                    "Shadow Revenants", " Spectral Steeds", "Wall of Shade"],
                                       "Circle 6": ["Clouds", "Genocide", "Mojo", "Nightmare", "Possess",
                                                    "Scrying", "Shadow Things", "Simulacrum"]},
                             "Prophet": "Priest",
                             "Templar": "Priest",
                             "Theurgist": "Priest/Wizard",
                             "Swashbuckler": "Rogue",
                             "Charlatan": "Wizard",
                             "Warlock": "Wizard",
                             "Monk": "Priest",
                             "Gypsy": "Priest/Wizard",
                             "Diviner": "Priest/Wizard",
                             "Scout": "Wizard",
                             "Paragon": "Priest/Wizard"}

        self._spells_buff_list = ["spells.Priest.Boon", "spells.Priest.Faith", "spells.Wizard.Speed",
                                  "spells.Witch.Onslaught"]
        class_name = self.__class__.__name__

        # if class name is Spells don't do this. Only do it for sub classes
        self.spells_list = {}
        if not class_name == "Spells":
            _class_name = class_name
            if args:
                if args[0] == 'multiclass':
                    _class_name = self._spells_list[class_name]
            self.spells_list = self.get_spells_list(_class_name)

    def get_spells_list(self, class_name=""):
        if class_name == "":
            class_name = self.__class__.__name__
            
        class_list = class_name.split("/")
        spells_list = {}
        sd = []
        for key in class_list:
            sd.append(self._spells_list[key])

        for d in sd:
            for key, value in d.items():
                if key in spells_list.keys():
                    spells_list[key].append(value)
                else:
                    spells_list[key] = value
                    
        return spells_list #sorted(spells_list)

    def get_spells_buff_list(self):
        return self._spells_buff_list

    def print_spell_details(self, class_name=""):
        if class_name == "":
            class_name = self.__class__.__name__

        print("=" * max_length)
        print(" Spell Details for", class_name)
        print("")
        print(self.spells_list)
        print("")
        print("=" * max_length)
        print("")

    @staticmethod
    def update_args(args, param):
        t_args = tuple()
        if args:
            _args = list(args)
            if args[0] == 'multiclass':
                _args.append(param)
            t_args = tuple(_args)
        return t_args


class Priest(Spells):
    def __init__(self, *args, **kwargs):
        t_args = Spells.update_args(args, 'Priest')
        super(Priest, self).__init__(*t_args, **kwargs)


class Wizard(Spells):
    def __init__(self, *args, **kwargs):
        t_args = Spells.update_args(args, 'Wizard')
        super(Wizard, self).__init__(*t_args, **kwargs)


class Bard(Spells):
    def __init__(self, *args, **kwargs):
        super(Bard, self).__init__(*args, **kwargs)


class Druid(Spells):
    def __init__(self, *args, **kwargs):
        super(Druid, self).__init__(*args, **kwargs)


class Magician(Spells):
    def __init__(self, *args, **kwargs):
        super(Magician, self).__init__(*args, **kwargs)


class Witch(Spells):
    def __init__(self, *args, **kwargs):
        super(Witch, self).__init__(*args, **kwargs)


class Prophet(Priest):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Prophet, self).__init__('multiclass')


class Templar(Priest):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Templar, self).__init__('multiclass')


class Theurgist(Priest, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Theurgist, self).__init__('multiclass')


class Charlatan(Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Charlatan, self).__init__('multiclass')


class Warlock(Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Warlock, self).__init__('multiclass')


class Monk(Priest):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Monk, self).__init__('multiclass')


class Gypsy(Priest, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Gypsy, self).__init__('multiclass')


class Diviner(Priest, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Diviner, self).__init__('multiclass')


class Scout(Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Scout, self).__init__('multiclass')


class Paragon(Priest, Wizard):
    def __init__(self, *args, **kwargs):
        _args = tuple('multiclass')
        super(Paragon, self).__init__('multiclass')
        
        

'''
if __name__ == "__main__":

    spells = Spells()

    try:
        fn = os.path.dirname(os.path.realpath(__file__)) + "/data/spells.csv"
        cs = ["Priest", "Wizard", "Druid", "Magician", "Witch"]
        sep = ", "
        with open(fn, "w", newline='\n') as file:
            for c in cs:
                for circle in spells._spells_list[c]:
                    for spell in spells._spells_list[c][circle]:
                        file.write(c + sep + circle + sep + spell + sep + sep + sep + sep + sep + sep + "\n")
            for spell in spells._spells_list["Bard"]:
                file.write("Bard" + sep + sep + spell + sep + sep + sep + sep + sep + sep + "\n")
    except FileNotFoundError:
        print("file not found")
'''