from typing import Dict

class Context():
  def __init__(self, name:str, characters:Dict[str, object], view:Dict[str, str]):
    self.name = name
    self.characters = characters
    self.view = view
