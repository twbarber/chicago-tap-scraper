from bs4 import BeautifulSoup
import requests
import json

BASE_URL = "http://www.dryhopchicago.com/drink/beer/"


class Menu(object):

    def __init__(self, updated, beer_list):
        self.updated = updated
        self.beer_list = beer_list

    def __repr__(self):
        return json.dumps(self.__dict__,
                          default=lambda o: o.__dict__,
                          indent=4,
                          separators=(',', ': ')
                          )

    def json(self):
        return self.__repr__()


class Beer(object):

    def __init__(self, name, info, desc):
        self.name = name.title()
        self.style = self.parse_style(info)
        self.abv = self.parse_abv(info)
        self.desc = desc

    def __str__(self):
        return "Name: " + self.name + "\nStyle: " + self.style + \
            "\nABV: " + self.abv + "\nDesc: " + self.desc + "\n"

    def __repr__(self):
        return json.dumps(str(self.__dict__))

    @staticmethod
    def parse_style(info):
        return info.split("—")[0]

    @staticmethod
    def parse_abv(info):
        return info.split("—")[1]


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
        style = info[0].get_text()
        desc = info[1].get_text()
        beers.append(Beer(name, style, desc))
    return beers


def get_menu():
    html = get_menu_html()
    return parse_menu_html(html)
