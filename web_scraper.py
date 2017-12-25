
# imports
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup  # parses the html page


# setting the url
# newegg serach result for "video cards"
URL = """https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=vidoe+cards&ignorear=0&N=-1&isNodeId=1"""


# loading the webpage  text into a local variable
u_client = urlopen(URL)
page_html = u_client.read()
u_client.close()
page_soup = soup(page_html, "html.parser")


# get all the div containers  that contain each item(graphic cards) on the website
# to get the proper attribute, you need to look at the html output
container_divs = page_soup.find_all("div", {"class": "item-container"})


# open a csv file to store the scraped info
file = open("products.csv", "w")
headers = "brand,product_name,shipping\n"
file.write(headers)

# loop through all the items (containers)
for container in container_divs:
    brand = container.div.div.a.img["title"]
    title_container = container.find_all("a", {"class": "item-title"})
    product_name = title_container[0].text
    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()
    file.write(brand + "," + product_name.replace(",", "|") +
               "," + shipping + "\n")


# close the file
file.close()
