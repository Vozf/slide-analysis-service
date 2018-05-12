import os

from slide_analysis_service.constants.tile import BASE_TILE_WIDTH, BASE_TILE_HEIGHT
from slide_analysis_service.descriptors import all_descriptors
from slide_analysis_service.interface.slide_descriptor import SlideDescriptor
from slide_analysis_service.interface.constants import DATABASE_DEFAULT_NAME,\
    DEFAULT_SIMILAR_AMOUNT
from slide_analysis_service.similarities import all_similarities
from slide_analysis_service.utils.functions import get_tile_from_coordinates


class SlideAnalysisService:
    def __init__(self, descriptor_directory_path='C:\Study\Course\slide_analysis\web_slide_analysis\slide-analysis-service\slide_analysis_service' + '/' + DATABASE_DEFAULT_NAME,
                 similar_amount=DEFAULT_SIMILAR_AMOUNT):
        self.descriptor_directory_path = descriptor_directory_path
        self.similar_amount = similar_amount

    def get_slide(self, imagepath, descriptor, similarity):
        return SlideDescriptor(self, imagepath, descriptor, similarity)

    def get_directory(self):
        return self.descriptor_directory_path

    def get_tile(self, imagepath, x_coord, y_coord):
        return get_tile_from_coordinates(imagepath, x_coord, y_coord, BASE_TILE_WIDTH, BASE_TILE_HEIGHT).data

    @staticmethod
    def get_descriptors():
        return all_descriptors

    @staticmethod
    def get_similarities():
        return all_similarities
