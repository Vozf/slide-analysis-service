from functools import reduce

import numpy
import openslide

from slide_analysis_service.constants.tile import (
    BASE_TILE_HEIGHT,
    BASE_TILE_WIDTH,
)
from slide_analysis_service.descriptors import all_descriptors
from slide_analysis_service.utils.tile_class import Tile


def _compose_util(f, g):
    return lambda *a, **kw: f(g(*a, **kw))


def compose(*fs):
    return reduce(_compose_util, fs)


def get_descriptor_class_by_name(name):
    return next((x for x in all_descriptors if x.__name__ == name), None)


def get_tile_from_coordinates(path, x_coord, y_coord, width, height):
    return Tile(x_coord, y_coord, width, height, openslide.open_slide(path)
                .read_region((x_coord, y_coord), 0, (width, height)))


def get_tiles_coords_from_indexes(indexes, step, img_width, img_height):
    num_cols = int(img_width / step)
    row = (indexes / num_cols).astype(int)
    column = indexes - row * num_cols
    y_coord = (row * step)
    x_coord = (column * step)
    coords = numpy.array([x_coord, y_coord]).T.tolist()
    return list(map(lambda arr: {"x": arr[0], "y": arr[1], "width": BASE_TILE_WIDTH,
                                 "height": BASE_TILE_HEIGHT}, coords))


def get_similarity_map_shape(img_w, img_h, step):
    return numpy.array([int(img_w / step), int(img_h / step)])
