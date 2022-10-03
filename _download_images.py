import argparse
import requests
import os


def download_images(link, file_name = None, folder = 'images'):
    response = requests.get(link)
    response.raise_for_status()

    if not os.path.exists(folder): os.makedirs(folder)
    if isinstance(file_name, type(None)):
        file_name = link.split('/')[-1]

    with open(f'{folder}/{file_name}', 'wb') as file:
        file.write(response.content)
        return True


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("image_link", help="image adress for download")
    args = parser.parse_args()
    
    if download_images (args.image_link): print ("Download is done!")

if __name__ == '__main__':
    main()