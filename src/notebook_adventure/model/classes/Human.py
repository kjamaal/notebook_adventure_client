from ..base.Character import Character

__all__ = 'Human',

class Human(Character):
  def __init__(self, name, age, gender, physical_attacks, magic_attacks, hp, md):
    Character.__init__(self, name, age, gender, physical_attacks, magic_attacks, hp, md)

  def attack(self, target_obj, attack_obj):
    return [
      'I\'m attacking with type '+attack_obj.aType,
      'taking '+str(attack_obj.damage)+' of damage from '+target_obj.name,
      'who is a(n) '+target_obj.__class__.__name__
    ]
  
  def heal(self, target, amount, type):
    pass 
