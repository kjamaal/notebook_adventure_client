from ..base.Character import Character

__all__ = 'Elf',

class Elf(Character):
  def __init__(self, name, age, gender, physical_attacks, magic_attacks, hp, md):
    Character.__init__(self, name, age, gender, physical_attacks, magic_attacks, hp, md)

  def attack(self, target, attack_obj):
    pass

  def heal(self, target, amount, type):
    pass
