import os
import requests

from datetime import datetime
from base_functions import download_image
from dotenv import load_dotenv


def get_nasa_epic_request(url, nasa_key):
    params = {'api_key': nasa_key}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_nasa_epic(nasa_key, natural=True, folder='images'):
    if natural:
        collection_type = 'natural'
    else:
        collection_type = 'enhanced'
    api_url = f'https://api.nasa.gov/EPIC/api/{collection_type}'
    for image in get_nasa_epic_request(api_url, nasa_key):

        image_name = image['image']
        image_date = datetime.fromisoformat(image['date']).strftime('%Y/%m/%d')
        image_link = f'https://epic.gsfc.nasa.gov/archive/{collection_type}'
        image_link = f'{image_link}/{image_date}/jpg/{image_name}.jpg'

        file_name = f'nasa_{collection_type}_{image_name}.jpg'

        download_image(image_link, file_name=file_name, folder=folder)


if __name__ == '__main__':

    load_dotenv()
    nasa_key = os.environ['NASA_KEY']
    fetch_nasa_epic(nasa_key)
