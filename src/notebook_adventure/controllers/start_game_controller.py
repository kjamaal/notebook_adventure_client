from ..core import factory
from ..services import api_caller

def fetch_context(name):
  return api_caller.get_context(name)
    
