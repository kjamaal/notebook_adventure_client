from ..controllers import fight_controller
from ..core import formatter

def play(ctx):
  d = fight_controller.get_dialog()
  formatter.scroll_output(d)
