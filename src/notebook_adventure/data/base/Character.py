

class Character:
  def __init__(self, name, age, gender, physical_attacks, magic_attacks, hp, md):
    self.name = name 
    self.age = age
    self.gender = gender
    self.physical_attacks = physical_attacks
    self.magic_attacks = magic_attacks
    self.hp = hp 
    self.md = md 

  def attack(self, target, attack_type, attack_name): 
    if attack_type == 'physical':
      print('I\'m attacking you and taking strength with '+ attack_name)
    else:
      print('I\'m attacking you and taking magic defense (constitution?) with '+ attack_name)
