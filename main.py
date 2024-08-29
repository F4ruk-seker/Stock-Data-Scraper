from scrapers import ActivePublicOfferingScraper, OfferScraper
import config


tasks = [
    {
        'target': config.OFFER_DATA_SOURCE,
        'scraper': OfferScraper
    },
    {
        'target': config.PUBLIC_OFFER_DATA_SOURCE,
        'scraper': ActivePublicOfferingScraper
    }
]

for task in tasks:
    if scraper := task.get('scraper')(target=task.get('target')):
        print(f'{task.get('scraper').__name__}')
        print(scraper.data)
