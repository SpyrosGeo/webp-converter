#!/usr/bin/python3
import sys
import requests
from PIL import Image
import random
import string
import os
from termcolor import colored,cprint
if(len(sys.argv) > 1):
    link = sys.argv[1]
else: link = '-h'

PATH = '/home/thatguy/Downloads/sterea/'
def show_list():
    return  os.listdir(PATH)

def clear_folder():
    dir_list =show_list()
    if (len(dir_list)==0):
        cprint('Directory is Empty','white','on_red')
        return
    for file in dir_list:
        os.remove(f'{PATH}{file}')
    cprint('Files removed!','black','on_cyan')


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
def save_image_from_url():
    try:
        img_data = requests.get(link).content
        with open('temp.webp','wb') as handler:
            handler.write(img_data)
    except:
        cprint(f'Error while processing URL:{link}','white','on_red')


def convert_to_jpg():
    clear_folder()
    name = get_random_string(8)
    im = Image.open('temp.webp').convert('RGB')
    im.save(f'{PATH}{name}.jpg','jpeg')
    cprint(f'file ${name}.jpg was saved','wihite','on_cyan')

if(link=="-h" or len(sys.argv)==0):
    text = colored("Webp to jpg converter","green",attrs=["reverse","blink"])
    print(text)
    print("========")
    cprint("Usage: Run the script with the image URL as argument","white","on_black")
    print("========")
    cprint("Available Flags:","white","on_black")
    cprint("-h: Help ","white","on_black")
    cprint("-l: Prints all files on directory","white","on_black")
    cprint("-d: Deletes all files on directory","white","on_black")

elif(link=="-l"):
    dir_list =  show_list()
    print('Files:',dir_list)
elif(link=="-d"):
    clear_folder()

else:
    save_image_from_url()
    convert_to_jpg()
