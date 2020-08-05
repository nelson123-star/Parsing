import requests
import csv
from bs4 import BeautifulSoup

#url = "https://journal.tinkoff.ru/list/most-expensive-cars/"

#header = {"User-agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

#response = requests.get(url, headers=header)

#html = response.text

#soup = BeautifulSoup(html,"html.parser")

#conteiner = soup.find("div", id = "bodyNews", {"class":"oldurls"})

#elements = conteiner.find_all("p", align= "justify")
#print(elements)
##string = "Топ самых больших звезд:"+"\n"
##k = 0
#for element in elements:
#    if element.find("strong"):
#        print(element.strong + "\n")
##        string += "\t" + element.strong.text + "\n"

##with open('data.txt','w',encoding = 'utf8') as f:
##    f.write(string)

#url = "https://wonderful-planet.ru/gidrosfera/22-reki-8/"

#response = requests.get(url)

#if response.status_code == 200:
#    html=response.text

#soup = BeautifulSoup(html,"html.parser")

#table = soup.find("table")

#trs = table.find_all("tr")

#string = "Названия рек и их протяженность: \n"

#for e, tr in enumerate(trs):
#    if e == 0:
#        continue
#    tds = tr.find_all("td")
#    name = tds[1].text.strip()
#    length = tds[2].text.strip()
#    string += "\t{} {} {}км \n".format(e,name,length)

#print(string)

#url = "https://www.worldfootball.net/teams/leicester-city/2013/3/"

#response = requests.get(url)

#html = response.text

#soup = BeautifulSoup(html, "html.parser")

#table = soup.find("table",{"class":"standard_tabelle"})

#lines = table.find_all("tr")
#count = 0

#for line in lines:
#    elements = line.find_all("td")
#    if len(elements) == 8:
#        count+=int(elements[6].text.strip().split(":")[0])

#print(count)

#url = "http://statistic.su/blog/earth_distance/2010-07-14-7"

#response = requests.get(url)

#html = response.text

#soup = BeautifulSoup(html, "html.parser")

#uls = soup.find_all("ul")

#for ul in uls:
#    if "Меркурий" in ul.text:
#        data=ul.text.strip().split("\n")

#arr_data = []

#for d in data:
#    temp = d.replace(" ", "").split("-")
#    temp[1] = int(float(temp[1])*1000000)
#    arr_data.append(temp)

#for data in arr_data:
#    print("\t",data[0], data[1])

#print("\n")
#arr_data = sorted(arr_data, key = lambda x: x[1], reverse = False)
#for data in arr_data:
#    print("\t",data[0], data[1])

#url = "http://sportunit.ru/velosipedy?limit=100"

#response = requests.get(url)

#html = response.text

#multi_class = "product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12".split(" ")

#soup = BeautifulSoup(html, "html.parser")

#products = soup.find_all("div", {"class":"col-xs-12"})
#arr_data = []
#count = 1
#sum = 0
#for product in products:
#    if product.attrs["class"] == multi_class:
#        image = product.find("img")["src"]
#        name = product.find("div", {"class":"product-name"}).text
#        code = product.find("div", {"class":"product-model"}).text
#        description = product.find("div", {"class":"product-description"}).text
#        price = product.find("p", {"class":"price"}).text.strip().replace("р.","")
#        print("\t",count,name+" "+price+" рублей "+" "+code+" "+"\n"+"\t"+description)
#        arr_data.append([name,price,code,description])
#        count +=1
#        sum +=int(price)

#print("\n\t"+"Общая сумма стоимости велосипедов: ",sum)
#sum = str(sum)
#names = ["Наименование","Цена","Номер","Описание"]

#with open("data1.csv","w",newline="") as f:
#    writer = csv.writer(f,delimiter = " ")
#    writer.writerow(names)

#    for product in arr_data:
#        writer.writerow(product)
#    writer.writerow(sum)

from datetime import datetime
print("Выбирите жанр")
headline = str(input())
print("Введите рейтинг")
#rating_input = float(input())
try:
    rating_input = float(input())
except ValueError:
    rating_input = rating_input.replace(",",".")
start_time = datetime.now()
string = ""
string_url=""
count = 1
for i in range(1,7):

    url = "https://bop.filmshd.vip/xfsearch/genre/{}/page/{}/".format(headline,i)

    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    container = soup.find("div", id = "dle-content")
    films = soup.find_all("div", {"class":"th-tip"})
    #films_url = soup.find_all("a")
    #print(films_url)
    #for film_url in films_url:
    #    film_url = films_url.get("href")  
    #    string_url += "\t{}\n".format(film_url)
    #    print(string_url)
        
    for film in films:
        name = film.find("div", {"class":"th-tip-title"}).text.strip()
        short_info = film.find_all("div", {"class":"short-info"})
        try:
            rating = film.find("div", {"class":"short-info kp"}).text.strip().replace("КиноПоиск:","")
            rating = rating.replace(" ","")
        except AttributeError:
            continue
        data = short_info[0].text.strip()
        country = short_info[1].text.strip()
        #geenre = short_info[2].text.strip()
        #timing = short_info[3].text.strip()
        if float(rating) >rating_input:
            string += "{}".format(count)+"\tНазвание: {} \n".format(name) + "\t{} \n".format(data) + "\t{} \n".format(country)+"\tРейтинг:{} \n".format(rating)#+"\tСсылка:{} \n".format(film_url)
            count+=1
        print(string)

end_time = datetime.now()

print("Фильмы в жанре {} c рейтингом выше {}:".format(headline,rating_input),count-1,"\n"+string,"\n"+string_url,'Время: {}'.format(end_time - start_time))

with open('data_films.txt','w',encoding = 'utf8') as f:
    f.write(headline)
    f.write("\n")
    f.write(string)
            #country = info.find("span", "Страна").text.strip()
            #geenre = info.find("span", "Жанр").text.strip()
            #timing = info.find("span", "Длительность").text.strip()
            #if "Дата" in info.text:
            #    data = info.text               
                #if "Страна" in info.text:
                #    country = info.text.strip()
                
                    #string += "\tНазвание: {} \n".format(name) + "\tДата: {} \n".format(data) + "\tСтрана: {} \n".format(country)
                    #if "Жанр" in info.text:
                    #    geenre = info.text.strip()
                    #    if "Длительность" in info.text:
                    #        timing = info.text.strip()
                            #+ "\tЖанр: {} \n".format(geenre)+ "\tДлительность: {} \n".format(timing)
        
        #print(count,string)
      
    #count +=1
    
    
#if "Год" in short_info.text:
        #    data=short_info.text.strip().split("\n")
        #if "Год" in short_info.text:
        #    data=ul.text.strip().split("\n")
        #rate = film.find("div", {"class":"rate"}).text
        #year = film.find("span", {"class":"sh_year"}).text
        #link = film.find("div", {"class":"title"}).a["href"]
        # #string_info += "\tНазвание: {} \n".format(name)
        #string_info += "\tКатегория: {} \n".format(category.replace(" ",""))
        #string_info += "\tРейтинг: {} \n".format(rate)
        #string_info += "\tГод: {} \n".format(year)
        #string_info += "\tСсылка: {} \n".format(link)
        #+ "\tКатегория: {} \n".format(category.replace(" ",""))+ "\tРейтинг: {} \n".format(rate)+"\tГод: {} \n".format(year)+"\tСсылка: {} \n".format(link)





