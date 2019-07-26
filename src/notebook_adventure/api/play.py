""" Implement the hello command.

"""
from ..core.logger import logger
from ..core.formatter import scroll_output
import sys

stdin_ = sys.__stdin__
sys.stdin = stdin_

def main(name):
    """ Execute the command.
    
    :param name: name of saved game to play
    """
    logger.debug("Starting a game")

    def play_intro():
      scroll_output(['\033[1;33;40mHello there. Let\'s play a game.'],{'print_by' : 'char','sec_delay': .1})
    
    def play_game():
      output = input('\033[0;37;40mWould you like to play? (y/n): ')
      if output == 'y':
        script = [
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
          'Part ll',
        ]           
      

        scroll_output(script,{'print_by':'line','sec_delay':2})

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
