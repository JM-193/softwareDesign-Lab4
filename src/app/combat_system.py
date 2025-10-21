from src.app.i_combat_system import ICombatSystem

class CombatSystem(ICombatSystem):
    def __init__(self, damage_calculator, defense_calculator):
        self.damage_calculator = damage_calculator
        self.defense_calculator = defense_calculator

    def perform_attack(self, attacker, weapon, target):
        # Check if the target is alive
        if not target.is_alive:
            return f"{target.name} ya está derrotado"

        # Get the base damage for the attack
        base_damage = weapon.attack(attacker, target)
        final_damage = base_damage

        # Calcule crit damage
        critical_hit_text = ""
        if self.damage_calculator.check_critical_hit():
            final_damage *= .5
            critical_hit_text = " (¡Golpe crítico!)"

        # Apply defense reduction
        final_damage = self.defense_calculator.calculate_damage_after_defense(final_damage, target)

        # Apply damage to the target
        target.take_damage(final_damage)

        return f"{attacker.name} ataca a {target.name} con {weapon.name}, causando {final_damage} de daño.{critical_hit_text}"
