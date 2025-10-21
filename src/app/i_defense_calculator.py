from abc import ABC, abstractmethod

class IDefenseCalculator(ABC):
    @abstractmethod
    def calculate_damage_after_defense(self, damage, defender):
        """Calculates the damage after applying defender's defense stats"""
        pass
