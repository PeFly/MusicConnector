from ._anvil_designer import indexTemplate
from anvil import *
import anvil.server

import re

class index(indexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def check_input(self):
    link_regex = r'https://open\.spotify\.com/(intl-[a-z]{2}/)?(track|album|artist|playlist)/([a-zA-Z0-9]+)'
    regex_match = re.match(link_regex, self.link_submit.text)
    if regex_match:
      print(f"{self.link_input.text} matches {link_regex}")
      return True
    else:
      print(f"{self.link_input.text} not matches {link_regex}")
      self.link_input.role = "outlined-error"
      return False

  def link_input_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if self.check_input():
      open_form('result')

  def link_input_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.check_input():
      self.link_submit.visible = True

  def link_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.check_input():
      open_form('result')







