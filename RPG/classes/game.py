import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    # def disable(self):
    #     self.HEADER = ''
    #     self.OKBLUE = ''
    #     self.OKGREEN = ''
    #     self.WARNING = ''
    #     self.FAIL = ''
    #     self.ENDC = ''


class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.maxmp = mp
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.df = df
        self.magic = magic
        self.items = items
        self.atklow = atk - 10
        self.atkhigh = atk + 10
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atklow, self.atkhigh)

    def generate_spell_dmg(self, i):
        magiclow = self.magic[i]["dmg"] - 10
        magichigh = self.magic[i]["dmg"] + 5
        return random.randrange(magiclow, magichigh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, heal):
        self.hp += heal

        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_maxhp(self):
        return self.maxhp

    # reduce magic points, because for every spell, there is a cost for using it
    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        for item in self.actions:
            print("   " + str(i) + ": " + item)
            i += 1

    def choose_magic(self):
        i = 1
        for spell in self.magic:
            print("   " + str(i) + ": " + spell.name, "(Cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        for item in self.items:
            print("   " + str(i) + ": " + item["item"].name, ",", item["item"].description,
                  "(x" + str(item["quantity"]) + ")")
            i += 1

    def player_stats(self):

        # build health bar
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4
        while bar_ticks > 0:
            hp_bar += '█'
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        # build magic point bar
        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10
        while mp_bar_ticks > 0:
            mp_bar += '█'
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        print("          HP                                MP")
        print("         _________________________               __________ ")
        print(
            str(self.get_hp()) + "/" + str(
                self.maxhp) + " |" + bcolors.OKGREEN + hp_bar +
            bcolors.ENDC + "|       " + str(
                self.get_mp()) + "/" + str(self.maxmp) + " |" +
            bcolors.OKBLUE
            + mp_bar + bcolors.ENDC + "|")
