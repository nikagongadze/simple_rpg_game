import random

class bcolors:
    header = '\033[95m'
    okblue = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endc = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic,items):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.current_hp = hp
        self.mp = mp
        self.items = items
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['attack', 'magic', 'items']
        self.name = name

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_heal(self,heal):
        return self.hp + heal

    def get_spells(self, i):
        get_spell = self.magic[i]
        return get_spell

    def get_dmg(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n"+bcolors.okblue + bcolors.bold + "Actions" + bcolors.endc)
        for item in self.actions:
            print("     "+str(i) + ":" + item)
            i += 1

    def choose_magic(self):
        i = 1
        print(" ")
        print(" ")
        print("\n"+bcolors.okblue + bcolors.bold + "Magic" + bcolors.endc)
        for spell in self.magic:
            print("     "+str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")" + " (damage " + str(spell.dmg) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print(" ")
        print(" ")
        print("\n"+bcolors.okblue + bcolors.bold + "Magic" + bcolors.endc)
        for item in self.items:
            print("     "+str(i) + ":", item["item"].name, " - " + item["item"].description + " (" + str(item["quantity"]) + "pcs)")
            i += 1

    def get_stats(self):
        hp_bar = "█"
        bar_ticks = (self.hp / self.max_hp) * 100 / 4
        mp_bar = "█"
        mp_ticks = (self.mp / self.max_mp) * 100 / 4

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 10:
            decreased = 10 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 9 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print(bcolors.header + bcolors.bold + "NAME                HP                                        MP" + bcolors.endc)


        print(
            bcolors.bold + self.name + "   "+ bcolors.endc + current_hp +
             "|" + bcolors.okgreen + hp_bar + bcolors.endc + "|" + bcolors.endc + "     " + current_mp +
            bcolors.bold +
            "  |" + bcolors.okblue + "██████████" + bcolors.endc + "|")

    def enemy_stats(self):
        hp_bar = "█"
        bar_ticks = (self.hp / self.max_hp) * 100 / 4

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        current_hp = ""

        if len(hp_string) < 10:
            decreased = 10 - len(hp_string)
            while decreased > 0:
                 current_hp += " "
                 decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.max_mp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 9 - len(mp_string)
            while decreased > 0:
                 current_mp += " "
                 decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string


        print("")
        print(
            bcolors.bold + bcolors.fail + self.name + bcolors.endc +  "   " + current_hp + bcolors.endc +
            "|" + bcolors.fail + hp_bar + bcolors.endc + "|" + bcolors.endc + "     " + current_mp +
            bcolors.bold +
            "  |" + bcolors.fail + "██████████" + bcolors.endc + "|")


        

