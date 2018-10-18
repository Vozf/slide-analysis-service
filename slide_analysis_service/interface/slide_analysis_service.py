import os

from slide_analysis_service.descriptors import all_descriptors_dict
from slide_analysis_service.interface.slide_descriptor import SlideDescriptor
from slide_analysis_service.interface.constants import DATABASE_DEFAULT_NAME,\
    DEFAULT_SIMILAR_AMOUNT
from slide_analysis_service.similarities import all_similarities_dict


class SlideAnalysisService:
    def __init__(self, descriptor_directory_path=os.getcwd() + '/' + DATABASE_DEFAULT_NAME,
                 similar_amount=DEFAULT_SIMILAR_AMOUNT):
        self.descriptor_directory_path = descriptor_directory_path
        self.similar_amount = similar_amount

    def get_slide(self, imagepath, descriptor):
        return SlideDescriptor(self, imagepath, descriptor)

    def get_directory(self):
        return self.descriptor_directory_path

    @staticmethod
    def get_descriptors():
        return all_descriptors_dict

    @staticmethod
    def get_similarities():
        return all_similarities_dict
