from os import listdir
from os.path import isfile, join
from pathlib import Path

import requests
import os


def pick_all_imagefiles(folder = 'images'):
    return [ Path.cwd()/folder/filename for filename in listdir(folder) if isfile(join(folder, filename))]


def download_image(link, file_name, folder = 'images'):
    response = requests.get(link)
    response.raise_for_status()

    os.makedirs(folder, exist_ok= True)
    with open(Path.cwd()/folder/file_name, 'wb') as file:
        file.write(response.content)
        return True