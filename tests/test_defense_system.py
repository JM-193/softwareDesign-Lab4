import unittest
from unittest.mock import MagicMock
from src.app.combat_system import CombatSystem
from src.models.character import Character
from src.models.sword import Sword
from src.models.bow import Bow
from src.models.battle_axe import BattleAxe
from src.app.defense_calculator import StandardDefenseCalculator, PercentageDefenseCalculator

class TestDefenseSystem(unittest.TestCase):

    def test_standard_defense_calculator_reduces_damage(self):
        """Test que StandardDefenseCalculator reduce el daño en una cantidad fija"""

        # Test with base damage, no crit
        mock_dmg_calc = MagicMock()
        mock_dmg_calc.check_critical_hit.return_value = False

        combat = CombatSystem(mock_dmg_calc,
                              StandardDefenseCalculator())
        hero = Character("Hero")

        # Enemy with default armor of 25
        enemy_1 = Character("Enemy1")
        # Enemy with armor of 5
        enemy_2 = Character("Enemy2", initial_armor = 5)

        # Let's use a Bow, the bow has 12 damage
        bow = Bow()

        combat.perform_attack(hero, bow, enemy_1)
        combat.perform_attack(hero, bow, enemy_2)

        # The firs enemy has more armor than the bow damage,
        # so it should only take 1 damage
        self.assertEqual(enemy_1.health, 99)

        # The second enemy has 5 armor, so it should take 7 damage (12 - 5)
        self.assertEqual(enemy_2.health, 93)

    def test_percentage_defense_calculator_reduces_damage(self):
        """Test que PercentageDefenseCalculator reduce el daño en un porcentaje"""

        # Test with base damage, no crit
        mock_dmg_calc = MagicMock()
        mock_dmg_calc.check_critical_hit.return_value = False

        combat = CombatSystem(mock_dmg_calc,
                              PercentageDefenseCalculator())
        hero = Character("Hero")

        # Enemy with default armor of 25
        enemy_1 = Character("Enemy1")

        # Let's use a Sword, the sword has 15 damage
        sword = Sword()

        combat.perform_attack(hero, sword, enemy_1)

        # Since the enemy has 25% damage reduction from their 25 points of armor,
        # they should take 15 * (1 - 0.25) = 11.25 -> 11 damage
        self.assertEqual(enemy_1.health, 89)

    def test_negative_flat_armor_increases_damage(self):
        """Test que el armor negativo en StandardDefenseCalculator aumenta el daño"""

        # Test with base damage, no crit
        mock_dmg_calc = MagicMock()
        mock_dmg_calc.check_critical_hit.return_value = False

        combat = CombatSystem(mock_dmg_calc,
                              StandardDefenseCalculator())
        hero = Character("Hero")

        # Enemy with negative armor of -5
        enemy = Character("Enemy", initial_armor = -8)

        # Let's use a Bow again, the bow has 12 damage
        bow = Bow()

        combat.perform_attack(hero, bow, enemy)

        # The enemy has -8 armor, so it should take 12 - (-8) = 20 damage
        self.assertEqual(enemy.health, 80)

    def test_negative_percentage_armor_increases_damage(self):
        """Test que el armor negativo en PercentageDefenseCalculator aumenta el daño"""

        # Test with base damage, no crit
        mock_dmg_calc = MagicMock()
        mock_dmg_calc.check_critical_hit.return_value = False

        combat = CombatSystem(mock_dmg_calc,
                              PercentageDefenseCalculator())
        hero = Character("Hero")

        # Enemy with negative armor of -20
        enemy = Character("Enemy", initial_armor = -20)

        # Let's use a Sword again, the sword has 15 damage
        sword = Sword()

        combat.perform_attack(hero, sword, enemy)

        # The enemy has -20 armor, so it should take 15 * (1 - (-0.20)) = 18 damage
        self.assertEqual(enemy.health, 82)

    def test_battle_axe_reduces_enemy_armor(self):
        """Test que BattleAxe reduce el armor del enemigo al atacar"""

        # Test with base damage, no crit
        mock_dmg_calc = MagicMock()
        mock_dmg_calc.check_critical_hit.return_value = False

        combat = CombatSystem(mock_dmg_calc,
                              StandardDefenseCalculator())
        hero = Character("Hero")

        # Enemy with 15 armor
        enemy = Character("Enemy", initial_armor = 15)

        # We're testing the BattleAxe, which has 20 dmg and recudes armor by 5
        battle_axe = BattleAxe()

        # Perform the first attack
        combat.perform_attack(hero, battle_axe, enemy)

        # After this first attack, the enemy should've only taken 20 - 15 = 5 damage
        # and its armor should be reduced by 5
        self.assertEqual(enemy.health, 95)
        self.assertEqual(enemy.armor, 10)

        # Perform a second attack
        combat.perform_attack(hero, battle_axe, enemy)

        # Now the enemy should take 20 - 10 = 10 damage
        # and its armor should be reduced by another 5
        self.assertEqual(enemy.health, 85)
        self.assertEqual(enemy.armor, 5)
