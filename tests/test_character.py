import unittest
from src.models.character import Character

class TestCharacter(unittest.TestCase):

    def test_character_starts_alive_with_full_health(self):
        """Test que un personaje nuevo tiene salud completa y está vivo"""
        warrior = Character("Conan")
        self.assertEqual(warrior.health, 100)
        self.assertTrue(warrior.is_alive)

    def test_take_damage_reduces_health_and_can_kill(self):
        """Test que el daño reduce salud y puede matar al personaje"""
        mage = Character("Gandalf")
        mage.take_damage(30)
        self.assertEqual(mage.health, 70)

        mage.take_damage(70)
        self.assertFalse(mage.is_alive)

    def test_heal_increases_health(self):
        """Test que la curación aumenta la salud"""
        rogue = Character("Garrett")
        rogue.take_damage(50)
        rogue.heal(30)
        self.assertEqual(rogue.health, 80)

    def test_restore_armor_resets_armor_only_when_armor_is_less_than_initial_value(self):
        """Test que restaurar la armadura la reinicia a su valor inicial, solo si es menor que el valor inicial"""
        # Tiene 25 de armadura inicial por defecto
        paladin = Character("Uther")

        # Aumentamos la armadura
        paladin.armor = 50
        paladin.restore_armor()
        self.assertEqual(paladin.armor, 50)  # No debería cambiar

        # Disminuimos la armadura
        paladin.armor = 10
        paladin.restore_armor()
        self.assertEqual(paladin.armor, 25)  # Debería restaurarse al valor inicial
