from ..controllers import start_game_controller
from ..core import formatter
#from ..model.classes import Human, Orc, Demon, Physical_attack, Magic_attack
import sys

stdin_ = sys.__stdin__
sys.stdin = stdin_
views = sys.modules[__name__]

def play(name):
  ctx = start_game_controller.fetch_context(name)
  if ctx:
    getattr(views, ctx.view).play(ctx)
  else:
    formatter.scroll_output('ain\'t no game by that name',{'print_by':'char','sec_delay':.1})
