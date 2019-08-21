from ..controllers import the_forest_controller
from ..core import formatter

def play(ctx):
  d = the_forest_controller.get_dialog()
  formatter.scroll_output(d)
  ctx.view.clear()
  ctx.view.update({'the_forest':'scene1'})
  the_forest_controller.put_context(ctx)
  getattr(list(ctx.view.keys())[0],'play')(ctx)
