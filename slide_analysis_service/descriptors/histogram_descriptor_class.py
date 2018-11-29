from concurrent.futures import ThreadPoolExecutor

import numpy

from slide_analysis_service.descriptors.constants import *


class HistogramDescriptor:
    def __init__(self, settings=(3, 2, 3)):
        self.settings = settings
        (self.r_mod, self.g_mod, self.b_mod) = settings

    def calc(self, tile):
        arr = numpy.array(tile.data)
        value = numpy.histogram((numpy.ravel(arr[:, :, 0]) >> (8 - self.r_mod) << (8 - self.r_mod))
                                + (numpy.ravel(arr[:, :, 1]) >> (8 - self.b_mod) << self.g_mod)
                                + (numpy.ravel(arr[:, :, 2]) >> (8 - self.g_mod)),
                                bins=numpy.arange(0, COLOR_RANGE + 1))[0]
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
        return 'Color histogram'
