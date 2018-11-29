from concurrent.futures import ThreadPoolExecutor

import numpy
from PIL import Image
import pickle
import os

from slide_analysis_service.descriptors.constants import *


class AdaptiveHistogramDescriptor:
    def __init__(self, settings=None):
        self.settings = settings

        """
        Palette extraction process can be found in adaptive-color-palette.ipynb
        """
        with open(os.path.join(os.path.dirname(__file__), 'palette.out'), 'rb') as fp:
            palette_raw = pickle.load(fp)
        self.palette = Image.new('P', (16, 16))
        self.palette.putpalette(palette_raw)

    def calc(self, tile):
        img_conv = tile.data.convert('RGB').quantize(palette=self.palette)
        value = numpy.histogram(numpy.array(img_conv).flatten(), bins=numpy.arange(0, COLOR_RANGE + 1))[0]
        value = value / numpy.sum(value)
        return value

    def get_descriptor_object(self, tile_stream):
        with ThreadPoolExecutor() as executor:
            descr_arr = list(executor.map(self.calc, tile_stream))
            return {
                "descriptor_array": descr_arr
            }

    @staticmethod
    def name():
        return 'Adaptive Color histogram'
