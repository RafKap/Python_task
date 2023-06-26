import random

from game.Character import Character, bcolors
from game.Magic import Spell
from game.Inventory import Item


# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 50, 200, "black")
quake = Spell("Quake", 14, 140, "black")


# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create item
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("High potion", "potion", "Heals 100HP", 100)
superpotion = Item("Super potion", "potion", "Heal 200HP", 200)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("Mega elixir", "elixir", "Fully restore whole party HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 DMG", 500)



player_magic = [fire, thunder, blizzard, meteor, cure, cura]
enemy1_magic = [fire, thunder]
enemy2_magic = [blizzard, meteor]
enemy3_magic = [cure, cura]

player_items = [{"item": potion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 1},
                {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 2},
                {"item": grenade, "quantity": 1}]

# Instance characters
Player_1 = Character("Saw", 1000, 40, 160, 34, player_magic, player_items)
Player_2 = Character("Player_2", 1800, 100, 40, 34, player_magic, player_items)
Player_3 = Character("Pl_3", 1200, 20, 600, 34, player_magic, player_items)

enemy_1 = Character("Enemy_1", 1800, 65, 45, 25, enemy1_magic, [])
enemy_2 = Character("Enemy_2", 1000, 40, 100, 25, enemy2_magic, [])
enemy_3 = Character("Enemy_3", 1000, 20, 150, 0, enemy3_magic, [])

players = [Player_1, Player_2, Player_3]
enemies = [enemy_1, enemy_2, enemy_3]
#



print(f'{bcolors.FAIL}{bcolors.BOLD}AN ENEMY ATTACKS! {bcolors.ENDC}')
running = True
while running:

    print()
    print("Players:")
    for player in players:
        player.get_stats()
    print()


    print("Enemy:")
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        print("=" * 10)
        print(f'Player {bcolors.OKGREEN}{player.name}{bcolors.ENDC} turn')
        player.choose_action()
        choice = int(input("Chose action: ")) - 1
        print()


    # Attack
        if choice == 0:
            dmg = player.generate_damage()
            target_of_player = player.choose_targer(enemies)

            enemies[target_of_player].take_dmg(dmg)

            print(f'{bcolors.OKBLUE}You{bcolors.ENDC} deal {bcolors.OKBLUE}{dmg}{bcolors.ENDC} dmg to {bcolors.ENDC}'
                  f'{bcolors.FAIL}{enemies[target_of_player].name}{bcolors.ENDC}')

            if enemies[target_of_player].get_hp() == 0:
                print(f'{bcolors.FAIL}{enemies[target_of_player].name} was defeated{bcolors.ENDC}')
                del enemies[target_of_player]
                continue



    # Spells
        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1
            target_of_player = player.choose_targer(enemies)



            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            current_mp = player.get_mp()
            dmg = spell.generate_damage()

            if spell.cost > current_mp:
                print(f'{bcolors.FAIL}\nNot enough MP\n{bcolors.ENDC}')
                continue

            if spell.type == "white":
                before_hp = player.get_hp()
                player.heal(dmg)
                after_hp = player.get_hp()
                print(f'{bcolors.OKBLUE}{spell.name}{bcolors.ENDC} heals for {bcolors.OKBLUE}{str(dmg)}{bcolors.ENDC} HP')
                print(f'Healed from {bcolors.OKBLUE}{before_hp}{bcolors.ENDC} to {bcolors.OKBLUE}{after_hp}{bcolors.ENDC}')
            elif spell.type == "black":
                enemies[target_of_player].take_dmg(dmg)
                print(f'{bcolors.OKBLUE}{player.name}{bcolors.ENDC} attacked for '
                      f'{bcolors.OKBLUE}{dmg}{bcolors.ENDC} dmg with {bcolors.OKBLUE}{spell.name}{bcolors.ENDC} spell')

                if enemies[target_of_player].get_hp() == 0:
                    print(f'{bcolors.FAIL}{enemies[target_of_player].name} was defeated{bcolors.ENDC}')
                    del enemies[target_of_player]
                    continue

            player.reduce_mp(spell.cost)

        # Items
        elif choice == 2:
            player.choose_item()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(f'{bcolors.FAIL}None left...{bcolors.ENDC}')
                continue

            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                before_hp = player.get_hp()
                player.heal(item.prop)
                after_hp = player.get_hp()
                print(f'{bcolors.OKBLUE}{item.name}{bcolors.ENDC} heals for {bcolors.OKBLUE}{item.prop}{bcolors.ENDC}HP')
                print(f'Healed from {bcolors.OKBLUE}{before_hp}{bcolors.ENDC} to {bcolors.OKBLUE}{after_hp}{bcolors.ENDC}')

            elif item.type == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(f'{bcolors.OKBLUE}{item.name}{bcolors.ENDC} restore Your HP and MP')


            elif item.type == "attack":
                target_of_player = player.choose_targer(enemies)
                enemies[target_of_player].take_dmg(item.prop)
                print(f'{bcolors.OKBLUE}{player.name}{bcolors.ENDC} deal {bcolors.OKBLUE}{item.prop}{bcolors.ENDC} dmg'
                      f'with {bcolors.OKBLUE}{item.name}{bcolors.ENDC}')

            print()
            enemies[target_of_player].get_enemy_stats()
            print("-" * 10)
            print()

        # Check if battle is over
        defeated_players = 0
        defeated_enemy = 0

        for enemy in enemies:
            if enemy.get_hp() == 0:
                defeated_enemy += 1
                del enemies[target_of_player]

        for play in players:
            if play.get_hp() == 0:
                defeated_players += 1

        # Check if player won
        if defeated_enemy == len(enemies):
            print(f'{bcolors.OKGREEN}You win!{bcolors.ENDC}')
            running = False
        # Check if enemy won
        elif defeated_players == len(players):
            print(f'{bcolors.FAIL}You Lose!{bcolors.ENDC}')
            running = False


    print("-" * 5)
    print(f'{bcolors.FAIL}ENEMY TURN{bcolors.ENDC}')
        # Enemy turn
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)
        target_of_enemy = random.randrange(0, len(players))
        enemy_dmg = enemy.generate_damage()

        if enemy_choice == 0:

            players[target_of_enemy].take_dmg(enemy_dmg)
            print(f'{bcolors.FAIL}{enemy.name}{bcolors.ENDC} deal {bcolors.FAIL}{enemy_dmg} dmg{bcolors.ENDC} to '
                  f'{bcolors.OKGREEN}{players[target_of_enemy].name}{bcolors.ENDC}')


        if enemy_choice == 1:
            print("magia")
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                before_hp = enemy.get_hp()
                enemy.heal(magic_dmg)
                after_hp = enemy.get_hp()
                print(f'{bcolors.FAIL}\n{spell.name}{bcolors.ENDC} heals {bcolors.FAIL}{enemy.name}{bcolors.ENDC} '
                      f'for {bcolors.FAIL}{str(magic_dmg)} HP{bcolors.ENDC}')
                print(f'Healed from {bcolors.FAIL}{before_hp}{bcolors.ENDC} to {bcolors.FAIL}{after_hp}{bcolors.ENDC}HP')
            elif spell.type == "black":
                players[target_of_enemy].take_dmg(magic_dmg)
                print(f'{bcolors.FAIL}{enemy.name}{bcolors.ENDC} attacked{bcolors.OKGREEN} {players[target_of_enemy].name}{bcolors.ENDC} '
                      f'for {bcolors.FAIL}{magic_dmg}{bcolors.ENDC} with {bcolors.FAIL}{spell.name} spell {bcolors.ENDC}')


            


