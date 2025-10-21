from src.models.weapon import Weapon

class MagicStaff(Weapon):
    def __init__(self):
        super().__init__(name = "báculo mágico",
                         damage = 10)

    def apply_post_attack_effects(self, attacker, target):
        """
        Apply a burning effect after the attack is executed.

        The magic staff heals the user for 5 health points on each hit.
        """
        attacker.heal(5)
