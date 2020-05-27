import requests
from bs4 import BeautifulSoup


class Otakudesu:
    def __init__(self):
        self.data = {}
        self.hasil = {}

    def __repr__(self):
        return str(self.data)

    def request(self, link):
        """ Request to the link"""
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def homepage(self):
        soup = self.request("https://otakudesu.org/")
        list1 = soup.find('div', class_ = "venz")
        contain = list1.find_all('li')
        data = {}
        num = 1
        for i in contain:
            eps = i.find('div', class_ ="epz")
            thumb = i.find("img")
            data[num] = {'judul': i.h2.text,
            'Episode': eps.text,
            'link': i.a['href'],
            'thumbnail': thumb['src']}
            num += 1
        self.data = data
        return self 


#lu ambil apa aja btw ? eps, thumbnail, link donlot, 
#dah kelar mi tinggal rapihin
#bjir otaku desu gk bisa di rightclick web nya :v
#dah gampang nih di scrap
#oke gw lanjut bikin mie nya :v

cl = Otakudesu()
print(str(cl.homepage()))
