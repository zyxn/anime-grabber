# import requests
# from bs4 import BeautifulSoup

# page = requests.get('https://drivenime.com/kanata-no-astra-bd-subtitle-indonesia-batch/')
# soup = BeautifulSoup(page.text, 'html.parser')
# list1 = soup.find_all('div', class_ = ['post-single-content box mark-links'])
# data = "Hasil\n"
# data += "Judul: {}\n".format(soup.find("h1", class_ = ['title single-title']).text)
# for i in list1:
#     pdata = i.find_all('p')
#     informasi = pdata[2]
#     tblink = pdata[0].find('img')
#     p720 = pdata[5].find('a')
#     p480 = pdata[5].find('a')
#     p360 = pdata[5].find('a')
#     sectex = str(informasi).split("<br/>")
#     data += "Thumbnail: {}\n".format(tblink['data-lazy-src'])
#     data += "Sinopsis: {}\n".format(pdata[1].text)
#     data += "informasi:\n"
#     data += sectex[0].strip("<p>")
#     data += sectex[-1].strip("</p>")
#     data += "\n".join(sectex[1:-2])
#     data += "\n\nLink Download\n"
#     data += "   {}: {}\n".format(p720.text, p720['href'])
#     data += "   {}: {}\n".format(p480.text, p480['href'])
#     data += "   {}: {}".format(p360.text, p360['href'])



#print(data)

#print(list1)
# data ="Hasil Menu \n\n"
# num = 1
# print(list1)

    #print(i.a['href'])
    #for x in i:
        #print(a)
        #linkto = x.find("a")
        


        #         "parsinng the container of the page."
        # list1 = soup.find_all('div', class_ = ['post excerpt', 'post excerpt last'])
        # data ="Hasil Menu \n\n"
        # num = 1
        # try:
        #     for i in list1:
        #         caption = i.find("div", class_ = 'post-content image-caption-format-1')
        #         thumbnail = i.find("img", class_ = 'attachment-featured size-featured wp-post-image')
        #         data += 'Anime Ke-{}\n'.format(str(num))
        #         data += 'Judul: {}\n'.format(i.a['title'])
        #         data += 'Link: {}\n'.format(i.a['href'])
        #         data += 'Caption: "{}"\n'.format(caption.text[10:])
        #         data += 'Thumbnail: {}\n\n'.format(thumbnail['src'])
        #         num += 1


def bntg():
    return "kambing"

    def ayam():
        return "ayam"

print(bntg().ayam())

elif cmd.startswith("sendstick: "):
    sep = text.split(" ")
    grup_id = sep[1]
    tikel_id = sep[2]
    tikel_gede_no_anim["tikelNoAnim"]["template"]["columns"][0]["imageUrl"] = "https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/IOS/sticker@2x.png".format(tikel_id)
    client.sendTemplate(grup_id, tikelgede)


import requests
from bs4 import BeautifulSoup



class Drivenime:

    def homepage(self):
        """Scrap The homepage drivenime"""
        soup = self.request("http://www.drivenime.com")
        data = self.parsing(soup)
        return data

    def search(self, query):
        query = query.replace(" ", "+")
        soup = self.request("http://www.drivenime.com/?s=" + query )
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
        data ="Hasil Menu \n\n"
        tagihan = []
        num = 1
        try:
            for i in list1:
                caption = i.find("div", class_ = 'post-content image-caption-format-1')
                thumbnail = i.find("img", class_ = 'attachment-featured size-featured wp-post-image')
                data += 'Anime Ke-{}\n'.format(str(num))
                data += 'Judul: {}\n'.format(i.a['title'])
                data += 'Link: {}\n'.format(i.a['href'])
                tagihan.append(i.a['href'])
                data += 'Caption: "{}"\n'.format(caption.text[10:])
                data += 'Thumbnail: {}\n\n'.format(thumbnail['src'])
                num += 1
        except:
            return "Anime Tidak Tersedia."
        return data



    def request(self, link):
        """ Request to the link"""
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup
    
    claa
        

    def parse_web(self, soup):
        list1 = soup.find_all('div', class_ = ['post-single-content box mark-links'])
        data = "Hasil\n"
        data += "Judul: {}\n".format(soup.find("h1", class_ = ['title single-title']).text)
        for i in list1:
            pdata = i.find_all('p')
            informasi = pdata[2]
            tblink = pdata[0].find('img')
            p720 = pdata[5].find('a')
            p480 = pdata[5].find('a')
            p360 = pdata[5].find('a')
            sectex = str(informasi).split("<br/>")
            data += "Thumbnail: {}\n".format(tblink['data-lazy-src'])
            data += "Sinopsis: {}\n".format(pdata[1].text)
            data += "informasi:\n"
            data += sectex[0].strip("<p>")
            data += sectex[-1].strip("</p>")
            data += "\n".join(sectex[1:-2])
            data += "\n\nLink Download\n"
            data += "   {}: {}\n".format(p720.text, p720['href'])
            data += "   {}: {}\n".format(p480.text, p480['href'])
            data += "   {}: {}".format(p360.text, p360['href'])
        return data

anime = Drivenime()
print(anime.parse_web(anime.request("http://drivenime.com/fate-kaleid-liner-prisma%e2%98%86illya-prisma%e2%98%86phantasm-bd-subtitle-indonesia/")))