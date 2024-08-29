import os
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent

env = os.getenv

PUBLIC_OFFER_DATA_SOURCE = env('PUBLIC_OFFER_DATA_SOURCE')
OFFER_DATA_SOURCE = env('OFFER_DATA_SOURCE')
