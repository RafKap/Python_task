import random
from game.Magic import Spell
from game.Inventory import Item
import pprint



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Character:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]


    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)



    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp


    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]["name"]
    #
    # def get_spell_mp_cost(self, i):
    #     return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(f'{bcolors.OKBLUE}{bcolors.BOLD}Actions{bcolors.ENDC}')
        for action in self.actions:
            print(f'    {str(i)}. {action}')
            i += 1

    def choose_magic(self):
        i = 1
        print(f'{bcolors.OKBLUE}{bcolors.BOLD}Magic{bcolors.ENDC}')
        print(f'    {str(0)}. Go back')
        for spell in self.magic:
            print(f'    {str(i)}. {spell.name} (cost: {str(spell.cost)})')
            i += 1
        print()

    def choose_item(self):
        i = 1
        print(f'{bcolors.OKBLUE}{bcolors.BOLD}Items{bcolors.ENDC}')
        print(f'    {str(0)}. Go back')
        for item in self.items:
            print(f'    {str(i)}. {item["item"].name}: {item["item"].description} - Qty: {item["quantity"]}')
            i += 1
        print()


    def choose_targer(self, enemies):
        i = 1
        print(f'{bcolors.FAIL}{bcolors.BOLD}Enemies{bcolors.ENDC}')
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print(f'    {str(i)}. {enemy.name} (HP {enemy.hp}/{enemy.maxhp})')
                i += 1
        target = int(input(f'Choose target:')) - 1
        return target





    def get_stats(self):
        hp_current = self.hp / self.maxhp * 100
        hp = int(hp_current) * 26 / 100
        hp = int(hp)
        if (len(str(self.hp)) + len(str(self.maxhp))) == 8:
            hp_space = 2
        elif len(str(self.maxhp)) == 4:
            hp_space = 1
        else:
            hp_space = 0


        mp_current = self.mp / self.maxmp * 100
        mp = int(mp_current) * 10 / 100
        mp = int(mp)
        if (len(str(self.mp)) + len(str(self.maxmp))) == 6:
            mp_space = 2
        elif len(str(self.maxmp)) == 3:
            mp_space = 1
        else:
            mp_space = 0


        print(f'Name                {" " * hp_space}{bcolors.OKGREEN}__________________________        '
              f'{" " * mp_space}{bcolors.OKBLUE}__________{bcolors.ENDC}')
        print(f'{bcolors.BOLD}{self.name}:{" " * (8 - len(self.name))}   '
              f'{" " * (3 - len(str(self.hp)))}{self.hp}/{self.maxhp}{bcolors.OKGREEN}'
              f'|{"█" * hp}{" " * (26 - hp)}|{bcolors.ENDC} '
              f'{" " * (2 - len(str(self.mp)))}{self.mp}/{self.maxmp}{bcolors.OKBLUE}'
              f'|{"█" * mp}{" " * (10 - mp)}|{bcolors.ENDC}')

        print(f'                    {" " * hp_space}HP                                {" " * mp_space}MP')



    def get_enemy_stats(self):
        hp_current = self.hp / self.maxhp * 100
        hp = int(hp_current) * 26 / 100
        hp = int(hp)
        if (len(str(self.hp)) + len(str(self.maxhp))) == 8:
            hp_space = 2
        elif len(str(self.maxhp)) == 4:
            hp_space = 1
        else:
            hp_space = 0


        print(f'Name                {" " * hp_space}{bcolors.FAIL}__________________________{bcolors.ENDC}')
        print(f'{bcolors.BOLD}{self.name}:{" " * (8 - len(self.name))}   '
              f'{" " * (3 - len(str(self.hp)))}{self.hp}/{self.maxhp}{bcolors.FAIL}'
              f'|{"█" * hp}{" " * (26 - hp)}|{bcolors.ENDC}{bcolors.ENDC}')

        print(f'                    {" " * hp_space}HP')


    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        if self.mp < spell.cost:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg


