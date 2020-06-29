#!/bin/bash
clear
pip3 install --upgrade pip
pip3 install pyyaml
pip3 install PyMuPDF
pip3 install pillow
pip3 install requests
pip3 install beautifulsoup4
pip3 install progressbar2

sudo cp yameroo /usr/bin/yameroo
sudo chmod +x /usr/bin/yameroo

sudo cp animewalp.py /usr/lib/python3.8/
sudo cp hentaitopdf.py /usr/lib/python3.8/
sudo cp hentaidown.py /usr/lib/python3.8/

mkdir -p /home/$USER/yameroo/{animewallpapers,hentais,config}
cp config.yaml /home/$USER/yameroo/config/

clear
echo " __   __  _______  __   __  _______  ______    _______  _______
|  | |  ||   _   ||  |_|  ||       ||    _ |  |       ||       |
|  |_|  ||  |_|  ||       ||    ___||   | ||  |   _   ||   _   |
|       ||       ||       ||   |___ |   |_||_ |  | |  ||  | |  |
|_     _||       ||       ||    ___||    __  ||  |_|  ||  |_|  |
  |   |  |   _   || ||_|| ||   |___ |   |  | ||       ||       |
  |___|  |__| |__||_|   |_||_______||___|  |_||_______||_______|
    by Raudonkepuris

Beat covid-19, by beating your meat

Script combining features of anime-walpaper-changer, hentai-pics-to-pdf, quick-hentai-downloader

Before using read docs.md

Or write
yameroo -h"
