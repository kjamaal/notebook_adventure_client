from ..base.Attack import Attack

class Physical_attack(Attack):
  def __init__(self, name, aType, damage):
    self.target_member = 'hp'
    Attack.__init__(self, name, aType, damage)
    