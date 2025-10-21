from src.models.weapon import Weapon

class BattleAxe(Weapon):
    def __init__(self):
        super().__init__(name = "hacha de batalla",
                         damage = 20)

    def apply_post_attack_effects(self, attacker, target):
        """
        Apply armor reduction after the attack is executed.

        The battle axe reduces the target's armor by 5 points on each hit.

        Note: Armor could become negative, check if that's okay to you.
        """
        target.armor -= 5
