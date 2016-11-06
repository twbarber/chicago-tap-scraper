from distutils.core import setup

setup(
    name='chicago-tap-scraper',
    version='0.0.1',
    packages=['TapScraper', 'TapScraper.taps', 'TapScraper.tests'],
    url='https://github.com/twbarber/chicago-tap-scraper',
    license='MIT',
    author='Tyler Barber',
    author_email='dev@twbarber.com',
    description='Used for retrieving Chicago Craft Breweries current Tap Lists'
)
