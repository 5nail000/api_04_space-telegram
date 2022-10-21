from urllib.parse import urlparse

from base_functions import *


def fetch_nasa_epic(natural= True, folder= 'images'):
    url = f'https://api.nasa.gov/EPIC/api/'
    if natural: collection_type = 'natural'
    else: collection_type = 'enhanced'
    url = f'{url}{collection_type}'
    params = {'api_key' : NASA_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()

    for image in response.json():
        image_name = image['image']
        image_date = f"{image['date'].split('-')[0]}/{image['date'].split('-')[1]}/{image['date'].split('-')[2][:2]}" 
        image_link = f'https://epic.gsfc.nasa.gov/archive/{collection_type}/{image_date}/jpg/{image_name}.jpg'
        file_name = f'nasa_{collection_type}_{image_link.split("/")[-1]}'

        download_image(image_link, file_name= file_name, folder= folder)
        print(file_name)

    return True


if __name__ == '__main__':

    load_dotenv()
    NASA_KEY = os.getenv('NASA_KEY')

    fetch_nasa_epic()