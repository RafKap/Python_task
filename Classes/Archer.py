class archer:

    def __init__(self):
        self.class_name = "Archer"
        self.armor_type = 2
        self.armor_bonus = 5
        self.damage_bonus = 5
        self.hp_bonus = 50
        self.ranged = True

    def __str__(self):
        return "Archer is a long range warrior, who always hit first"

