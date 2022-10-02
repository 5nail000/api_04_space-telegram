import requests
import pprint
import os
from urllib.parse import urlparse

pp = pprint.PrettyPrinter(indent=4)
folder = 'images'
NASA_KEY = 'vmQJpqWaEtt1fW6ZcQfQCG97qsrvI7KwY5aNU4Hd'


def get_file_extension (link):
    print(link.split(".")[-1])


def download_images(folder, link, file_name):
    response = requests.get(link)
    response.raise_for_status()

    if not os.path.exists(folder): os.makedirs(folder)

    with open(f'{folder}/{file_name}', 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(folder):

    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(url)
    response.raise_for_status()

    order = -37
    launch_id = len(response.json()) + order
    if launch_id > len(response.json()): launch_id - len(response.json())

    current_id = response.json()[order]['id']
    url = f'https://api.spacexdata.com/v5/launches/{current_id}'

    response = requests.get(url)
    response.raise_for_status()
    images_sequense = response.json()['links']['flickr']['original']

    for index, image in enumerate(images_sequense, 1):
        name = f'spacex_{launch_id}_{index}.jpg'
        download_images(folder, image, name)


def fetch_nasa_apod(folder):
    url = f'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key' : NASA_KEY,
        'count': 50
    }
    response = requests.get(url, params=params)
    response.raise_for_status()

    for image in response.json():
        image_link = image['url']
        parsed_link = urlparse(image_link)
        file_name = f'nasa_apod_{image["date"]}_{parsed_link.path.split("/")[-1]}'
        if parsed_link.hostname =='apod.nasa.gov':
            print(f'file_name: {file_name}')
            download_images(folder, image_link, file_name)


def fetch_nasa_epic(folder, natural = True):
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

        print (file_name)
        download_images(folder, image_link, file_name)


    

#fetch_spacex_last_launch(folder)
#fetch_nasa_apod(folder)
fetch_nasa_epic(folder, False)