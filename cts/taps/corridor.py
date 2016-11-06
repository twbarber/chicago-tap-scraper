import re

import requests
from bs4 import BeautifulSoup

from cts.menu import Menu, Beer

BASE_URL = "http://www.corridorchicago.com/beer-menu/"


def get_menu_html():
    return requests.get(BASE_URL, headers={'User-agent': 'Tap Room Chicago'})


def parse_menu_html(html):
    soup = BeautifulSoup(html.content, "lxml")
    content = soup.find("div", {"id": "block-b49ad1de13139de70881"}).find("p", {"class": "text-align-center"})
    update_date = content.find("em").get_text().split("as of")[1].strip()
    beer_list = content.find_all("span")
    beers = parse_beers(beer_list)
    return Menu(update_date, beers)


def parse_beers(beer_list):
    x = 0
    beers = []
    while x < len(beer_list):
        span = beer_list[x]
        if is_beer_title(span):
            title = span.get_text()
            style = ""
            abv = ""
            desc = ""
            n = x + 1
            while n < len(beer_list) and not is_beer_style(beer_list[n]):
                if is_beer_title(beer_list[n]):
                    break
                text = beer_list[n].get_text()
                if is_beer_style(text):
                    entries = text.split("(")
                    style = entries[0].strip()
                    if style is None or style is "":
                        style = beer_list[n-1].get_text().strip()
                    abv = entries[1].split(" ABV")[0]
                else:
                    desc += re.sub(r'\.(?! )', '. ', re.sub(r' +', ' ', text))
                n += 1
            beers.append(Beer(title, style, abv, desc.strip()))
            x = n
    return beers


def is_beer_title(span):
    return span["style"] in ["font-size:14pt", "font-size:14.0pt", "font-size:18.6667px"]


def is_beer_style(line):
    return "%" in line


def get_menu():
    html = get_menu_html()
    return parse_menu_html(html)
