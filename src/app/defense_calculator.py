from src.app.i_defense_calculator import IDefenseCalculator

class StandardDefenseCalculator(IDefenseCalculator):
    """
    Standard damage reduction based on target's armor.

    Each point of armor reduces damage by 1 point.

    Negative armor increases damage
    """

    def calculate_damage_after_defense(self, damage, target):
        """Calculates the damage after applying defender's defense stats"""

        # Check if target has 'armor' attribute
        if not hasattr(target, 'armor'):
            raise AttributeError("Target has no 'armor' attribute. Add one or use the NoDefenseCalculator.")

        reduced_damage = damage - target.armor

        # Ensure at least 1 damage is dealt as to not make opponents OP
        return max(1, reduced_damage)

class PercentageDefenseCalculator(IDefenseCalculator):
    """
    Percentage-based damage reduction based on target's armor.

    Each point of armor reduces damage by 1%.

    Negative armor increases damage taken.
    """
    def calculate_damage_after_defense(self, damage, target):
        """Calculates the damage after applying defender's defense stats"""

        # Check if target has 'armor' attribute
        if not hasattr(target, 'armor'):
            raise AttributeError("Target has no 'armor' attribute. Add one or use the NoDefenseCalculator.")

        # Percentage is capped between -100% and 100% to avoid extreme cases
        armor_points = min(max(target.armor, -100), 100)

        # Calculate reduction
        reduction_percentage = armor_points / 100.0
        reduced_damage = damage * (1 - reduction_percentage)

        # Ensure at least 1 damage is dealt as to not make opponents OP
        return max(1, int(reduced_damage))

class NoDefenseCalculator(IDefenseCalculator):
    """ No damage reduction applied. Full damage is always dealt. """
    def calculate_damage_after_defense(self, damage, target):
        """Returns the original damage without any reduction"""
        return damage
