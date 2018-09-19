"""
Simple web scraper, done with BeautifulSoup. 
"""

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

myURL = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
uClient = uReq(myURL)

#read the page and get the html
pageHTML = uClient.read()
uClient.close()
pageSoup = soup(pageHTML, "html.parser")

#get each product
containers = pageSoup.findAll("div",{"class" : "item-container"})

#create the file
filename = "productos.csv"
f = open(filename,"w")

#create file headers
headers = "brand, product_name, shipping \n"
f.write(headers)

#loop the page and store the values 
for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a",{"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    #write in the file, product names has commas, so i replace them for a blank space
    f.write(brand+","+product_name.replace(","," ")+","+shipping+"\n")

#close the file
f.close()    