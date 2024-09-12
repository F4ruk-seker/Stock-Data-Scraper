from scrapers import ActivePublicOfferingScraper, OfferScraper
from api import OfferApiSYNC
from requests.auth import HTTPBasicAuth

import config


tasks = [
    {
        'target': config.OFFER_DATA_SOURCE,
        'scraper': OfferScraper,
        'api': {
            'url': config.API_HOST / 'assets/bulk/assets',
            'data_type': 'json'
        }
    },
    # {
    #     'target': config.PUBLIC_OFFER_DATA_SOURCE,
    #     'scraper': ActivePublicOfferingScraper
    # }
]

for task in tasks:
    if scraper := task.get('scraper')(target=task.get('target')):
        task['api']['data'] = [d.__dict__ for d in scraper.data]
        task['api']['auth'] = HTTPBasicAuth('pars', 'pars')
        # auth
        if offer_api_sync := OfferApiSYNC(**task['api']):
            print('ok')

        print(f'{task.get('scraper').__name__} - sayı {len(scraper.data)}')
        # print(scraper.data)
