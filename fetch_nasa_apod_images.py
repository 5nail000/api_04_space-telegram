from urllib.parse import urlparse

from base_functions import *


def fetch_nasa_apod(folder = 'images', count = 30):
    url = f'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key' : NASA_KEY,
        'count': count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    for image in response.json():
        image_link = image['url']
        parsed_link = urlparse(image_link)
        file_name = f'nasa_apod_{image["date"]}_{parsed_link.path.split("/")[-1]}'
        if parsed_link.hostname =='apod.nasa.gov':
            download_image(image_link, file_name= file_name, folder= folder)
            print(file_name)
    
    return True


if __name__ == '__main__':
    fetch_nasa_apod()