from game.Character import Character
import random

enemy_1 = Character("Enemy_1", 1800, 65, 45, 25, [], [])
enemy_2 = Character("Enemy_2", 1000, 40, 100, 25, [], [])
enemy_3 = Character("Enemy_3", 1000, 20, 150, 0, [], [])


enemies = [enemy_1, enemy_2, enemy_3]
enemy_choice = random.randrange(0, 3)
print(enemy_choice)