from requests import api
import json
from api import OfferApiSYNC

# with open('result.json', 'r', encoding='utf-8') as df:
#     raw = df.read()
#     data = json.loads(raw)
#
#
# response = api.post('http://127.0.0.1:8000/api/offers/bulk/offers', json=data)
#
# print(response)
# print(response.status_code)
# print(response.text)


with open('ative_offer_test_data.json', 'r', encoding='utf-8') as df:
    data = json.loads(df.read())

for d in data:
    print(d)
#
response = api.post('http://127.0.0.1:8000/api/offers/bulk/public-offer', json=data)

print(response)
print(response.status_code)
print(response.text)
