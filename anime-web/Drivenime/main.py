import requests
from bs4 import BeautifulSoup



class Drivenime:
    def __init__(self):
        self.data = {}
        self.hasil = {}
    
    def __repr__(self):
        return str(self.data)

    def homepage(self):
        """Scrap The homepage drivenime"""
        soup = self.request("http://www.drivenime.com")
        data = self.parsing(soup)
        return data

    def genre(self, genres):
        genres = genres.replace(" ", "+")
        soup = self.request("http://www.drivenime.com/genre/{}/".format(genres))
        data = self.parsing(soup)
        return data

    def parsing(self, soup):
        "parsinng the container of the page."
        list1 = soup.find_all('div', class_ = ['post excerpt', 'post excerpt last'])
        data = {}
        num = 1
        try:
            for i in list1:
                caption = i.find("div", class_ = 'post-content image-caption-format-1')
                thumbnail = i.find("img", class_ = 'attachment-featured size-featured wp-post-image')
                data[num] = {
                    'judul': i.a['title'], 
                    'link': i.a['href'],
                    'caption': caption.text[10:],
                    'thumbnail': thumbnail['src']
                    }
                num += 1
        except:
            return "Anime Tidak Tersedia."
        self.data = data
        return self

    def search(self, query):
        query = query.replace(" ", "+")
        soup = self.request("http://www.drivenime.com/?s=" + query )
        data = self.parsing(soup)
        return data

    def request(self, link):
        """ Request to the link"""
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def parse_web(self, soup):
        list1 = soup.find_all('div', class_ = ['post-single-content box mark-links'])
        data = {}
        judul = soup.find("h1", class_ = ['title single-title']).text
        for i in list1:
            pdata = i.find_all('p')
            informasi = pdata[2]
            tblink = pdata[0].find('img')
            p720 = pdata[5].find('a')
            p480 = pdata[5].find('a')
            p360 = pdata[5].find('a')
            sectex = str(informasi).split("<br/>")
            data = {'judul': judul,
            'thumbnail': tblink['data-lazy-src'],
            'sinopsis': pdata[1].text,
            'informasi': "{}\n{}\n{}".format(sectex[0].strip("<p>"),sectex[-1].strip("</p>"),"".join(sectex[1:-2])),
            'download':{
                '360p': p360['href'],
                '480p': p480['href'],
                '720p':p720['href']
            }}
        return data

    def pick(self,num):
        link = self.data[num]['link']
        soup = self.request(link)
        data = self.parse_web(soup)
        self.hasil = data
        return self.hasil
