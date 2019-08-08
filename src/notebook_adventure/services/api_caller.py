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
    view = {'new_game':'scene1'}

    for i in range(0,10):
      orcs.append(factory.new_char('orc'+str(i), 20, 'm', 'Orc'))
    
    characters = {main_char.name:main_char, 
    sylva.name:sylva}
  
    for o in orcs:
      characters.update({o.name:o})
  
    ctx = factory.new_context('marley', characters, view)
    
    return ctx
  else:
    return {}
  
  #Should be
  #build requests client for contexts method
  #return serializer.de_serialize(requests.get(name))

def get_dialog(view):
  #STUB
  if view == 'new_game':
    return [
      'Part 1',
      '[Sylva (your guardian)]',
      'Prince, as you know, your parents recently died in the war saving our kingdom from the orc kingdom.',
      'Today you shall become the king/queen.',
      '[Narrator]',
      'As you walk the hall to the arena, several guards bow.',
      'You sit in the chair in your designated area to watch the fights.',
      'Guards on either side of you hold spears.',
      '[You]',
      'Thank you for coming on this day, today I will become the new human ruler.',
      'As you know, it is tradition to watch fights in the arena after the new ruler is crowned.',
      '[Narrator]',
      'You are crowned.',
      'The crowd cheers.',
      'The battle between a wizard and a very dangerous archer begins.',
      'After about four hours, the third round ends between a swordsman and a brain washing fifty year old .(The fifty year old wins)',
      'Everyone gets ready for the next round.',
      'Just then, an explosion happens on the right side of the arena.',
      'Dark green creatures come out of the damaged area filling the arena.',
      'The guards on your sides go and fight the things comming for you.',
      '[Sylva]',
      'Two soldiers there, one there GO GO GO!',
      'King/Queen!',
      '[Narrator]',
      'Two orcs jump in front of you.',
      'Sylva comes out of nowhere, rushing words out of her mouth.',
      '[Sylva]',
      'I got this one you get that one!',
      'FIGHT tutorial',
      'End of part l',
      'Part ll'
    ]
  elif view == 'fight_tutorial':
    return [
      'we fightin!!!!'
    ]
  #should be
  #return [_decompress(requests.get(view,dialog))]

def put_context(ctx):
  #s = serializer.serialize(ctx)
  #requests.put(s)
  return True

def _decompress(text):
  pass
