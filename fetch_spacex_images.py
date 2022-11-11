import argparse
import requests

from time import sleep
from base_functions import download_image

def get_spacex_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def fetch_spacex_images(launch_id, folder = 'images'):

    response_dict = get_spacex_request('https://api.spacexdata.com/v5/launches/')

    if launch_id > len(response_dict) -1: 
        raise ValueError(f'Non-existent launch. Total launches is {len(response_dict)-1}')

    current_id = response_dict[launch_id]['id']
    response_dict = get_spacex_request (f'https://api.spacexdata.com/v5/launches/{current_id}')
    images_sequense = response_dict['links']['flickr']['original']

    if len(images_sequense) < 1:
        raise ValueError(f"\nlaunch you have specified has no images\n")

    for index, image in enumerate(images_sequense, 1):
        index = '{:02d}'.format(index)
        name = f"spacex_{launch_id}_{index}.jpg"
        download_image(image, file_name= name, folder= folder)
        print (name)
    
    print (f"\nImage seqene downloading is done\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-id", help="Launch id", default= 12)

    args = parser.parse_args()
    print (f"\n{args.id} Launch. Getting links of images.")
    
    try:
        fetch_spacex_images(int(args.id))
    except ValueError as value:
        print(value)