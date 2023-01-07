#!/usr/bin/python3.9
import sys
import requests
from PIL import Image
import random
import string
import os
link = sys.argv[1]
PATH = '/home/thatguy/Downloads/sterea/'
def show_list():
    return  os.listdir(PATH)

def clear_folder():
    for file in dir_list:
        os.remove(f'{PATH}{file}')
    print('Files removed!')


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
def save_image_from_url():
    img_data = requests.get(link).content
    with open('temp.webp','wb') as handler:
        handler.write(img_data)


def convert_to_jpg():
    name = get_random_string(8)
    im = Image.open('temp.webp').convert('RGB')
    im.save(f'{PATH}{name}.jpg','jpeg')


if(link=="-l"):
    dir_list =  show_list()
    print('Files:',dir_list)
elif(link=="-d"):
    dir_list =show_list()
    clear_folder()

else:
    save_image_from_url()
    convert_to_jpg()
