import unittest
from unittest.mock import MagicMock
from src.app.combat_system import CombatSystem
from src.models.character import Character
from src.models.sword import Sword
from src.models.magic_staff import MagicStaff
from src.app.defense_calculator import *

class TestCombatSystem(unittest.TestCase):

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

    def test_magic_staff_heals_user(self):
        """Test que el bastón mágico cura al usuario en lugar de dañar al enemigo"""
        mock_dmg_calc = MagicMock()
        mock_dmg_calc.check_critical_hit.return_value = False

        combat = CombatSystem(mock_dmg_calc, NoDefenseCalculator())
        hero = Character("Hero")
        enemy = Character("Enemy")
        magic_staff = MagicStaff()

        hero.take_damage(5)  # Hero takes some damage first
        self.assertEqual(hero.health, 95)

        combat.perform_attack(hero, magic_staff, enemy)

        # Hero should be healed by 5 points
        self.assertEqual(hero.health, 100)
