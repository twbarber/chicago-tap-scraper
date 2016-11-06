import json


class Menu(object):

    def __init__(self, updated, beer_list):
        self.updated = updated
        self.beer_list = beer_list

    def __repr__(self):
        return json.dumps(self.__dict__,
                          default=lambda o: o.__dict__,
                          indent=4,
                          separators=(',', ': '))

    def json(self):
        return self.__repr__()


class Beer(object):

    def __init__(self, name, style, abv, desc):
        self.name = name.title()
        self.style = style
        self.abv = abv
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
