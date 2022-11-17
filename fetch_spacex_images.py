import argparse
import requests

from base_functions import download_image


def get_spacex_request(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_spacex_images(launch_id, folder='images'):
    api_url = 'https://api.spacexdata.com/v5/launches'
    response_dict = get_spacex_request(api_url)

    if launch_id > len(response_dict) - 1:
        existent_text = 'Non-existent launch. Total launches is'
        print(f'{existent_text} {len(response_dict)-1}')
        return

    current_id = response_dict[launch_id]['id']
    response_dict = get_spacex_request(f'{api_url}/{current_id}')
    images_sequense = response_dict['links']['flickr']['original']

    if len(images_sequense) < 1:
        print("\nlaunch you have specified has no images\n")
        return

    for index, image in enumerate(images_sequense, 1):
        index = '{:02d}'.format(index)
        name = f"spacex_{launch_id}_{index}.jpg"
        download_image(image, file_name=name, folder=folder)
        print(name)

    print("\nImage seqene downloading is done\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-id", help="Launch id", default=12)

    args = parser.parse_args()
    print(f"\n{args.id} Launch. Getting links of images.")

    fetch_spacex_images(int(args.id))
