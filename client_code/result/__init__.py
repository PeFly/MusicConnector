from ._anvil_designer import resultTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.server

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
    anvil.server.call('spotify_get_link_information')

