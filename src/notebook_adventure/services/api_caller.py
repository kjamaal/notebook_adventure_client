'''Service to make calls to the backend api.

'''

def get_attacks(char_type):
  if char_type == 'Human':
    return {'physical':['punch','kick'],'magic':['conjure','lightning']}
  elif char_type == 'Orc':
    return {'physical':['bite','scratch'],'magic':['push','hide']}
