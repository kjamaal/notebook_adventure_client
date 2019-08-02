'''Service to make calls to the backend api.

'''

def get_attacks(char_type):
  '''Call to the backend to get the list of attacks

  '''
  #Here's a stub of data. Will replace will call responses
  if char_type == 'Human':
    return {'physical':['punch','kick'],'magic':['conjure','lightning']}
  elif char_type == 'Orc':
    return {'physical':['bite','scratch'],'magic':['push','hide']}
  elif char_type == 'Demon':
    return {}
  elif char_type == 'Elf':
    return {}
