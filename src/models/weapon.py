from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name: str, damage: int):
        self._name = name
        self._damage = damage

    @property
    def name(self) -> str:
        """Return the name of the weapon"""
        return self._name

    def attack(self) -> int:
        """Return the damage dealt by the weapon"""
        return self._damage

    def apply_post_attack_effects(self, attacker, target):
        """
        Apply any post-attack effects such as
        buffs for the attacker or debuffs for the target.

        Override this method in subclasses if needed.

        Does nothing by default.
        """
        pass
