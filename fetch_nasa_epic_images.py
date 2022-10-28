import os
import requests

from datetime import datetime
from base_functions import download_image
from dotenv import load_dotenv


def fetch_nasa_epic(nasa_key, natural= True, folder= 'images'):
    url = f'https://api.nasa.gov/EPIC/api/'
    if natural: collection_type = 'natural'
    else: collection_type = 'enhanced'
    url = f'{url}{collection_type}'
    params = {'api_key' : nasa_key}
    response = requests.get(url, params=params)
    response.raise_for_status()

    for image in response.json():

        image_name = image['image']
        image_date = datetime.fromisoformat(image['date']).strftime('%Y/%m/%d')
        image_link = f'https://epic.gsfc.nasa.gov/archive/{collection_type}/{image_date}/jpg/{image_name}.jpg'
        
        file_name = f'nasa_{collection_type}_{image_name}.jpg'

        download_image(image_link, file_name= file_name, folder= folder)

    return True


if __name__ == '__main__':

    load_dotenv()

    try:
        nasa_key = os.environ['NASA_KEY']
    except Exception as _ex: 
        print (f'KeyError: {_ex}')
    else:
        fetch_nasa_epic(nasa_key)