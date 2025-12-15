from api_helper import ClientWrapper
from constants import *
import json
import os

needs_url = False
needs_token = False
needs_file = False

if not os.path.exists(CONFIG_PATH):
    needs_url = True
    needs_token = True
    needs_file = True

try:
    config = json.load(CONFIG_PATH)
except json.decoder.JSONDecodeError:
    needs_url = True
    needs_token = True
    needs_file = True



api = ClientWrapper()