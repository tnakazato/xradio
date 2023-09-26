import os
import re
import gdown
import shutil
import json

from prettytable import PrettyTable

gdown_ids = {
    'Antennae_South.cal.ms':'1f6a6hge0mDZVi3wUJYjRiY3Cyr9HvqZz',
    'Antennae_North.cal.ms':'1sASTyp4gr4PzWZwJr_ZHEdkqcYjF86BT',
    'demo_simulated.im':'1esOGbRMMEZXvTxQ_bdcw3PaZLg6XzHC5',
}


def check_download(name, folder, id):
    fullname = os.path.join(folder, name)
    if not os.path.exists(fullname):
        url = "https://drive.google.com/u/0/uc?id=" + id + "&export=download"
        gdown.download(url, fullname + ".zip")
        shutil.unpack_archive(filename=fullname + ".zip", extract_dir=folder)


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def gdown_data(ms_name, download_folder="."):
    assert (
        ms_name in gdown_ids
    ), "Measurement set not available. Available measurement sets are:" + str(
        gdown_ids.keys()
    )

    id = gdown_ids[ms_name]
    create_folder(download_folder)
    check_download(ms_name, download_folder, id)


def list_datasets():
    ms = []
    im = []
    for key, _ in gdown_ids.items():
        if key[-2:] == 'ms':
            ms.append(key)
        elif key[-2:] == 'im':
            im.append(key)
#        basename = key.split('.')[0]
#        file = ''.join((basename, '.json'))
#        path = os.path.dirname(__file__)
    table = PrettyTable()
    table.field_names = ["Measurement Table"] #  ,"Description"]
    table.align = "l"
    for key in ms:
        table.add_row([str(key)])
    print(table)
    table = PrettyTable()
    table.field_names = ["Image Table"] #  ,"Description"]
    table.align = "l"
    for key in im:
        table.add_row([str(key)])
    print(table)
