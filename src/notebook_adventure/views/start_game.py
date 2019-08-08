from ..controllers import start_game_controller
from ..core import formatter
from . import new_game, fight_tutorial
import sys

stdin_ = sys.__stdin__
sys.stdin = stdin_

def play(name):
  ctx = start_game_controller.fetch_context(name)
  if ctx:    
    getattr(globals()[list(ctx.view.keys())[0]], 'play')(ctx)
  else:
    formatter.scroll_output('ain\'t no game by that name')
