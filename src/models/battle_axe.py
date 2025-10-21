from src.models.weapon import Weapon

class BattleAxe(Weapon):
    def __init__(self):
        super().__init__("hacha de batalla")

    def attack(self, attacker, target):
        """
        Return the damage dealt by the weapon

        Any other effects such as buffs or debuffs
        should be handled before returning.
        """

        # The battle axe reduces the target's armor by 5 points on each hit
        # Note: Armor could be negative to give extra damage,
        # each defense system should check if armor is outside its  own boundaries
        target.armor -= 5

        # Battle axe has a fixed damage of 20
        return 20
