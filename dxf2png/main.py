"""
Copyright (c) 2021 Nikita Letov (letovnn@gmail.com)
Distributed under the MIT software license, see the accompanying
file COPYING or http://www.opensource.org/licenses/mit-license.php.

This script converts DXF files to PNG file.
Usage:
    python main.py -i input.dxf -o output.png
or
    python main.py --input input.dxf --output output.png
"""
import os
import cv2
import json
import ezdxf
import shutil
import imutils
import matplotlib.pyplot as plt
from datetime import datetime
from natsort import natsort_keygen
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import argparse

natsort_key = natsort_keygen()

SETTINGS_FILE = 'settings.txt'

try:
    file = open(SETTINGS_FILE, 'r')
except FileNotFoundError:
    with open(SETTINGS_FILE, 'w') as file:
        file.write('Batch.json')
with open(SETTINGS_FILE, 'r') as f:
    Data_JSON = 'Batches/' + f.read()

Data_JSON_Contents = []

BATCHES = []
NON_BATCHES = ['NON_BATCH']

file_names = []
image_locations = []
quantities = []
description = []
checkmarked = []
materials = []
batch_name_list = []
batch_index_val = []

batch_group_box_GUI = []

company = 'GRAD4 Inc.'
title = 'DXF to PNG'
version = 'v0.2'

latest_update_date = datetime(2020, 11, 27, 2, 21, 6)
latest_update_date_formated = latest_update_date.strftime(
    "%A %B %d %Y at %X%p")

'''
A converter job class. Initializes the convertion and its parameters.

Attributes:
    file : str
        input file name
    img_res : int
        output image resolution in dots per inch (DPI)
'''
class Converter():
    def __init__(self, img_res):
        self.default_img_format = '.png'
        self.img_res = img_res
    '''
    A function that handles the actual convertion.

    Parameters:
        path : str
            input file path
        save_to : str
            output file name
    '''
    def convert_dxf2img(self, path, save_to):
        # Checking for positive output resolution
        if self.img_res <= 0:
            raise ValueError('The file resolution must be a positive number')
        if not os.path.exists(path):
            raise ValueError('File does not exist')
        # Checking the file extentions
        input_extention = os.path.splitext(input_filename)[1].lower()
        if input_extention != '.dxf':
            raise ValueError('Incorrect input file format: the input file must be DXF')
        output_extention = os.path.splitext(output_filename)[1].lower()
        if output_extention != '.png':
            raise ValueError('Incorrect output file format: the output file mush be PNG')
        # Reading the DXF file
        doc = ezdxf.readfile(path)
        msp = doc.modelspace()
        auditor = doc.audit()
        if len(auditor.errors) != 0: # Checking for reading errors
            # TODO: This is terrible from the user feedback point of view.
            # It was done by Qt previously.
            return
        fig = plt.figure()
        ax = fig.add_axes([0, 0, 1, 1])
        ctx = RenderContext(doc)
        ctx.set_current_layout(msp)
        ctx.current_layout.set_colors(bg = '#FFFFFF')
        # TODO: The following line hardcodes the lineweight which causes some convertions
        # look weird. Sad...
        out = MatplotlibBackend(ax, params={"lineweight_scaling": 6})
        Frontend(ctx, out).draw_layout(msp, finalize = True)
        fig.savefig(save_to, dpi = self.img_res)
        im = cv2.imread(save_to)
        hei, wid, c = im.shape
        if hei > wid:
            region = imutils.rotate_bound(im, 90)
            cv2.imwrite(save_to, region)
        plt.close(fig)

# Cleans working directories if called
def clear_folders(folders):
    for folder in folders:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

def load_batches(*args):
    global Data_JSON_Contents
    for j in args:
        j.clear()
    with open(Data_JSON) as file:
        Data_JSON_Contents = json.load(file)
        for info in Data_JSON_Contents:
            for batch in info:
                if batch != 'NON_BATCH':
                    args[0].append(batch)
        args[0].append('NON_BATCH')

if __name__ == '__main__':
    # if images directory doesn't exist we create it
    if not os.path.exists('Images'): os.makedirs('Images')
    if not os.path.exists('Print'): os.makedirs('Print')
    if not os.path.exists('Capture'): os.makedirs('Capture')
    if not os.path.exists('Batches'): os.makedirs('Batches')
    if not os.path.exists('Backups'): os.makedirs('Backups')
    # if data.json file doesn't exist, we create it
    if not os.path.isfile(Data_JSON):
        with open(Data_JSON, 'w+') as f:
            f.write('[{"NON_BATCH":[]}]')
    clear_folders(['Capture', 'Print'])
    # Load data file
    load_batches(BATCHES)
    SAVED_DATA_JSON_FILES = os.listdir('Batches/')
    parser = argparse.ArgumentParser(description = 'This application allows converting DXF to PNG')
    parser.add_argument("-i", dest = "input_filename",
                    help = "Input DXF file name", metavar = "FILE")
    parser.add_argument("-o", dest = "output_filename",
                    help = "Output PNG file name", metavar = "FILE")
    args = parser.parse_args()
    input_filename = str(args.input_filename)
    output_filename = str(args.output_filename)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    files = [input_filename]
    converter = Converter(img_res = 300)
    print(f'Converting DXF file {dir_path}/{input_filename} to PNG ...')
    converter.convert_dxf2img(path = dir_path + "/" + input_filename,
                              save_to = dir_path + "/" + output_filename)
    print('Conversion is successful')
    print(f'File written to {dir_path}/{output_filename}')
