import requests
from bs4 import BeautifulSoup

from cts.menu import Menu, Beer

BASE_URL = "http://www.dryhopchicago.com/drink/beer/"


def get_menu_html():
    return requests.get(BASE_URL)


def parse_menu_html(html):
    soup = BeautifulSoup(html.content, "lxml")
    menu = soup.find("div", {"class": "menu-content"})
    update_date = menu.find("span").find("strong").get_text().split(" ")[-1]
    beer_list = soup.find("ul", {"id": ""})
    beers = beer_list.find_all("li")
    beers.pop()
    beers = parse_beers(beers)
    return Menu(update_date, beers)


def parse_beers(beer_list):
    beers = []
    for item in beer_list:
        name = item.find("h3").get_text().strip()
        info = item.findAll("p")
        style = info[0].get_text().split("—")[0]
        abv = info[0].get_text().split("—")[1]
        desc = info[1].get_text()
        beers.append(Beer(name, style, abv, desc))
    return beers


def get_menu():
    html = get_menu_html()
    return parse_menu_html(html)
