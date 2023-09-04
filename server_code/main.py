##### MUSIC CONNECTOR #####
# Translate music between streaming services
###########################


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