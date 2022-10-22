import argparse
import requests

from time import sleep
from base_functions import download_image


def fetch_spacex_images(launch_id, folder = 'images'):

    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(url)
    response.raise_for_status()

    if launch_id > len(response.json()): 
        print (f'Non-existent launch. Total launches is {len(response.json())}')
        return False

    current_id = response.json()[launch_id]['id']
    url = f'https://api.spacexdata.com/v5/launches/{current_id}'
    response = requests.get(url)
    response.raise_for_status()
    images_sequense = response.json()['links']['flickr']['original']

    if len(images_sequense) == 0:
        return False

    for index, image in enumerate(images_sequense, 1):
        if len(str(len(images_sequense)))>len(str(index)): 
            zeroes = '0' * (len(str(len(images_sequense))) - len(str(index)))
        else:
            zeroes = ""

        name = f'spacex_{launch_id}_{zeroes}{index}.jpg'
        download_image(image, file_name= name, folder= folder)
        print (name)
    
    return True


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="Launch id")

    id = 0
    try:
        args = parser.parse_args()
        print (f"\n{args.id} Launch. Getting links of images.")
        id = int(args.id)
        
    except:
        print ('\nLets get first images (Launch ID= 12)')
        id = 12

    if fetch_spacex_images(id): 
        print (f"\nImage seqene downloading is done\n")
    else:
        print (f"\nlaunch you have specified has no images\n")
    
    sleep(1)