from src.models.weapon import Weapon

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="espada")

    def attack(self, attacker, target):
        """
        Return the damage dealt by the weapon

        Any other effects such as buffs or debuffs
        should be handled before returning.
        """

        # Sword has a fixed damage of 15
        return 15
