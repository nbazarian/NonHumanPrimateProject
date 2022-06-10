#Based on this code: https://infatica.io/blog/scrape-images-with-python/

from bs4 import BeautifulSoup

import requests
import shutil

class BeautifulScrapper():
    def __init__(self, url:str, classid:str, folder:str):
        self.url = url
        self.classid = classid
        self.folder = folder
    
    def _get_info(self):
        image_data = []

        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", class_= self.classid)

        for link in links:
            image_tag = link.findChildren("img")
            image_data.append((image_tag[0]["src"], image_tag[0]["alt"]))

        return image_data

    def _download_images(self, image_data):
        response = requests.get(image_data[0], stream=True)
        realname = ''.join(e for e in image_data[1] if e.isalnum())
        
        file = open(self.folder.format(realname), 'wb')
        
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, file)
        del response

    def scrape_images(self):
        image_data = self._get_info()    

        for i in range(0, len(image_data)):
            self.download_image(image_data[i])
