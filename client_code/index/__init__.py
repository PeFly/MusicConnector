from ._anvil_designer import indexTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server
from anvil.js.window import localStorage

class index(indexTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def go_to_index(self, **event_args):
    anvil.server.call('spotify_get_link_information', self.link_input.text)
    open_form('result')
  
  def link_input_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if anvil.server.call('check_input', self.link_input.text):
      self.go_to_index()
    else:
      self.link_input.role = "outlined-error"
      alert(f"{self.link_input.text} is no valid link", title="Invalid link")

  def link_input_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    with anvil.server.no_loading_indicator:
      if anvil.server.call('check_input', self.link_input.text):
        self.link_input.role = "input-valid"
        self.link_submit.visible = True
      elif self.link_input.text == "":
        self.link_input.role = "outlined"
        self.link_submit.visible = False
      else:
        self.link_input.role = "outlined-error"
        self.link_submit.visible = False

  def link_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.go_to_index()







