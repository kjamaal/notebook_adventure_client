from abc import ABC, abstractmethod

__all__ = "Character",

class Character(ABC):
  def __init__(self, name, age, gender, physical_attacks, magic_attacks, hp, md):
    self.name = name 
    self.age = age
    self.gender = gender
    self.physical_attacks = []
    self.magic_attacks = []
    self.hp = hp 
    self.md = md 
    super().__init__()
  
  @abstractmethod
  def attack(self, target, attack_obj): 
    pass

  @abstractmethod
  def heal(self, target, heal_obj):
    pass
