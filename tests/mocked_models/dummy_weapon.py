from src.models.weapon import Weapon

class DummyWeapon(Weapon):
    """Arma dummy para testing que no hace daño real"""
    def __init__(self):
        super().__init__(name = "arma dummy",
                         damage = 0)
