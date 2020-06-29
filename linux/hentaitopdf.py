#! /usr/bin/env python3

import fitz
import glob
from PIL import Image
import argparse
import os

def make_pdf(path, name, save_path):
    document = fitz.open()

    extensions = ["*.jpg", "*.png"]
    image_list = []

    for extension in extensions:
        for file in glob.glob(path + extension):
            image_list.append(file)

    image_list.sort()

    for image in image_list:
        im = Image.open(image)
        w, h = im.size
        new_page = document.newPage(width = w, height = h)
        page = document[-1]
        page.insertImage((0, 0, w, h), image)
        im.close()

    document.save(save_path + name)
    document.close()
