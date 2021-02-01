# Races
HUMAN = "Human"
DWARF = "Dwarf"
ELF = "Elf"
HALFLING = "Halfling"
GNOME = "Gnome"
HALF_ELF = "Half Elf"
YAWP = "Yawp"
FAERIE_FLARE = "Faerie Flare"


# Classes
BARD = "Bard"
DRUID = "Druid"
MAGICIAN = "Magician"
WITCH = "Witch"
PRIEST = "Priest"
WIZARD = "Wizard" 
PROPHET = "Prophet"
TEMPLAR = "Templar"
THEURGIST = "Theurgist"
CHARLATAN = "Charlatan"
WARLOCK = "Warlock"
MONK = "Monk"
GYPSY = "Gypsy"
DIVINER = "Diviner"
SCOUT = "Scout"
PARAGON = "Paragon"
ROGUE = "Rogue"
WARRIOR = "Warrior"
BUCCANEER = "Buccaneer"
BARBARIAN = "Barbarian"
PALADIN = "Paladin"
RANGER = "Ranger"
ILLUSIONIST = "Illusionist"
class_list = [BARBARIAN, BARD, BUCCANEER, CHARLATAN, DIVINER, DRUID, GYPSY,
              ILLUSIONIST, MAGICIAN, MONK, PALADIN, PARAGON, PRIEST, PROPHET, RANGER,
              ROGUE, SCOUT, THEURGIST, TEMPLAR, WARLOCK, WARRIOR, WITCH, WIZARD]

spell_casters = [BARD, CHARLATAN, DIVINER, DRUID, GYPSY, ILLUSIONIST, MAGICIAN, MONK, PARAGON, PRIEST,
                    PROPHET, SCOUT, THEURGIST, TEMPLAR, WARLOCK, WITCH, WIZARD]
wizards = [WIZARD, CHARLATAN, DIVINER, GYPSY, PARAGON, SCOUT, THEURGIST, WARLOCK]
priests = [PRIEST, DIVINER, GYPSY,  MONK, PARAGON, PROPHET, TEMPLAR, THEURGIST]


# Miscellaneous
DATE = "Date"
TIME = "Time"
OPEN = "Open"
ROOT = "Root"
TITLE = "Title"
DICT = "Dict"

# Character Info
NAME = "Name"
RACE = "Race"
CLASS = "Class"
NOTES = "Notes"
MALE = "Male"
FEMALE = "Female"
ARMOR = "Armor"
WEAPON = "Weapon"
SPELL = "Spell"
HONOR = "Honor"
RACIAL = "Racial"

# Character Attribute
GENDER = "Gender"
AGE = "Age"
HEIGHT = "Height"
WEIGHT = "Weight"

# Movement
MOVEMENT = "Movement"
BASE = "Base"
ADJ = "Adj"
WALKING = "Walking"
RUNNING = "Running"
SWIMMING = "Swimming"

# Encumbrance
ENCUMBRANCE = "Encumbrance"
TOTAL_LOAD = "Total Load"
MODIFIERS = "Modifiers"
BURDENED = "Burdened"

# Experience
LEVEL = "Level"
EXPERIENCE = "Experience"
NEXT_LEVEL = "Next Level"

# Character Stats
ABILITY_SCORES = "Ability Scores"
STR = "STR"
DEX = "DEX"
INT = "INT"
HLTH = "HLTH"
BUFF = "Buff"
EFFECTIVE = "Effective"
CURRENT = "Current"
DURATION = "Duration"

# Character Saves
DICE = "Dice"
SAVES = "Saves"
WITHSTAND = "Withstand"
DODGE = "Dodge"
RESIST = "Resist"
HONOR_POINTS = "Honor Pts"
SPELL_POINTS = "Spell Points"
SPELL_EFF_MOD = "Spell Effectiveness Modifiers"

# Combat Factors
COMBAT_FACTORS = "Combat Factors"
KNOCKDOWN = "Knockdown"
DEFENSE = "Defense"
STUN = "Stun"
ENDURANCE = "Endurance"
FATIGUE = "Fatigue"
EXTRA_FATIGUE = "Extra Fatigue"
CF_ADJ = "CF Adj"

# Bonuses
BONUSES = "Bonuses"
TO_HIT = "To Hit"
DAMAGE = "Damage"
ACTIONS = "Actions"
OUTSIDE = "Outside"
UNDERGROUND = "Underground"

# Skills [NAME, RANK, ORDER]
CLASS_SKILLS = "Class Skills"
RACIAL_SKILLS = "Racial Skills"
HONOR_SKILLS = "Honor Skills"
CSP = "CS_"
RSP = "RS_"
HSP = "HS_"
RANK = "Rnk"
ORDER = "Ord"
MASTERED = "Mastered"
DESC = "Description"
TIPS = "Tips"
USED = "Times Used"
LIMIT = "Use Per Day Limit"
skills_dict = {RANK: 0, MASTERED: False, MODIFIERS: 0, ADJ: 0, DESC: "", USED: 0, LIMIT: 0}
skills_dict = {RANK: 0, MASTERED: False, MODIFIERS: 0, ADJ: 0, DESC: "", USED: 0, LIMIT: 0}

# Weapons [SIZE, TYPE, DAMAGE, RANGE, DURABILITY, LOAD, RANK, ORDER]
DICE_ADJ = "Dice and Adj"
GROUP = "Group"
WEAPONS_LIST = "Weapons List"
WSP = "Weapon_"
SIZE = "Size"
TYPE = "Type"
RANGE = "Range"
DURABILITY = "Dur"
LOAD = "Load"
SLASHING_GRP = "Slashing Group"
PIERCING_GRP = "Piercing Group"
BLUDGEONING_GRP = "Bludgeoning Group"
CLEAVING_GRP = "Cleaving Group"
THROWING_GRP = "Throwing Group"
BOW_GRP = "Bow Group"
MELEE = "Melee"
MISSILE = "Missile"
TOTAL_WLOAD = "Total Weapons Load"
weapons_dict = {SIZE: "", TYPE: "", DAMAGE: "", RANGE: "", DURABILITY: "", LOAD: 0, RANK: 0, MASTERED: False}

# Armor [TYPE, DURABILITY, SLASHING, PIERCING, BLUDGEONING, CLEAVING, LOAD, RANK, ORDER]
ARMOR_LIST = "Armor List"
ASP = "Armor_"
SLASHING = "S"
PIERCING = "P"
BLUDGEONING = "B"
CLEAVING = "C"
LIGHT_GRP = "Light Armor Group"
MEDIUM_GRP = "Medium Armor Group"
HEAVY_GRP = "Heavy Armor Group"
HELMET_GRP = "Helmet Group"
UNARMED_GRP = "Unarmed Group"
SHIELD_GRP = "Shield Group"
TOTAL_ALOAD = "Total Armor Load"
SPBC_BUFF = "SPBC"
TOTAL_SPBC = "Total SPBC"
TOTAL = "Total"
armor_dict = {TYPE: "", DURABILITY: "", SLASHING: 0, PIERCING: 0, BLUDGEONING: 0, CLEAVING: 0, LOAD: 0, RANK: 0,
              MASTERED: False}

# Money [GOLD_PIECES, SILVER_PIECES, COPPER_PIECES, OTHER]
CURRENCY = "Currency"
MSP = "Currency_"
GOLD_PIECES = "Gold Pieces"
SILVER_PIECES = "Silver Pieces"
COPPER_PIECES = "Copper Pieces"
OTHER = "Other"
GP = "GP"
SP = "SP"
CP = "CP"
AMOUNT = "Amount"

# Equipment [QUANTITY, LOAD, ADJ, DURABILITY]
QUANTITY = "Qty"
CONTAINER_LIST = "Containers"
WORN = "Worn"
IN_CONTAINER = "In Container"
CONTAINER_1 = "Container 1"
CONTAINER_2 = "Container 2"
CONTAINER_3 = "Container 3"
CONTAINER_4 = "Container 4"
C1P = "C1_"
C2P = "C2_"
C3P = "C3_"
C4P = "C4_"
equipment_dict = {QUANTITY: 1, LOAD: 0.1, ADJ: "", DURABILITY: 0, WORN: False}

# Combat Stuff
ROUND = "Round"
BUFFS = "Buffs"
BUFFS_LIST = "Buffs List"
START = "Start"
END = "End"
FIELD = "Field"
METHOD = "Method"
DEF_BUFF = "Default Buff"
AVL_BUFFS = "Available Buffs"
EFFECTS = "Effects"
BSP = "Buff_"
IN_GRID = "In Grid"
ROW = "Row"
buffs_dict = {METHOD: "", START: 0, DURATION: 0, EFFECTS: {FIELD: "", BUFF: ""}, IN_GRID: "", ROW: 0}

character_attributes = [GENDER, AGE, HEIGHT, WEIGHT]

movements = [MOVEMENT, WALKING, RUNNING, SWIMMING]

encumbrances = [ENCUMBRANCE, TOTAL_LOAD, MODIFIERS, BURDENED]

experiences = [LEVEL, EXPERIENCE, NEXT_LEVEL]

abilities = [STR, DEX, INT, HLTH]

saves = [WITHSTAND, DODGE, RESIST]

combat_factors = [KNOCKDOWN, DEFENSE, STUN, ENDURANCE]

bonuses = [TO_HIT, DAMAGE, ACTIONS]

searches = [OUTSIDE, UNDERGROUND]

currency = [GP, SP, CP, OTHER]

money = [AMOUNT, LOAD]

equipment = [QUANTITY, LOAD, ADJ, DURABILITY, TOTAL_LOAD]

containers = [CONTAINER_1, CONTAINER_2, CONTAINER_3, CONTAINER_4]

weapons = [WEAPONS_LIST, DICE_ADJ, SIZE, TYPE, DAMAGE, RANGE, DURABILITY, LOAD, RANK, ORDER, TOTAL_WLOAD, TO_HIT]

armor = [ARMOR_LIST, TYPE, DURABILITY, SLASHING, PIERCING, BLUDGEONING, CLEAVING, LOAD, RANK, ORDER, TOTAL_ALOAD]

skills = [CLASS_SKILLS, RACIAL_SKILLS, HONOR_SKILLS, RANK, ORDER]
