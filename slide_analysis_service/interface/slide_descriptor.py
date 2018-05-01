import os

from slide_analysis_service.descriptor_database_service import DescriptorDatabaseWriteService
from slide_analysis_service.search_service import SearchService
from slide_analysis_service.splitting_service import SplittingService
from slide_analysis_service.descriptors import all_descriptors_dict
from slide_analysis_service.similarities import all_similarities_dict

class SlideDescriptor:
    def __init__(self, slide_analysis_service, imagepath, descriptor, similarity):
        self.slide_analysis_service = slide_analysis_service
        self.imagepath = imagepath
        self.descriptor = all_descriptors_dict[descriptor]()
        self.similarity = all_similarities_dict[similarity]()
        if self.is_ready():
            self._connect_descriptor_base()

    def is_ready(self):
        return os.path.isfile(self._get_descriptorpath())

    def precalculate(self):
        split = SplittingService()
        stream = split.split_to_tiles(self.imagepath)

        descriptor_database_service = DescriptorDatabaseWriteService(
            self.descriptor,
            self.slide_analysis_service.get_directory())

        descriptor_database_service.create(stream)
        self._connect_descriptor_base()

    def _connect_descriptor_base(self):
        self.search_service = SearchService(self._get_descriptorpath(), self.imagepath)

    def _get_descriptorpath(self):
        directory = self.slide_analysis_service.get_directory()
        return DescriptorDatabaseWriteService.get_filepath(directory, self.imagepath,
                                                           self.descriptor)

    def find(self, rect):
        return self.search_service.find_similar(rect, self.slide_analysis_service.similar_amount, self.similarity)

