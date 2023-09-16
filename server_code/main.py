##### MUSIC CONNECTOR #####
# Translate music between streaming services
###########################


import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
import anvil.http



##### MODULES #####
import anvil.server
import re


##### CLIENT CALLABLE #####
@anvil.server.callable
def check_input(input_link):
  link_regex = r'https://open\.spotify\.com/(intl-[a-z]{2}/)?(track|album|artist|playlist)/([a-zA-Z0-9]+)'
  if re.match(link_regex, input_link):
    return True
  else:
    return False