import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), '.env'))

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
USERNAME = os.environ.get('USR')
PASSWORD = os.environ.get('PASSWORD')
USER_AGENT = os.environ.get('USER_AGENT')
