from _download_images import *
import argparse
import requests

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

    for index, image in enumerate(images_sequense, 1):
        if len(str(len(images_sequense)))>len(str(index)): 
            zeroes = '0' * (len(str(len(images_sequense))) - len(str(index)))
        else:
            zeroes = ""

        name = f'spacex_{launch_id}_{zeroes}{index}.jpg'
        download_images(image, file_name= name, folder= folder)
        print (name)
    
    return True


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("id", help="Launch id")
    args = parser.parse_args()
    print (f"{args.id} Launch. Getting links of images.")

    if fetch_spacex_images(int(args.id)): print (f"Image seqene downloading is done")

if __name__ == '__main__':
    main()