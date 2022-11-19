import os
import requests
from base_functions import download_image
from urllib.parse import urlparse
from dotenv import load_dotenv


def get_nasa_apod_request(url, nasa_key, count=30):
    params = {
        'api_key': nasa_key,
        'count': count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_nasa_apod(nasa_key, folder='images', count=30):

    api_url = 'https://api.nasa.gov/planetary/apod'
    for image in get_nasa_apod_request(api_url, nasa_key, count):
        if image['media_type'] == 'image':
            image_link = image['url']
            parsed_link = urlparse(image_link)
            file_name = parsed_link.path.split("/")[-1]
            file_name = f'nasa_apod_{image["date"]}_{file_name}'
            if parsed_link.hostname == 'apod.nasa.gov':
                download_image(image_link, file_name=file_name, folder=folder)
                print(file_name)


if __name__ == '__main__':

    load_dotenv()
    nasa_key = os.environ['NASA_KEY']
    fetch_nasa_apod(nasa_key)
