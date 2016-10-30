from bs4 import BeautifulSoup
import requests

BASE_URL = "http://www.dryhopchicago.com/drink/beer/"


class Beer(object):

    def __init__(self, name, info, desc):
        self.name = name.title()
        self.style = self.parse_style(info)
        self.abv = self.parse_abv(info)
        self.desc = desc

    def __str__(self):
        return "Name: " + self.name + "\nStyle: " + self.style + \
            "\nABV: " + self.abv + "\nDesc: " + self.desc + "\n"

    @staticmethod
    def parse_style(info):
        return info.split("—")[0]

    @staticmethod
    def parse_abv(info):
        return info.split("—")[1]


def get_tap_list():
    html = requests.get(BASE_URL)
    soup = BeautifulSoup(html.content, "lxml")
    beer_list = soup.find("ul", {"id": ""})
    beers = beer_list.find_all("li")
    beers.pop()
    for item in beers:
        name = item.find("h3").get_text().strip()
        info = item.findAll("p")
        style = info[0].get_text()
        desc = info[1].get_text()
        beer = Beer(name, style, desc)
        print(beer)

get_tap_list()
