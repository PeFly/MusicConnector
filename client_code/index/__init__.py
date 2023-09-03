from ._anvil_designer import indexTemplate
from anvil import *
import anvil.server

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
    alert("Enter wurde gedrückt", title="Debug", large=True)




