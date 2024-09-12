from scrapers import ActivePublicOfferingScraper, OfferScraper
from api import OfferApiSYNC
from requests.auth import HTTPBasicAuth
from models import ApiTaskModel, TaskModel
import config


tasks = [
    TaskModel(
        kwargs={'target': config.OFFER_DATA_SOURCE},
        scraper=OfferScraper,
        api_task=ApiTaskModel(
            data=[],
            data_type='json',
            url=config.API_HOST / 'assets/bulk/assets',
            auth=config.AUTH
        )
    ),
    TaskModel(
        kwargs={'target': config.PUBLIC_OFFER_DATA_SOURCE},
        scraper=ActivePublicOfferingScraper,
        api_task=ApiTaskModel(
            data=[],
            data_type='json',
            url=config.API_HOST / 'assets/bulk/public-assets',
            auth=config.AUTH,
            success_codes=[201, 204]
        )
    )
]

for task in tasks:
    if scraper := task.scraper(**task.kwargs):
        task.api_task.data = [d.__dict__ for d in scraper.data]
        task.api_task.auth = HTTPBasicAuth('pars', 'pars')
        # auth
        if offer_api_sync := OfferApiSYNC(**task.api_task.__dict__):
            print('ok')

        print(f'{task.scraper.__name__} - sayı {len(scraper.data)}')
        print(scraper.data[0].__dict__)
