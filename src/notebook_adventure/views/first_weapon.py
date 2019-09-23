from ..controllers import first_weapon_controller
from ..core import formatter

def play(ctx):
  d = first_weapon_controller.get_dialog()
  formatter.scroll_output(d)
    