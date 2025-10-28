from random import randint

def first_choice():
    return int(input("""What would you like to do next?
    1 = More Info
    2 = Start building
    """))

def dnd_info_selection(): # what do you want info about?
    info = int(input("""What do you want to learn about?
                1 = Classes
                2 = Species
                3 = Backgrounds
                4 = Feats
                5 = Building process
                6 = Start building
                """))
    return info

def start_building(): #how do you wanna roll your atributes?
    print("""Alright! Lets start building!
    Your first step is to roll your atributes.
    You can either roll 4d6 6 times yourself,
    let me roll for you or use the standart spread.""")
    build_step_1 = int(input("""What would you like to do?
                1 = Roll yourself
                2 = Let me roll for you
                3 = Use the spread
                """))
    return build_step_1

def dnd_class_info_selection(): #which class info?
    dnd_class_info = int(input("""What class do you want to learn about?
            1 = Barbarian
            2 = Bard
            3 = Cleric
            4 = Druid
            5 = Fighter
            6 = Monk
            7 = Paladin
            8 = Ranger
            9 = Rogue
            10 = Sorcerer
            11 = Warlock
            12 = Wizard
            """))
    return dnd_class_info

def species_info_selection(): #which species info?
    species_info = int(input("""What species do you want to learn about?
        1 = Aasimar
        2 = Dragonborn
        3 = Dwarf
        4 = Elf
        5 = Gnome
        6 = Goliath
        7 = Halfling
        8 = Human
        9 = Orc
        10 = Tiefling
        """))
    return species_info

def bg_info_selection(): #which background info?
    bg_info = int(input("""What background do you want to learn about?
        1 = Acolyte
        2 = Artisan
        3 = Charlatan
        4 = Criminal
        5 = Entertainer
        6 = Farmer
        7 = Guard
        8 = Guide
        9 = Hermit
        10 = Merchant
        11 = Noble
        12 = Sage
        13 = Sailor
        14 = Scribe
        15 = Soldier
        16 = Wayfarer
        """))
    return bg_info

def feat_info_selection(): #which feat info?
    feat_info = int(input("""There are many feats in DnD. At this point
    only Origin feats are relevant however.
    Which Origin feat do you want to learn about?
        1 = Alert
        2 = Crafter
        3 = Healer
        4 = Lucky
        5 = Magic Initiate
        6 = Musician
        7 = Savage Attacker
        8 = Skilled
        9 = Tavern Brawler
        10 = Tough
        """))
    return feat_info

def roll_yourself():
    results = []
    print("""Please roll 6x 4d6, remove the smallest
result and note down your results.
F.e.: You rolled 3, 6, 4 and 3:
Remove one of the threes, because it's the smallest result
and add the others together (3+6+4=13).
Do this 6 times.""")
    results.append(int(input("Roll 1: ")))
    results.append(int(input("Roll 2: ")))
    results.append(int(input("Roll 3: ")))
    results.append(int(input("Roll 4: ")))
    results.append(int(input("Roll 5: ")))
    results.append(int(input("Roll 6: ")))
    print("Your results are: ", results)

def pc_roll():
    numbers = []
    results = []
    print("I will roll your atributes for you now.")
    counter = 0
    times = 0
    while times < 6:
        while counter < 4:
            zahl = randint(1, 6)
            numbers.append(zahl)
            counter += 1
        print("Your numbers are: ", numbers)
        numbers.remove(min(numbers))
        total = (numbers[0] + numbers[1] + numbers[2])
        print("Your total is: ", total)
        results.append(total)
        counter = 0
        numbers = []
        times += 1
    print("Your results are: ", results)

def spread():
    print("""Great, you want to use the standart spread.
       That means, your numbers are:
       15, 14, 13, 12, 10 and 8.""")
    results = [15, 14, 13, 12, 10, 8]