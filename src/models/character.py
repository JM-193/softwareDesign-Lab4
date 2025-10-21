class Character:
    def __init__(self, name, health=100, initial_armor=25):
        self.name = name
        self.health = health
        self.is_alive = True
        self.initial_armor = initial_armor
        # Armor can vary during combat via buffs/debuffs
        self.armor = initial_armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False

    def heal(self, amount):
        if self.is_alive:
            self.health += amount

    def restore_armor(self):
        if self.is_alive and self.armor < self.initial_armor:
            # Only restore armor when debuffed
            self.armor = self.initial_armor
