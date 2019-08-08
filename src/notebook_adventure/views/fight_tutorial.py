from ..controllers import fight_tutorial_controller
from ..core import formatter
from . import fight

def play(ctx):
  d = fight_tutorial_controller.get_dialog()
  formatter.clear_screen()
  formatter.scroll_output(d)
  ctx.view.clear()
  ctx.view.update({'fight':'scene1'})
  fight_tutorial_controller.put_context(ctx)
  getattr(list(ctx.view.keys())[0],'play')(ctx)
