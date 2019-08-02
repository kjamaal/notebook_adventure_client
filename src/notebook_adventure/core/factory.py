'''A factory module to create concrete classes with data from the data model

'''
from ..services import api_caller
from ..data.classes import Human

def new_human(name,age,gender):
  pAttacks = _get_attacks('Human')['physical']
  mAttacks = _get_attacks('Human')['magic']
  return Human.Human(name,age,gender,pAttacks,mAttacks,10,10)

def _get_attacks(char_type):
  return api_caller.get_attacks(char_type)
