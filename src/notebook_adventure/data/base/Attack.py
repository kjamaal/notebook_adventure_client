from abc import ABC, abstractmethod

class Attack(ABC):
  def __init__(self, name, aType, damage):
    self.name = name
    self.aType = aType
    self.damage = damage
    super().__init__()
