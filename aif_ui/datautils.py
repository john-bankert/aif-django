from django.contrib.auth.models import User, Group, Permission
from .models import Character, CharacterForm

def add_users():
    add_user('John', 'jbankert@gmail.com', 'k72CD@&rsa49PKF', 'John', 'Bankert')
    add_user('demo', 'demo@aif.magichelmet.xyz', '1qaz2wsx!QAZ@WSX', 'Demo', 'User')
    add_user('Gamemaster', 'gamemaster@aif.magichelmet.xyz', '1234qwer!@#$QWER', 'Game', 'Masater')
    # new_group, created = Group.objects.get_or_create(name='game_master')
    # proj_add_perm = Permission.objects.get(name='Can add users to party')
    # new_group.permissions.add(proj_add_perm)
    # ct = ContentType.objects.get_for_model(Project)
    # permission = Permission.objects.create(codename='can_add_project', name='Can add project', content_type=ct)
    # new_group.permissions.add(permission)
    # new_group, created = Group.objects.get_or_create(name='aif_admin')


def add_user(userName, email, password, firstName, lastName,):
    if User.objects.filter(username=userName).count() == 0:
        user = User.objects.create_user(userName, email, password)
        user.first_name = firstName
        user.last_name = lastName
        user.save()


def add_chauncy():

    # djc = Character(name='Chauncy')
    djc = Character().new('Chauncy', 'Human', 'Warrior', 16, 14, 11, 16)

    djc.race = 'Human'
    djc.class = 'Warrior'
    djc.gender = 'Male'
    djc.age = 19
    djc.height = "6'"
    djc.weight = 175
    djc.notes = ""
    djc.open = False

    djc.gold_amount = 5
    djc.silver_amount = 15
    djc.copper_amount = 10

    djc.save()

    for skill in ["Armorer", "Awareness", "Balance", "Block", "Disarm", "Melee", "Missile", "Mounted Battle", "Scrapping", "Stamina", "Weaponsmith"]:
        cs = djc.classskills_set.create(item_name=skill)
        cs.rank = self.char[aif.CSP + skill][aif.RANK]
        cs.order = int(cs.rank / 4)
        cs.buff = self.char[aif.CSP + skill][aif.MODIFIERS]
        cs.adjusted = self.char[aif.CSP + skill][aif.ADJ]
        cs.mastered = self.char[aif.CSP + skill][aif.MASTERED]
        cs.description = self.char[aif.CSP + skill][aif.DESC]
        cs.save()

    for skill in ["Appraising", "Bartering", "History", "Instinct", "Leadership", "Linguistics", "Wisdom"]:
        rs = djc.racialskills_set.create(item_name=skill)
        rs.rank = self.char[aif.RSP + skill][aif.RANK]
        rs.order = int(cs.rank / 4)
        rs.buff = self.char[aif.RSP + skill][aif.MODIFIERS]
        rs.adjusted = self.char[aif.RSP + skill][aif.ADJ]
        rs.mastered = self.char[aif.RSP + skill][aif.MASTERED]
        rs.description = self.char[aif.RSP + skill][aif.DESC]
        rs.save()

    for weapon in ["Slashing Group", "Piercing Group", "Bludgeoning Group", "Cleaving Group", "Throwing Group", "Bow Group"]:
        w = djc.weapons_set.create(item_name=weapon)
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

    for armor in ["Light Armor Group", "Medium Armor Group", "Heavy Armor Group", "Helmet Group", "Unarmed Group", "Shield Group"]:
        a = djc.armor_set.create(item_name=armor)
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

def add_florian():

    djc = Character(name='Florian')

    djc.race = 'Elf'
    djc.class = 'Wizard'
    djc.gender = 'Male'
    djc.age = 108
    djc.height = "5'4\""
    djc.weight = 108
    djc.notes = ""
    djc.open = False

    djc.str_base = 10
    djc.str_buff = 0
    djc.str_adjusted = 10
    djc.str_modifiers = ""

    djc.dex_base = 12
    djc.dex_buff = 0
    djc.dex_adjusted = 12
    djc.dex_modifiers = ""

    djc.int_base = 18
    djc.int_buff = 0
    djc.int_adjusted = 18
    djc.int_modifiers = "+2"

    djc.health_base = 15
    djc.health_buff = 0
    djc.health_adjusted = 15
    djc.health_modifiers = ""
    djc.health_current = 15

    djc.movement = ""
    djc.walking_base = 36
    djc.walking_buff = 0
    djc.walking_adjusted = 36

    djc.running_base = 72
    djc.running_buff = 0
    djc.running_adjusted = 72

    djc.swimming_base = 18
    djc.swimming_buff = 0
    djc.swimming_adjusted = 18

    djc.encumbrance = 20
    djc.total_load = 0
    djc.modifiers = 0
    djc.burdened = 10

    djc.level = 1
    djc.experience = 0
    djc.next_level = 10

    djc.knockdown_base = 5
    djc.knockdown_buff = 0
    djc.knockdown_cf_points = 0
    djc.knockdown_adjusted = 5

    djc.defense_base = 13
    djc.defense_buff = 0
    djc.defense_cf_points = 0
    djc.defense_adjusted = 13

    djc.stun_base = 9
    djc.stun_buff = 0
    djc.stun_cf_points = 0
    djc.stun_adjusted = 9
    djc.stun_current = 0

    djc.endurance_base = 15
    djc.endurance_buff = 0
    djc.endurance_cf_points = 0
    djc.endurance_adjusted = 15

    djc.fatigue = 0
    djc.extra_fatigue = 0

    djc.withstand_dice = 3
    djc.withstand_modifiers = "+1"
    djc.withstand_adjusted = "3d6+1"

    djc.dodge_dice = 4
    djc.dodge_modifiers = ""
    djc.dodge_adjusted = "4d6"

    djc.resist_dice = 3
    djc.resist_modifiers = ""
    djc.resist_adjusted = "3d6"

    djc.honor_points_base = 0
    djc.honor_points_current = 0

    djc.spell_points_base = 0
    djc.spell_points_current = 0
    djc.spell_effectiveness_modifier = 0

    djc.damage_dice_base = 0
    djc.damage_dice_buff = 0
    djc.damage_dice_adjusted = "0"

    djc.damage_mods_base = 0
    djc.damage_mods_buff = 0
    djc.damage_mods_adjusted = ""

    djc.damage_adjusted = ""

    djc.to_hit_dice_base = 3
    djc.to_hit_dice_buff = 0
    djc.to_hit_dice_adjusted = "3d6"

    djc.to_hit_mods_base = 0
    djc.to_hit_mods_buff = 0
    djc.to_hit_mods_adjusted = ""

    djc.to_hit_adjusted = "3d6"

    djc.actions_base = 1
    djc.actions_buff = 0
    djc.actions_adjusted = "1"

    djc.outside_search_dice = 4
    djc.outside_search_modifiers = 0
    djc.outside_search_adjusted = "4d6"

    djc.underground_search_dice = 4
    djc.underground_search_modifiers = 0
    djc.underground_search_adjusted = "4d6"

    djc.spbc_buff = 0

    djc.gold_amount = 4
    djc.gold_load = .04

    djc.silver_amount = 17
    djc.silver_load = .17

    djc.copper_amount = 11
    djc.copper_load = .11

    djc.current_round = 0
    djc.mastered_count = 0
    djc.game_day = 0
    djc.game_time = ""

    djc.save()

    for skill in ["Accuracy", "Brew", "Diminish", "Focus", "Item", "Lore", "Scribe"]:
        cs = djc.classskills_set.create(item_name=skill)
        cs.rank = self.char[aif.CSP + skill][aif.RANK]
        cs.order = int(cs.rank / 4)
        cs.buff = self.char[aif.CSP + skill][aif.MODIFIERS]
        cs.adjusted = self.char[aif.CSP + skill][aif.ADJ]
        cs.mastered = self.char[aif.CSP + skill][aif.MASTERED]
        cs.description = self.char[aif.CSP + skill][aif.DESC]
        cs.save()

    for skill in  ["Camouflage", "Elven History", "Faerie Flare", "Nightvision", "Plant Empathy", "Sense Enchantment", "Tracking"]:
        rs = djc.racialskills_set.create(item_name=skill)
        rs.rank = self.char[aif.RSP + skill][aif.RANK]
        rs.order = int(cs.rank / 4)
        rs.buff = self.char[aif.RSP + skill][aif.MODIFIERS]
        rs.adjusted = self.char[aif.RSP + skill][aif.ADJ]
        rs.mastered = self.char[aif.RSP + skill][aif.MASTERED]
        rs.description = self.char[aif.RSP + skill][aif.DESC]
        rs.save()

    for weapon in ["Slashing Group", "Piercing Group", "Bludgeoning Group", "Cleaving Group", "Throwing Group", "Bow Group"]:
        w = djc.weapons_set.create(item_name=weapon)
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

    for armor in ["Light Armor Group", "Medium Armor Group", "Heavy Armor Group", "Helmet Group", "Unarmed Group", "Shield Group"]:
        a = djc.armor_set.create(item_name=armor)
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
