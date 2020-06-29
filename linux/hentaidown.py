#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from PIL import Image
import fitz
import getpass
import os
from progressbar import ProgressBar
import argparse

pbar = ProgressBar()

def generate_hentai(id, path):

    document = fitz.open()

    pages, gallery_page = get_info("https://nhentai.net/g/" + id + "/1")

    img_path = path + "quick-hentai-down-img-rdnkprs-script"

    img_type = gallery_page[-4:]
    gallery_page = gallery_page[:-5]

    for i in pbar(range(int(pages))):
        url = gallery_page + str(i+1) + img_type
        data = requests.get(url).content
        with open(img_path, "wb") as handler:
            handler.write(data)
        im = Image.open(img_path)
        w, h = im.size
        document.newPage(width = w, height = h)
        page = document[-1]
        page.insertImage((0, 0, w, h), img_path)
        im.close()

    os.remove(img_path)
    document.save(path + id)
    document.close()

def get_info(url):
    page = soup_from_url(url)
    number = page.find("span", {"class" : "num-pages"}).getText()
    gallery_page = page.find("section", {"id" : "image-container"}).find("a", recursive=False).find("img", recursive=False).get("src")
    return number, gallery_page

def soup_from_url(url):
    html = requests.get(url).content
    return BeautifulSoup(html, features="html.parser")
