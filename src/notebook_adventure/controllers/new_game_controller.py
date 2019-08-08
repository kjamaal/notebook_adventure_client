from ..core import factory
from ..services import api_caller

def get_dialog():
  return api_caller.get_dialog('new_game')

def put_context(ctx):
  api_caller.put_context(ctx)
