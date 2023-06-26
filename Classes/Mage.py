class mage:

    def __init__(self):
        self.class_name = "Mage"
        self.armor_type = 1
        self.armor_bonus = 0
        self.damage_bonus = 10
        self.hp_bonus = 0
        self.ranged = True

    def __str__(self):
        return "Mage is a mage. He can do spells"

