""" Implement the play command.

"""
from ..core.logger import logger
#from ..core.formatter import scroll_output
#from ..core import factory
from ..views import start_game
import sys

stdin_ = sys.__stdin__
sys.stdin = stdin_

def main(name):
    """ start a game.
    
    :param name: name of saved game to play
    """
    logger.debug("Starting game. name: "+name)
    start_game.play(name)

    ''' Attack sequence snippet
      from ..model.classes import Human, Orc, Demon, Physical_attack, Magic_attack
      attack_obj = Physical_attack.Physical_attack('punch','physical',10)
      orc = Orc.Orc('orcface',20,'m',['bite','scratch'],['push','hide'],10,10)
      scroll_output(human_ruler.attack(orc,attack_obj),{'print_by':'char','sec_delay':.1})
    '''

    return 0
