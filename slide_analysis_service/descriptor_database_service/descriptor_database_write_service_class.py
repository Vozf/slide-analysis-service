import os
import numpy


class DescriptorDatabaseWriteService:
    def __init__(self, descriptor, path_to_descriptors):
        self.descriptor = descriptor

        if path_to_descriptors[-1] == '/':
            self.base_path = path_to_descriptors
        else:
            self.base_path = path_to_descriptors + '/'

    @staticmethod
    def _dump_obj(file, obj):
        return numpy.save(file, obj)

    @staticmethod
    def get_filepath(base_path, image_path, descriptor):
        image_name = os.path.basename(image_path)
        human_readable = True
        if human_readable:
            return base_path + '/' + descriptor.__class__.__name__ + " " +\
                   image_name[0:image_name.find('.')] + ".npy"
        else:
            return str(hash(image_path + '/' + descriptor)) + ".npy"

    #todo move making of descr_filename somewhere else, so it can be accessed and modified
    def create(self, tile_stream):
        split = tile_stream.splitting_service
        image_path = split.path
        length = len(tile_stream)
        descr_filename = self.get_filepath(self.base_path, image_path,
                                           self.descriptor)

        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)

        info_obj = self.generate_database_info(image_path, length, split.tile_width,
                                               split.tile_height, split.step,
                                               split.width, split.height)

        descr_obj = self.descriptor.get_descriptor_object(tile_stream)
        descr_array = descr_obj["descriptor_array"]
        if "descriptor_configuration" in descr_obj:
            info_obj["descriptor_configuration"] = descr_obj["descriptor_configuration"]

        with open(descr_filename, 'wb') as file:
            self._dump_obj(file, info_obj)
            self._dump_obj(file, descr_array)

        return descr_filename

    def generate_database_info(self, image_path, length, tile_w, tile_h, step, img_w, img_h):
        return {
            "descriptor_name": self.descriptor.__class__.__name__,
            "descriptor_params": self.descriptor.settings,
            "image_path": image_path,
            "length": length,
            "tile_width": tile_w,
            "tile_height": tile_h,
            "step": step,
            "img_width": img_w,
            "img_height": img_h
        }
