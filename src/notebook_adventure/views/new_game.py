from ..controllers import new_game_controller
from ..core import formatter
from . import fight_tutorial
import sys

stdin_ = sys.__stdin__
sys.stdin = stdin_

def play(ctx):
  formatter.scroll_output(new_game_controller.get_dialog(),{'print_by':'line','sec_delay':2}) 
  ctx.view.clear()
  ctx.view.update({'fight_tutorial':'scene1'})
  new_game_controller.put_context(ctx)
  getattr(globals()[list(ctx.view.keys())[0]], 'play')(ctx)
      