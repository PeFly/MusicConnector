from ._anvil_designer import resultTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.js.window import localStorage

class result(resultTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def index_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('index')

  def spotify_click(self, **event_args):
    link_data = localStorage.get('last_request', {})
    print(link_data)

