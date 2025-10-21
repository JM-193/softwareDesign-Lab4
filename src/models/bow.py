from src.models.weapon import Weapon

class Bow(Weapon):
    """
    Class representing a bow weapon.

    The bow has a fixed damage of 12.
    """
    def __init__(self):
        super().__init__(name = "arco",
                         damage = 12)
