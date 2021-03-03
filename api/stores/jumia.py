from bs4 import BeautifulSoup
import requests
def jumia(query):
    
    url = "https://www.jumia.com.ng/catalog/?q="+query
    response = requests.get(url)
    dat = response.text
    soup = BeautifulSoup(dat,'html.parser')
    a = soup.find_all("a",{"class":"core"})
    for x in a:
        if 'Accessories'.lower() not in str(x.get('data-category')).lower():
            title = str(x.get('data-name'))
            img = str(x.find('img').get('data-src'))
            link ="https://jumia.com.ng" + str(x.get('href'))
            price= "na"
            for child in x.find('div',{'class':'prc'}).children:
                price= child
        else:
            title = "NA"
            img = "NA"
            link ="NA"
            price = "NA"
                    
    return title, img,link, price