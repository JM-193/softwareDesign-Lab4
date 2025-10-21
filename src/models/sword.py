from src.models.weapon import Weapon

class Sword(Weapon):
    """"
    Class representing a sword weapon.

    The sword has a fixed damage of 15.
    """
    def __init__(self):
        super().__init__(name = "espada",
                         damage = 15)
