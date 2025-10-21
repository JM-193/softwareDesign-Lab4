from abc import ABC, abstractmethod

class IDefenseCalculator(ABC):
    @abstractmethod
    def calculate_damage_after_defense(self, damage, target):
        """Calculates the damage after applying the target's defense stats"""
        pass # pragma: no cover
