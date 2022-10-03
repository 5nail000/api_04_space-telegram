import requests
from urllib.parse import urlparse
from _download_images import *

NASA_KEY = 'vmQJpqWaEtt1fW6ZcQfQCG97qsrvI7KwY5aNU4Hd'


def fetch_nasa_apod(folder = 'images'):
    url = f'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key' : NASA_KEY,
        'count': 30
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    for image in response.json():
        image_link = image['url']
        parsed_link = urlparse(image_link)
        file_name = f'nasa_apod_{image["date"]}_{parsed_link.path.split("/")[-1]}'
        if parsed_link.hostname =='apod.nasa.gov':
            download_images(image_link, file_name= file_name, folder= folder)
            print(file_name)
    
    return True


def fetch_nasa_epic(natural= True, folder= 'images'):
    url = f'https://api.nasa.gov/EPIC/api/'
    if natural: collection_type = 'natural'
    else: collection_type = 'enhanced'
    url = url + collection_type
    params = {'api_key' : NASA_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()

    for image in response.json():
        image_name = image['image']
        image_date = f"{image['date'].split('-')[0]}/{image['date'].split('-')[1]}/{image['date'].split('-')[2][:2]}" 
        image_link = f'https://epic.gsfc.nasa.gov/archive/{collection_type}/{image_date}/jpg/{image_name}.jpg'
        file_name = f'nasa_{collection_type}_{image_link.split("/")[-1]}'

        download_images(image_link, file_name= file_name, folder= folder)
        print(file_name)

    return True


def main():
    fetch_nasa_apod()

if __name__ == '__main__':
    main()