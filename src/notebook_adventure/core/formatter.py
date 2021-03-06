'''formatting helpers for output

'''
from time import sleep
from os import system, name
import sys

__all__ = "scroll_output",

config = {
  'print_by' : 'line',
  'sec_delay': 1,
}

stdout_ = sys.__stdout__
sys.stdout = stdout_

def scroll_output(output, config=config):
  '''set the speed and sequence of output to stdout

  :param name: output to scroll (must be a list of strings)
  :param name: config dict
  '''
  for line in output:
    if config['print_by'] == 'line':
      print('\n   '+line)
      sleep(config['sec_delay'])
    else:
      last = line[-1:]
      for char in line[:-1]:
        print(char,end='')
        sys.stdout.flush()
        sleep(config['sec_delay'])
      print(last)

def clear_screen():
  if name == 'nt': 
    _ = system('cls') 
  
  # for mac and linux(here, os.name is 'posix') 
  else: 
    _ = system('clear') 
