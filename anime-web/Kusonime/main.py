import requests
from bs4 import BeautifulSoup


class Kusonime:

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
        soup = self.request("https://www.kusonime.com/")
        data = self.parse(soup)
        return data
    
    def search(self, query):
        query = query.replace(" ", "+")
        soup = self.request("https://kusonime.com/?s={}&post_type=post".format(query))
        data = self.parse(soup)
        return data

    def parse(self,soup):
        list1 = soup.find_all('div', class_ = "kover")
        num = 1
        meta_data = {}
        for i in list1:
            judul = [x for x in i.find('h2', class_ = "episodeye")]
            thumb = [x for x in i.find('div', class_ = "thumbz")]
            genre = [x for x in i.find_all('a', rel = 'tag')]
            meta_data[num] = {"Judul": judul[0].text,
            "Link": judul[0]['href'],
            "Thumbnail": thumb[1]['src'],
            "Genre": ', '.join(x.text for x in genre)
            }
            num += 1
        self.data = meta_data
        return self

    def parse_page(self,soup):
        meta_data = {}
        judul = soup.find('h1', class_ = 'jdlz').text
        thumb_meta = [i for i in soup.find('div', class_ = 'post-thumb')]
        thumb = thumb_meta[3]['srcset'].split(", ")
        info = [x for x in soup.find('div', class_ = 'info')]
        sinop = [x for x in soup.find('div', class_ = 'lexot')]
        donlod = [x for x in soup.find('div', class_ = 'smokeddl')]
        meta_data = {"judul": judul,
        'thumbnail': thumb[-1].split(" ")[0],
        'informasi':{'japanese': info[0].text[10:],
        'seasons': info[2].text[10:],
        'type': info[4].text[6:],
        'total-episode':info[6].text[15:] , 
        'durasi':info[8].text[10:] ,
        'genre': info[1].text[8:],
        'produser':info[3].text[11:] ,
        'status': info[5].text[8:],
        'skor':info[7].text[7:],
        'rilis': info[9].text[13:]},
        'sinopsis': sinop[2].text,
        'link-download': None}
        link_dw = {}
        #num = 1
        for i in donlod[1:]:
           linked = i.find_all('a')
           link_dw[i.strong.text] = {
               'Google Sharer':linked[0]['href'],
               'Berkascloud':linked[1]['href'],
               'Google Drive':linked[2]['href'],
               'Mega.nz':linked[3]['href'],
               'Uptobox':linked[4]['href'],
               'Mirror':linked[5]['href']}
        meta_data['link-download'] = link_dw
        return meta_data

        #print(str(donlod[1].strong.text))
    
    def pick(self, num):
        link = self.data[num]['Link']
        soup = self.request(link)
        data = self.parse_page(soup)
        self.hasil = data
        return self.hasil




    #def parse(self, soup):
       # list1 = soup.find_all('div', class_ = "kover")




cl = Kusonime()
print(cl.homepage().pick(10))