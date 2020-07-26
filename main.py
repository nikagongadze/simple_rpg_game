import os
from classes.game import Person, bcolors
from classes.magic import spell
from classes.inventory import items


# Create black magic
Fire = spell("Fire", 10, 50, "black")
Thunder = spell("Thunder", 7, 70, "black")
Blizzard = spell("Blizzard", 14,80, "black")
Meteor = spell("Meteor", 20, 200, "black")
Quakke = spell("Quakke", 5, 10, "black")

# Create white magic
Heal = spell("Heal", 10, 50, "white")
Cure = spell("Cure", 7, 70, "white")

# Create items
potion = items("Potion", "potion", "heals 50 hp", 50)
hipotion = items("Hi-potion", "potion", "heals 100 hp", 100)
superpotion = items("Super potion", "potion", "heals 500 hp ", 500)
elexir = items("Elexir", "elexir", "restores fully hp of one member", 9999)
hielexir = items("Hi-elexir", "elexir", "restores fully hp for one member", 9999)
granade = items("Granade", "attck", "deals for 500 dmg", 500)

hero_magic = [Fire, Thunder, Blizzard, Meteor, Quakke, Heal, Cure]
hero_items = [{"item" : potion, "quantity" : 15}, {"item" : hipotion, "quantity" : 5},
              {"item" : superpotion, "quantity" : 2}, {"item" : elexir, "quantity" : 6},
              {"item" : hielexir, "quantity" : 3}, {"item" : granade, "quantity" : 5}]
# Instantiate people
hero = Person("ARAMIS", 1500, 180, 80, 100, hero_magic, hero_items)

enemy = Person("VALDOS", 1200, 120, 60, 50, [], [])




print(bcolors.fail + bcolors.bold + "ENEMY ATTACS!" + bcolors.endc)

while True:

    hero.get_stats()
    enemy.enemy_stats()
    print(" ")
    hero.choose_action()
    choose = input("choose action: ")
    os.system('clear')

    if int(choose) == 1:

        gen = hero.generate_dmg()
        enemy.get_dmg(gen)
        print("")
        print(bcolors.okblue + bcolors.bold + hero.name + ": attacked for " + str(gen) + " point of damage."
              + bcolors.endc)

        enm_dmg = enemy.generate_dmg()
        hero.get_dmg(enm_dmg)
        print(bcolors.fail + bcolors.bold + enemy.name + ": attacked for " + str(enm_dmg) + " point of damage." + bcolors.endc)
        print("")

        if enemy.hp == 0:
            print(" ")

            print(bcolors.fail + bcolors.bold + "==============" + bcolors.endc)
            print(bcolors.fail + bcolors.bold + "= ENEMY DIED =" + bcolors.endc)
            print(bcolors.fail + bcolors.bold + "==============" + bcolors.endc)
            break

        if hero.hp == 0:
            print(" ")
            print(bcolors.fail + bcolors.bold + "=============" + bcolors.endc)
            print(bcolors.fail + bcolors.bold + "= HERO DIED =" + bcolors.endc)
            print(bcolors.fail + bcolors.bold + "=============" + bcolors.endc)
            break

    elif int(choose) == 2:
        hero.choose_magic()
        chose_mgc = int(input("Choose magic: ")) - 1

        spell = hero.magic[chose_mgc]
        magic_dmg = spell.generate_spell_dmg()

        current = hero.get_mp()
        hero.reduce_mp(spell.cost)

        if spell.cost > current:
            hero.mp = current
            print(bcolors.fail + "\n you dont have enough MP" + bcolors.endc)
            continue

        if spell.type == "black":
            enemy.get_dmg(magic_dmg)
        elif spell.type == "white" and hero.hp < 1000:
            hero.hp += spell.dmg

        elif spell.type == "white" and hero.hp > 1000:
            hero.mp += spell.cost

    if enemy.hp == 0:
        print(" ")

        print(bcolors.fail + bcolors.bold + "==============" + bcolors.endc)
        print(bcolors.fail + bcolors.bold + "= ENEMY DIED =" + bcolors.endc)
        print(bcolors.fail + bcolors.bold + "==============" + bcolors.endc)
        break

    if hero.hp == 0:
        print(" ")
        print(bcolors.fail + bcolors.bold + "=============" + bcolors.endc)
        print(bcolors.fail + bcolors.bold + "= HERO DIED =" + bcolors.endc)
        print(bcolors.fail + bcolors.bold + "=============" + bcolors.endc)
        break

    elif int(choose) == 3:
        hero.choose_item()
        item_chooise = int(input("choose item: ")) - 1
        item  = hero.items[item_chooise]

        if item["quantity"] >= 1 :
            if item["item"].type == "potion":
                item["quantity"] -= 1

                hero.hp += item["item"].prop
                if hero.hp > hero.max_hp:
                    item["quantity"] += 1
                    print(bcolors.fail + bcolors.bold + "your hp wont be more then your max hp" + bcolors.endc)
                    hero.hp -= item["item"].prop

            elif item["item"].type == "elexir":
                item["quantity"] -= 1
                hero.hp = hero.max_hp
                hero.mp = hero.max_mp
                print(bcolors.okgreen + bcolors.bold + "fully restores player HP/MP" + bcolors.endc)

            elif item["item"].type == "attck":
                item["quantity"] -= 1
                enemy.get_dmg(item["item"].prop)
                print(bcolors.fail + bcolors.bold + "enemy got " + str(item["item"].prop) + bcolors.endc)
                if hero.hp == 0:
                    print(" ")
                    print(bcolors.fail + bcolors.bold + "=============" + bcolors.endc)
                    print(bcolors.fail + bcolors.bold + "= HERO DIED =" + bcolors.endc)
                    print(bcolors.fail + bcolors.bold + "=============" + bcolors.endc)
                    break

                if enemy.hp == 0:
                    print(" ")

                    print(bcolors.fail + bcolors.bold + "==============" + bcolors.endc)
                    print(bcolors.fail + bcolors.bold + "= ENEMY DIED =" + bcolors.endc)
                    print(bcolors.fail + bcolors.bold + "==============" + bcolors.endc)
                    break

        else:
            print(bcolors.fail + bcolors.bold + "this item is out of range" + bcolors.endc)



