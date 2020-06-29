import requests
from bs4 import BeautifulSoup
import os
import glob
import getpass
import webbrowser
import ctypes

def get_image(set_img, url):
    picture_page = soup_from_url(url).find("a", {"class" : "preview"}).get("href")
    image_url = soup_from_url(picture_page).find("img", {"id" : "wallpaper"}).get("src")

    img_data = requests.get(image_url).content

    image_path = get_path() + picture_page.split("/")[-1] + ".jpg"
  
    with open(image_path, "wb") as handler:
        handler.write(img_data)

    print("Link to the image page : " + picture_page)

    if set_img:
        set_image(image_path)
    elif not set_img:
        webbrowser.open(picture_page)

def set_image(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

def set_last_image():
    path = get_path() + "*"
    list_of_files = glob.glob(path)
    latest_file = max(list_of_files, key=os.path.getctime)
    set_image(latest_file)

def get_path():
    path = "C:\\Program Files\\yameroo\\animewallpapers\\"
    return path

def soup_from_url(url):
    html = requests.get(url).content
    return BeautifulSoup(html, features="html.parser")
