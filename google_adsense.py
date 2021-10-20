import re
import requests
from bs4 import BeautifulSoup


def get_google_adsense(domain):
    r = requests.get("http://"+domain)
    soup = BeautifulSoup(r.content, 'html5lib')
    ca_pub_id = re.findall("ca-pub-\d*", str(soup))
    if len(ca_pub_id) > 0:
        return ca_pub_id[0]
    else:
        return None


print(get_google_adsense("devanagarifonts.net"))