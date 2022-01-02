from random import random, randint
import json


amuCraftedMods = [
    [
        ['Hit Causes Monster To Flee', 3, 11],
        ['5% Chance To Cast Level 4 Frost Nova When Struck', 0, 0],
        ['Attacker Takes Damage of', 3, 10],
    ],
    [
        ['Faster Run/Walk', 5, 10],
        ['Life Stolen Per Hit %', 1, 4],
        ['+ To Life', 10, 20],
    ],
    [
        ['Faster Cast Rate', 5, 10],
        ['Regenerate Mana %', 4, 10],
        ['+ To Mana', 10, 20],
    ],
    [
        ['Increased Chance Of Blocking', 1, 10],
        ['Magic Damage Reduced By', 1, 2],
        ['Damage Reduced By', 1, 4],
    ],
]
amuPrefixMods = [
    # +1-2 to all char skill levels
    ['Barbarian Skill Level', 1, 2],
    ['Amazon Skill Level', 1, 2],
    ['Necromancer Skill Level', 1, 2],
    ['Druid Skill Level', 1, 2],
    ['Paladin Skill Level', 1, 2],
    ['Sorceress Skill Level', 1, 2],
    ['Assassin Skill Level', 1, 2],

    # +1-2 to char skill tree levels
    ['Bow and Crossbow Skills', 1, 2],
    ['Javelin and Spear Skills', 1, 2],
    ['Passive and Magic Skills', 1, 2],
    ['Martial Arts', 1, 2],
    ['Shadow Discipline', 1, 2],
    ['Traps', 1, 2],
    ['Elemental Skills', 1, 2],
    ['Shapeshifting Skills', 1, 2],
    ['Summoning Skills', 1, 2],
    ['Warcries', 1, 2],
    ['Combat Masteries', 1, 2],
    ['BCombat Skills', 1, 2],
    ['Summoning Spells', 1, 2],
    ['Curses', 1, 2],
    ['Bone and Poison Spells', 1, 2],
    ['PCombat Skills', 1, 2],
    ['Defensive Auras', 1, 2],
    ['Combat Auras', 1, 2],
    ['Fire Spells', 1, 2],
    ['Lightning Spells', 1, 2],
    ['Cold Spells', 1, 2],
    
    ['Attack Rating', 1, 90],
    ['Maximum Stamina', 5, 20],
    ['Cold Resist', 5, 40],
    ['Fire Resist', 5, 40],
    ['Poison Resist', 5, 40],
    ['Lightning Resist', 5, 40],
    ['All Resistances', 3, 20],
    ['Damage Taken Goes to Mana', 7, 12],
    ['Better Chance of Getting Magic Items', 5, 10],
    ['Light Radius', 1, 2]
]
amuSuffixMods = [
    ['10% change to cast level 3 Hydra', 0, 0],
    ['5% change to cast level 3 Frost Nova ', 0, 0],
    ['10% change to cast level 3 Charged Bolt', 0, 0],
    ['12% change to cast level 4 Charged Bolt', 0, 0],
    ['14% change to cast level 5 Charged Bolt', 0, 0],
    ['5% change to cast level 3 Chain Lightning', 0, 0],
    ['8% change to cast level 3 Chain Lightning', 0, 0],
    ['8% change to cast level 5 Chain Lightning', 0, 0],
    ['10% Faster Cast Rate', 0, 0],
    ['Minimum Damage', 2, 9],
    ['Maximum Damage', 1, 4],
    ['5% Bonus to Attack Rating or +5 to Light Radius', 0, 1],
    ['Attack Ratting 10-30 r 1-3 Light Radius', 0, 1],
    ['Adds 1-# Fire Damage', 2, 6],
    ['Adds 1-# Lightning Damage', 11, 23],
    ['Adds 1-# Cold Damage', 3, 6],
    ['+50 Poison Damage over 3s', 0, 0],
    ['% Mana Stolen per Hit', 3, 8],
    ['% Life Stolen per Hit', 2, 6],
    ['+ to Strength', 1, 30],
    ['+ to Dexterity', 1, 20],
    ['+ to Energy', 1, 20],
    ['to Life', 1, 60],
    ['Replenish Life', 2, 10],
    ['Damage Reduced by', 1, 4],
    ['Magic Damage Reduced by', 1, 3],
    ['Half Freeze Duration', 0, 0],
    ['Poison Length Reduced by %', 25, 75],
    ['Extra Gold from Monsters %', 25, 80],
    ['Better Chance of Finding Magic Items %', 5, 25],
    ['Level 2 Tornado Charges 25/25', 0, 0],
    ['Level 3 Twister Charges 27/75', 0, 0],
    ['Level 2 Grim Ward 25/25', 0, 0],
    ['Level 5 Holy Bolt 32/32', 0, 0],
    ['Level 2 Grim Ward 25/25', 0, 0],
    ['Level 1 Bne Spirit 22/22', 0, 0],
    ['Level 2 Attract 25/25', 0, 0],
    ['Level 3 Teleport 27/27', 0, 0],
    ['Level 5 Frost Nova 32/32', 0, 0],
    ['Level 6 Inner Sight 52/52', 0, 0],

]

prefix = (randint(0, len(amuPrefixMods)))

def getCraftedAmu() :
    prefixmod = randint(1, 3)
    suffixmod = 4 - prefixmod
    craftedmod = randint(0, 3)

    d = {3: 4, 5: 6, 7: 8}
    x = {1: 2}
    x.update(d)

    craftedAmu = {}
    print("Prefix modes:", prefixmod)
    print("Suffix modes:", suffixmod)
    print("Crafted mode:", craftedmod)
    print()

    craftedAmu.update({amuCraftedMods[craftedmod][0][0]: randint(amuCraftedMods[craftedmod][0][1], amuCraftedMods[craftedmod][0][2])})
    craftedAmu.update({amuCraftedMods[craftedmod][1][0]: randint(amuCraftedMods[craftedmod][1][1], amuCraftedMods[craftedmod][1][2])})
    craftedAmu.update({amuCraftedMods[craftedmod][2][0]: randint(amuCraftedMods[craftedmod][2][1], amuCraftedMods[craftedmod][2][2])})

    for x in range(0, prefixmod):
        temppref = randint(0, len(amuPrefixMods) - 1)
        craftedAmu.update({amuPrefixMods[temppref][0]: randint(amuPrefixMods[temppref][1], amuPrefixMods[temppref][2])})

    for x in range(0, suffixmod):
        tempsuf = randint(0, len(amuSuffixMods) - 1)
        craftedAmu.update({amuSuffixMods[temppref][0]: randint(amuSuffixMods[temppref][1], amuSuffixMods[temppref][2])})

    jsonAmu = json.dumps(craftedAmu, indent=5)
    print(jsonAmu)
    return


getCraftedAmu()
