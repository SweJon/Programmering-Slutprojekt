import requests
import random
import urllib.request
from bs4 import BeautifulSoup #tilläg som används för att läsa av hemsidor


def image_spider(max_pages): #funktion som tar upp bildernas url för att ladda ner de
    page = 1
    while page <= max_pages:
        url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=strawberry&_sacat=11700&LH&_pgn=" + str(page)
        source_code = requests.get(url)
        down_img = source_code.text
        soup = BeautifulSoup(down_img, features="html.parser")
        for link in soup.findAll("img", {"class": "s-item__image-img"}):
            src = link.get("src")
            print(src)
        page += 4 #antalet sidor som ska läsas av


def download_web_image(adr): #funktion som laddar ner bilder
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(adr, full_name)

download_web_image("http://teespring-storecontent.s3.amazonaws.com/oH48W9OolEiG3_iE40F0tw_store_banner_image?1478560026161")

