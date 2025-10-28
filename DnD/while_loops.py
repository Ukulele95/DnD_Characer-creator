import choices as c
import texts as t

def making_choice(): #Choose wether to get info or start building
    while True:
        choice = c.first_choice() #Select your choice
        if choice == 1:
            info = c.dnd_info_selection() #Choose which info do you want?
            what_info(info) #puts you to the specific info selection
            break
        elif choice == 2:
            build_step_1 = c.start_building() #Starts the building process
            roll_attributes(build_step_1) #Choose how to roll attributes
            break
        else:
            print("I'm sorry - Your response isn't valid.")
        return choice


def what_info(info): #Here you can choose what you want info about
    while True:
        if info == 1:
            dnd_class_info = c.dnd_class_info_selection() #classes
            which_class_info(dnd_class_info)
            break
        elif info == 2:
            species_info = c.species_info_selection() #species
            which_species_info(species_info)
            break
        elif info == 3:
            bg_info = c.bg_info_selection() #backgrounds
            which_bg_info(bg_info)
            break
        elif info == 4:
            feat_info = c.feat_info_selection() #feats
            which_feat_info(feat_info)
            break
        elif info == 5:
            print(t.build_info) #building process
            break
        elif info == 6:
            c.start_building() #start building instead
        else:
            print("Sorry, that option isn't available.")
            c.dnd_info_selection()
        return info

def roll_attributes(build_step_1):
    while True:
        if build_step_1 == 1:
            roll_yourself = c.roll_yourself()
            break
        elif build_step_1 == 2:
            pc_roll = c.pc_roll()
            break
        elif build_step_1 == 3:
            spread = c.spread()
            break
        else:
            print("Sorry, that option isn't available.")
            c.start_building()
        return build_step_1

def which_class_info(dnd_class_info):
    while True:
        if dnd_class_info == 1:
            print(t.barbarian_info)
            break
        elif dnd_class_info == 2:
            print(t.bard_info)
            break
        elif dnd_class_info == 3:
            print(t.cleric_info)
            break
        elif dnd_class_info == 4:
            print(t.druid_info)
            break
        elif dnd_class_info == 5:
            print(t.fighter_info)
            break
        elif dnd_class_info == 6:
            print(t.monk_info)
            break
        elif dnd_class_info == 7:
            print(t.paladin_info)
            break
        elif dnd_class_info == 8:
            print(t.ranger_info)
            break
        elif dnd_class_info == 9:
            print(t.rogue_info)
            break
        elif dnd_class_info == 10:
            print(t.sorcerer_info)
            break
        elif dnd_class_info == 11:
            print(t.warlock_info)
            break
        elif dnd_class_info == 12:
            print(t.wizard_info)
            break
        else:
            print("Sorry, that option isn't available.")
            c.dnd_class_info_selection()
        return dnd_class_info

def which_species_info(species_info):
    while True:
        if species_info == 1:
            print(t.aasimar_info)
            break
        elif species_info == 2:
            print(t.dragonborn_info)
            break
        elif species_info == 3:
            print(t.dwarf_info)
            break
        elif species_info == 4:
            print(t.elf_info)
            break
        elif species_info == 5:
            print(t.gnome_info)
            break
        elif species_info == 6:
            print(t.goliath_info)
            break
        elif species_info == 7:
            print(t.halfling_info)
            break
        elif species_info == 8:
            print(t.human_info)
            break
        elif species_info == 9:
            print(t.orc_info)
            break
        elif species_info == 10:
            print(t.tiefling_info)
            break
        else:
            print("Sorry, that option isn't available.")
            c.species_info_selection()
        return species_info

def which_bg_info(bg_info):
    while True:
        if bg_info == 1:
            print(t.acolyte_info)
            break
        elif bg_info == 2:
            print(t.artisan_info)
            break
        elif bg_info == 3:
            print(t.charlatan_info)
            break
        elif bg_info == 4:
            print(t.criminal_info)
            break
        elif bg_info == 5:
            print(t.entertainer_info)
            break
        elif bg_info == 6:
            print(t.farmer_info)
            break
        elif bg_info == 7:
            print(t.guard_info)
            break
        elif bg_info == 8:
            print(t.guide_info)
            break
        elif bg_info == 9:
            print(t.hermit_info)
            break
        elif bg_info == 10:
            print(t.merchant_info)
            break
        elif bg_info == 11:
            print(t.noble_info)
            break
        elif bg_info == 12:
            print(t.sage_info)
            break
        elif bg_info == 13:
            print(t.sailor_info)
            break
        elif bg_info == 14:
            print(t.scribe_info)
            break
        elif bg_info == 15:
            print(t.soldier_info)
            break
        elif bg_info == 16:
            print(t.wayfarer_info)
            break
        else:
            print("Sorry, that option isn't available.")
            c.bg_info_selection()
        return bg_info

def which_feat_info(feat_info):
    while True:
        if feat_info == 1:
            print(t.alert_info)
            break
        elif feat_info == 2:
            print(t.crafter_info)
            break
        elif feat_info == 3:
            print(t.healer_info)
            break
        elif feat_info == 4:
            print(t.lucky_info)
            break
        elif feat_info == 5:
            print(t.magic_initiate_info)
            break
        elif feat_info == 6:
            print(t.musician_info)
            break
        elif feat_info == 7:
            print(t.savage_attacker_info)
            break
        elif feat_info == 8:
            print(t.skilled_info)
            break
        elif feat_info == 9:
            print(t.tavern_brawler_info)
            break
        elif feat_info == 10:
            print(t.tough_info)
            break
        else:
            print("Sorry, that option isn't available.")
            c.feat_info_selection()
        return feat_info