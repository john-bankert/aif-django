import random
import json

def hex_string(length):
    s = ""
    h = "0123456789ABCDEF"
    for i in range(0, length):
        p = random.randint(0, 15)
        s += h[p:(p + 1)]
    return s
    
def bump_time(char):
    _hm = char.game_time.split(":")
    hour = int(_hm[0])
    minute = int(_hm[1]) + 1
    if minute > 59:
        minute = 0
        hour += 1
        if hour > 23:
            hour = 0
            char.game_day += 1
            
    _hm[0] = ("" if hour > 9 else "0") + str(hour)
    _hm[1] = ("" if minute > 9 else "0") + str(minute)
    char.game_time = _hm[0] + ":" + _hm[1]

def nones(n):
    return [None for _ in range(n)]

def lod(roll):
    if roll < 8:
        return 0
    else:
        i = 1
        while roll >= (8 + (i * 3)):
            i += 1
        return i

def roll_dice(num_dice, drop_lowest=True):
    rolls = []
    while len(rolls) < num_dice:
        rolls.append(random.randint(1, 6))
    sorted_rolls = sorted(rolls, reverse=True)
    roll_total = 0
    for i in range(num_dice):
        if i < (num_dice - 1):
            roll_total += sorted_rolls[i]
        elif drop_lowest:
            roll_total += sorted_rolls[i]
    return roll_total

def roll_combat(num_dice):
    results = {'total': 0, 'fatigue': 0}
    for i in range(num_dice):
        d6 = random.randint(1, 6)
        results['total'] += d6
        if d6 == 6:
            results['fatigue'] += 1
            
    if results['fatigue'] == 0:
        results['fatigue'] += 1

    return results
