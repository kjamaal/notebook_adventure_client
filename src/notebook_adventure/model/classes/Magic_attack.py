from ..base.Attack import Attack

class Magic_attack(Attack):
  def __init__(self, name, aType, damage):
    self.target_member = 'md'
    Attack.__init__(self, name, aType, damage)
    