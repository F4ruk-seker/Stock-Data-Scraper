import os
from pathlib import Path

from requests.auth import HTTPBasicAuth

from models.api_model import ApiHostModel

BASE_DIR: Path = Path(__file__).resolve().parent

env = os.getenv

PUBLIC_OFFER_DATA_SOURCE = env('PUBLIC_OFFER_DATA_SOURCE')
OFFER_DATA_SOURCE = env('OFFER_DATA_SOURCE')
API_HOST = ApiHostModel(env('API_HOST'))
API_USER = env('API_USER')
API_PASSWORD = env('API_PASSWORD')

AUTH = HTTPBasicAuth(API_USER, API_PASSWORD)