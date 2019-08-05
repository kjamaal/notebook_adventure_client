'''Service to make calls to the backend api.

'''
from ..core import serializer
from ..core import factory
import requests

def get_attacks(char_type):
  '''Call to the backend to get the list of attacks

  '''
  #Here's a stub of data. Will replace with api call responses
  if char_type == 'Human':
    return {'physical':['punch','kick'],'magic':['conjure','lightning']}
  elif char_type == 'Orc':
    return {'physical':['bite','scratch'],'magic':['push','hide']}
  elif char_type == 'Demon':
    return {}
  elif char_type == 'Elf':
    return {}
  
  #should be
  #Build requests client for attacks method
  #return serializer.de-serialize(requests.get(char_type))

def get_context(name):
  #Stubbing our calls
  if name == 'marley':
    main_char = factory.new_char('Marley', 11, 'm', 'Human')
    sylva = factory.new_char('sylva', 40, 'm', 'Human')
    orcs = []
    
    for i in range(0,10):
      orcs.append(factory.new_char('orc'+str(i), 20, 'm', 'Orc'))
    
    characters = {main_char.name:main_char, 
    sylva.name:sylva}
  
    for o in orcs:
      characters.update({o.name:o})
  
    ctx = factory.new_context('marley', characters, 'new_game')
    
    return ctx
  else:
    return {}
  
  #Should be
  #build requests client for contexts method
  #return serializer.de_serialize(requests.get(name))

def put_context(ctx):
  #s = serializer.serialize(ctx)
  #requests.put(s)
  return True
