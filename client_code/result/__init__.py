from ._anvil_designer import resultTemplate
from anvil import *
import anvil.server
from .. import global_vars
import json

class result(resultTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    with anvil.server.no_loading_indicator:
      global link
      self.link = global_vars.link
      self.link_response = anvil.server.call('spotify_get_link_information', self.link)
      self.id_response = anvil.server.call('spotify_get_id_data', self.link_response[0], self.link_response[1])

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def index_click(self, **event_args):
    """This method is called when the button is clicked"""
    global link_response
    global_vars.link_response = ""
    open_form('index')

  def spotify_click(self, **event_args):
    if self.output_label.visible == False:
      self.output_label.text = self.id_response
      album_data = self.id_response.get('album', {})
      images_list = album_data.get('images', [])
      first_image_url = images_list[0].get('url', '')
      self.artist_image.source = first_image_url
      self.output_label.visible = True
      self.artist_image.visible = True
    else:
      self.output_label.visible = False
      self.artist_image.visible = False
      

