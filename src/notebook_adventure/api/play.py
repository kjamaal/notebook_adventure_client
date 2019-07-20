""" Implement the hello command.

"""
from ..core.logger import logger
import sys


def main(name):
    """ Execute the command.
    
    :param name: name of saved game to play
    """
    logger.debug("Starting a game")
    stdout_ = sys.__stdout__
    sys.stdout = stdout_
    stdin_ = sys.__stdin__
    sys.stdin = stdin_


    def play_intro():
      print('''
        Hello there. Let's play a game.
      ''')
      return 0
    
    def play_game():
      output = input('Would you like to play? (y/n): ')
      if output == 'y':
        script = [
          'this is sentence one',
          'this is sentence two',
          'and a third sentence'
        ]

        for s in script:
          print(s)

    def _is_new():
      return True

    def _check_for_game():
      """ Make sure this saved game exists
      
      """
      return True

    if _check_for_game() and _is_new():
      play_intro()
      play_game()
    elif _is_new():
      play_game()
    else:
      print('Make a new game suckah')
    
    return 0
