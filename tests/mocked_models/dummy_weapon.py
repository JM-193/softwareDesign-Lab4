from src.models.weapon import Weapon

class DummyWeapon(Weapon):
    """Arma dummy para testing que no hace daño real"""
    def __init__(self):
        super().__init__(name="arma dummy")

    def attack(self, attacker, target) -> int:
        """
        Return the damage dealt by the weapon

        Any other effects such as buffs or debuffs
        should be handled before returning.
        """

        # Dummy weapon does no damage
        return 0
