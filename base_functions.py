import os
from os import listdir
from os.path import isfile, join
import requests


def pick_all_imagefiles(mypath = 'images'):
    return [f'{mypath}/{f}' for f in listdir(mypath) if isfile(join(mypath, f))]


def download_image(link, file_name = None, folder = 'images'):
    response = requests.get(link)
    response.raise_for_status()

    if not os.path.exists(folder): os.makedirs(folder)
    if isinstance(file_name, type(None)):
        file_name = link.split('/')[-1]

    with open(f'{folder}/{file_name}', 'wb') as file:
        file.write(response.content)
        return True


if __name__ == '__main__':
    True