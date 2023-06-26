class knight:

    def __init__(self):
        self.class_name = "Knight"
        self.armor_type = 3
        self.armor_bonus = 10
        self.damage_bonus = 0
        self.hp_bonus = 100
        self.ranged = False

    def __str__(self):
        return "Knight is a heavy armored unit, who can stay longer in battlefield"

