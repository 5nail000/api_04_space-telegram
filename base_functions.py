from os import listdir
from os.path import isfile, join
from pathlib import Path

import requests
import os


def pick_all_imagefiles(mypath = 'images'):
    return [ Path.cwd()/mypath/f for f in listdir(mypath) if isfile(join(mypath, f))]


def download_image(link, file_name = "", folder = 'images'):
    response = requests.get(link)
    response.raise_for_status()

    os.makedirs(folder, exist_ok= True)
    if len(file_name) == 0:
        file_name = link.split('/')[-1]

    with open(Path.cwd()/folder/file_name, 'wb') as file:
        file.write(response.content)
        return True