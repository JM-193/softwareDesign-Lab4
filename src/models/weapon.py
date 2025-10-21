from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, attacker, target) -> int:
        """
        Return the damage dealt by the weapon

        Any other effects such as buffs or debuffs
        should be handled before returning.
        """
        pass
