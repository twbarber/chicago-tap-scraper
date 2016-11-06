from distutils.core import setup

setup(
    name='chicago-tap-scraper',
    version='0.0.4',
    packages=['cts', 'cts.taps', 'cts.tests'],
    url='https://github.com/twbarber/chicago-tap-scraper',
    license='MIT',
    author='Tyler Barber',
    author_email='dev@twbarber.com',
    description='Used for retrieving Chicago Craft Breweries current Tap Lists'
)
