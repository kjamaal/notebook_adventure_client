from ..services import api_caller

def put_context(ctx):
  api_caller.put_context(ctx)

def get_dialog():
  return api_caller.get_dialog('fight')
