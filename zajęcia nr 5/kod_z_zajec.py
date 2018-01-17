import requests

url = 'http://api.nbp.pl/api/exchangerates/tables/A'

#do pracy domowej bedzie trzeba zmienic url u gory i potem ogarnac po obiektach pythonowych polecenie

#try:
    #cos tam r = requests.get(url=url)
#except Eception as e:


r = requests.get(url=url)
print(r)

from pprint import pprint
# order = ('headers', 'raw', 'status_code', 'ok', 'request', 'url', 'content', 'text', 'json')
# for attr in order:
#     print(attr)
#     pprint(getattr(r, attr))
#     print(80 * '-')
# print('json')
# pprint(r.json())

for x in r.json():
    print('type(x)', type(x))
    pprint(x)
    print(80*'_')