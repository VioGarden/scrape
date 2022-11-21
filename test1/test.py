import requests

import datetime

from requests_html import HTML

now = datetime.datetime.now()
second = now.second
micro = now.microsecond

url = 'https://gist.github.com/blissfulyoshi/586f173ba9afa45c64a7cb7c47ce7d1c/raw/613e214cff768f590074b967443f86d53dc6e871/Eastern%2520Ranked%2520Song%2520List:%25202021-06-01.json'

r = requests.get(url)

the_text = r.text

# with open(f"file-{second}-{micro}", 'w') as f:
#     f.write(the_text) # returns a JSON page

# print(type(the_text)) # a string




