import re
import requests
from bs4 import BeautifulSoup
from cts.menu import Menu, Beer

BASE_URL = "http://www.haymarketbrewing.com/beers"


def get_menu_html():
    return requests.get(BASE_URL, headers={'User-agent': 'Tap Room Chicago'})


def parse_menu_html(html):
    soup = BeautifulSoup(html.content, "lxml")
    content = soup.find("div", {"id": "block-b49ad1de13139de70881"}).find("p", {"class": "text-align-center"})
    return Menu(update_date, beers)


def parse_beers(beer_list):
    beers = []
    return beers


def is_beer_title(span):
    return span["style"] in ["font-size:14pt", "font-size:14.0pt", "font-size:18.6667px"]


def is_beer_style(line):
    return "%" in line


def get_menu():
    html = get_menu_html()
    return parse_menu_html(html)
