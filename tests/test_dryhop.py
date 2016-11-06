import re
import unittest
from taps.dryhop import Dryhop


class DryHopTest(unittest.TestCase):

    dryhop = Dryhop()
    html = dryhop.get_menu_html()

    def test_url_ok(self):
        response = self.dryhop.get_menu_html()
        self.assertEqual(response.status_code, 200)

    def test_can_parse_menu(self):
        menu = self.dryhop.parse_menu_html(self.html)
        self.assertTrue(menu.updated is not None)
        self.assertTrue(len(menu.beer_list) > 0)

    def test_beer_list_integrity(self):
        menu = self.dryhop.parse_menu_html(self.html)
        for beer in menu.beer_list:
            self.assertTrue(beer.name is not None)
            self.assertTrue(re.match(r'^\d\.\d%', beer.abv))
            self.assertTrue(beer.style is not None)
            self.assertTrue(beer.desc is not None)
