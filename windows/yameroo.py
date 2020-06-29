import animewalp as wp
import hentaitopdf as htp
import hentaidown as d
import argparse
import yaml
import getpass
import os

def get_config(dic):
    values = []

    config = open("C:\Program Files\yameroo\config\config.yaml")
    contents = yaml.load(config, Loader=yaml.FullLoader)

    for k, v in contents[dic].items():
        values.append(v)

    if dic == "animewalp":
        categories, purity, resolutions, sorting = values

        url = "https://wallhaven.cc/search?categories=" + categories + "&purity=" + purity + "&resolutions=" + resolutions + "&sorting=" + sorting + "&order=desc"
        return url

    elif dic == "hentai":
        return values[0]


def Main():
    parser = argparse.ArgumentParser(description = "For more information read docs.md file")
    parser.add_argument(
        "-n",
        "--getnew",
        action = "store_true",
        required = False,
        help = "get new wallpaper and apply as desktop background"
        )
    parser.add_argument(
        "-g",
        "--get",
        action = "store_true",
        required = False,
        help = "get a new wallpaper, without applying as desktop background"
        )
    parser.add_argument(
        "-a",
        "--apply",
        action = "store_true",
        required = False,
        help = "apply last image you've downloaded"
        )
    parser.add_argument(
        "-m",
        "--make",
        nargs = 2,
        metavar = ('path', 'name'),
        required = False,
        help = "provide abosule or relative path to a folder with your hentai and a name you want to give for the generated pdf file"
        )
    parser.add_argument(
        "-d",
        "--download",
        nargs = 1,
        metavar = 'ID',
        required = False,
        help = "provide hentai ID to download your hentai"
        )
    args = parser.parse_args()

    if args.getnew:
        url = get_config("animewalp")
        wp.get_image(True, url)
        quit()
    elif args.get:
        url = get_config("animewalp")
        wp.get_image(False, url)
        quit()
    elif args.apply:
        wp.set_last_image()
        quit()
    elif args.download:
        save_path = get_config("hentai")
        d.generate_hentai(args.download[0], save_path)
        quit()
    elif args.make:
        path = args.make[0]
        name = args.make[1]

    try:
        path
        name
    except NameError:
        name, path = None

    if name and path != None:
        save_path = get_config("hentai")
        if path.endswith("\\") == False:
            path = path + "\\"
        htp.make_pdf(path, name, save_path)
        quit()

if __name__ == "__main__":
    Main()
