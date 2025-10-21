import unittest
from unittest.mock import MagicMock
from src.app.combat_system import CombatSystem
from src.models.character import Character
from src.models.sword import Sword
from src.app.defense_calculator import *

class TestMiscellaneous(unittest.TestCase):

    def test_character_cannot_kill_dead_enemy(self):
        """Test que un personaje no puede atacar a un enemigo ya muerto"""
        mock_dmg_calc = MagicMock()
        mock_dmg_calc.check_critical_hit.return_value = False

        combat = CombatSystem(mock_dmg_calc, NoDefenseCalculator())
        hero = Character("Hero")
        enemy = Character("Enemy")
        enemy.take_damage(enemy.health)  # Matar al enemigo
        sword = Sword()

        result = combat.perform_attack(hero, sword, enemy)

        # Health should remain 0 and a message should indicate the enemy is already dead
        self.assertIn("ya está derrotado", result)
        self.assertEqual(enemy.health, 0)
