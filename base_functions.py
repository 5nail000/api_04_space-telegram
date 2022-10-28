import os
from os import listdir
from os.path import isfile, join
import requests


def pick_all_imagefiles(mypath = 'images'):
    return [f'{mypath}/{f}' for f in listdir(mypath) if isfile(join(mypath, f))]


def download_image(link, file_name = "", folder = 'images'):
    response = requests.get(link)
    response.raise_for_status()

    os.makedirs(folder, exist_ok= True)
    if len(file_name) == 0:
        file_name = link.split('/')[-1]

    with open(f'{folder}/{file_name}', 'wb') as file:
        file.write(response.content)
        return True