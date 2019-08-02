'''A factory module to create concrete classes with data from the data model

'''
from ..services import api_caller
from ..data.classes import Human, Orc, Demon, Elf

def new_char(name,age,gender,cType):
  pAttacks = _get_attacks(cType)['physical']
  mAttacks = _get_attacks(cType)['magic']

  if cType == 'Human':
    return Human.Human(name,age,gender,pAttacks,mAttacks,10,10)
  elif cType == 'Orc':
    return Orc.Orc(name,age,gender,pAttacks,mAttacks,10,10)
  elif cType == 'Demon':
    return Demon.Demon(name,age,gender,pAttacks,mAttacks,10,10)
  elif cType == 'Elf':
    return Elf.Elf(name,age,gender,pAttacks,mAttacks,10,10)
  else:
    return Exception

def _get_attacks(char_type):
  return api_caller.get_attacks(char_type)
