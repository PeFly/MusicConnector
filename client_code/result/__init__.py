from ._anvil_designer import resultTemplate
from anvil import *
import anvil.server
from .. import global_vars
import json

class result(resultTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    global link
    self.link = global_vars.link
    self.init_components(**properties)
    self.link_response = anvil.server.call('spotify_get_link_information', self.link)
    self.id_response = anvil.server.call('spotify_get_id_data', self.link_response[0], self.link_response[1])
    # Any code you write here will run before the form opens.

  # def get_lnik_informations(self):
    # self.link_response = anvil.server.call('spotify_get_link_information', self.link)

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def index_click(self, **event_args):
    """This method is called when the button is clicked"""
    global link_response
    global_vars.link_response = ""
    open_form('index')

  def spotify_click(self, **event_args):
    self.output_label.text = self.id_response
    self.output_label.visible = True

