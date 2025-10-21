import unittest
from unittest.mock import MagicMock
from src.app.combat_system import CombatSystem
from src.models.character import Character
from src.models.weapon import Weapon
from src.app.defense_calculator import NoDefenseCalculator
from tests.mocked_models.dummy_weapon import DummyWeapon

class TestDummyWeapon(unittest.TestCase):

    def test_dummy_weapon_in_combat_system(self):
        """Test que CombatSystem acepta DummyWeapon como Weapon válida"""
        mock_calculator = MagicMock()
        mock_calculator.check_critical_hit.return_value = True

        # Defense was irrelevant to this test, so we use NoDefenseCalculator
        combat = CombatSystem(mock_calculator, NoDefenseCalculator())
        hero = Character("Hero")
        enemy = Character("Enemy")
        dummy_weapon = DummyWeapon()

        # CombatSystem debe tratar a DummyWeapon como cualquier Weapon
        result = combat.perform_attack(hero, dummy_weapon, enemy)

        # Verificamos que se comporta como un Weapon en el sistema
        self.assertIn("arma dummy", result)
        self.assertIn("GOLPE CRÍTICO", result)
        self.assertEqual(enemy.health, 90)  # Solo daño crítico
        mock_calculator.check_critical_hit.assert_called_once()
