from urllib.parse import urlparse
import pprint

from _download_images import *
from fetch_spacex_images import *
from fetch_nasa_images import *

pp = pprint.PrettyPrinter(indent=4)
BOT_TOKEN = '5778281282:AAHAPOtzeP7_qofFxkkb0KxgSJzhMarWn-Y'
    

def main():
    if fetch_nasa_apod(): print ('Job is done')


if __name__ == '__main__':
    main()