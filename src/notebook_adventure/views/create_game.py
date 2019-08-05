from ..controllers import create_game_controller
from ..core import formatter
import sys

stdin_ = sys.__stdin__
sys.stdin = stdin_

def play(name):
  player_name = input('What\'s your name?: ')
  player_age = input('How old are you?: ')
  player_gender = input('what gender are you?: ')
  ctx = create_game_controller.create_context(name, player_name, player_age, player_gender, 'Human')
