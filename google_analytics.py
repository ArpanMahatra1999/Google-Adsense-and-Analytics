import re
import requests
from bs4 import BeautifulSoup


def get_google_analytics(domain):
    r = requests.get("http://" + domain)
    soup = BeautifulSoup(r.content, 'html5lib')
    ua_id = None
    for script in soup.find_all('script'):
        if len(script.text) > 0:
            ua_id = re.findall("UA-\d*-\d*", script.text)
            if len(ua_id) > 0:
                break
    if ua_id:
        return ua_id[0]
    else:
        return None


print(get_google_analytics("devanagarifonts.net"))