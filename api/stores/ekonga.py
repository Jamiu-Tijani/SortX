from bs4 import BeautifulSoup
import requests
import cfscrape
import json
from ..models import *
url = "https://www.konga.com/search?search="
def start_requests(self):
    for url in self.start_urls:
        token, agent = cfscrape.get_tokens(url, 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 RuxitSynthetic/1.0 v6870249674 t38550 ath9b965f92 altpub cvcv=2, _optional_')
        yield Request(url=url, cookies=token, headers={'User-Agent': agent})



def ekonga(query):
    url = "https://www.konga.com/search?search="+query
    token, agent = cfscrape.get_tokens(url, 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 RuxitSynthetic/1.0 v6870249674 t38550 ath9b965f92 altpub cvcv=2, _optional_')
    k_response =requests.get(url=url, cookies=token, headers={'User-Agent': agent})
    k_soup = BeautifulSoup(k_response.text,'html.parser')
    script = k_soup.find_all("script", {"id":"__NEXT_DATA__"})
    needed = script[0]
    done = json.loads(needed.contents[0])
    konga_data = done["props"]["initialProps"]["pageProps"]["resultsState"]["content"]['_rawResults'][0]['hits']
    for x in konga_data:
        if 'Accessories'.lower() not in str(x['category'][1]['category_name'].lower()):
            title = x['name']
            img = "https://www-konga-com-res.cloudinary.com/w_auto,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product" + x["image_thumbnail_path"] 
            link ="https://www.konga.com/product/" + x['url_key']
            price = x['price']
        
    
    
    
    return title, img,link,price


