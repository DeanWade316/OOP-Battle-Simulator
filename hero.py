import random

class Hero:
    """A playable character who battles enemies in the arena."""

    def __init__(self, name):
        self.name = name
        self.health = 115
        self.attack_power = 15
        self.hero_class = "Ranger"

    def attack(self):
        """Return a random amount of damage."""
        return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
        """Reduce health without allowing it to fall below zero."""
        self.health = max(0, self.health - damage)
        print(str(self.name) + "takes " + str(damage) + " damge. Health: " + str(self.health))
    
    def is_alive(self):
        """Return True while the hero has health remaining."""
        return self.health > 0