class Character:
    def __init__(self, name):
        self.name = name
        self.health_points = 100
        self.attack_damage = 10

    def basic_attack(self, target):
        target.health_points -= self.attack_damage
        print(f'{self.name} attacked {target.name} for {self.attack_damage} attack damage')