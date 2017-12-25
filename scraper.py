import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=vidoe+cards&ignorear=0&N=-1&isNodeId=1"
u_client = urlopen(url)
page_html = u_client.read()
u_client.close()
page_soup = soup(page_html, "html.parser")
container_divs= page_soup.find_all("div",{"class":"item-container"})
