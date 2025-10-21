from src.models.weapon import Weapon

class Bow(Weapon):
    def __init__(self):
        super().__init__("arco")

    def attack(self, attacker, target):
        """
        Return the damage dealt by the weapon

        Any other effects such as buffs or debuffs
        should be handled before returning.
        """

        # Bow has a fixed damage of 12
        return 12
