from ._anvil_designer import indexTemplate
from anvil import *
import anvil.server

import re

class index(indexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def link_input_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if self.link_input.text:
      open_form('result')

  def link_input_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.link_submit.visible = True

  def link_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.link_input.text:
      open_form('result')







