from ..base.Character import Character

__all__ = 'Demon',

class Demon(Character):
  def __init__(self, name, age, gender):
    self.physical_attacks = ['punch','kick']
    self.magic_attacks = ['attack1','attack2']
    self.hp = 10
    self.md = 10
    Character.__init__(self, name, age, gender, self.physical_attacks, self.magic_attacks, self.hp, self.md)
