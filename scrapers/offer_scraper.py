from scrapers.scraper import Scraper
import requests
from bs4 import BeautifulSoup
from models import OfferModel


class OfferScraper(Scraper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def scrape(self):
        response = requests.get(self.target)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            for stock in soup.find('table', {'id': 'stocks'}).find('tbody').find_all('tr'):
                td = stock.find_all('td')
                offer_model: OfferModel = OfferModel(
                    name=td[0].find('div', {'class': 'currency-details'}).find_all('div')[1].text.strip(),
                    code=td[0].find('div', {'class': 'currency-details'}).find_all('div')[0].text.strip(),
                    url=td[0].find('a').get('href'),
                    logo=td[0].find('img').get('src'),
                    current_price=td[1].text.strip(),
                    max_price=td[2].text.strip(),
                    min_price=td[3].text.strip(),
                    percentage=td[5].text.strip(),
                    last_update=td[6].text.strip(),
                    chart=td[7].find('img').get('src')
                )
                self + offer_model  # magic method __add__ > this function add to __data attribute
            self.set_successful(True)

    @property
    def data(self) -> list[OfferModel]:
        return super().data


if __name__ == '__main__':
    if scraper := OfferScraper(target=''):
        print(scraper.data)
