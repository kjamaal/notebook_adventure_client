from ..core import factory
from ..services import api_caller

def create_context(game_name, name, age, gender, cType):
  main_char = factory.new_char(name, age, gender, cType)
  sylva = factory.new_char('sylva', 40, 'm', 'Human')
  orcs = []
  view = {'new_game':'scene1'}
  
  for i in range(0,10):
    orcs.append(factory.new_char('orc'+i, 20, 'm', 'Orc'))
  
  characters = {main_char.name:main_char, 
  sylva.name:sylva}

  for o in orcs:
    characters.update({o.name:o})

  ctx = factory.new_context(game_name, characters, view)
  api_caller.put_context(ctx)
  
  return ctx 
