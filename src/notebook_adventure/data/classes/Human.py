from ..base import Character

class Human(Character):
  def __init__(self, name, age, gender, physical_attacks, magic_attacks, hp, md):
    Character.__init__(self, name, age, gender, physical_attacks, magic_attacks, hp, md)

  def attack(self, target, attack_type, attack_name):
    Character.attack(self, target, attack_type, attack_name)
