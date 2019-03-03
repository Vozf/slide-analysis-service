import numpy
import skimage.feature as skf

from concurrent.futures import ThreadPoolExecutor


class CoOccurrenceDescriptor:
    def __init__(self, settings=(3, 2, 3)):
        self.settings = settings
        self.r_mod, self.g_mod, self.b_mod = settings

    def _count_mat(self, tile):
        arr = numpy.array(tile.data)
        arr = (arr[:, :, 0] >> (8 - self.r_mod) << (self.g_mod + self.b_mod)) \
              + (arr[:, :, 1] >> (8 - self.g_mod) << self.b_mod) \
              + (arr[:, :, 2] >> (8 - self.b_mod))
        levels = 2 ** (self.r_mod + self.g_mod + self.b_mod)
        mat = skf.greycomatrix(arr, [1], [0, numpy.pi / 4, numpy.pi / 2, 3 * numpy.pi / 4],
                               levels=levels)
        s = numpy.sum(mat, axis=3)[:, :, 0]
        return (s + s.T).reshape([levels * levels])

    def normalize(self, vec):
        return vec / numpy.sum(vec)

    def _calc(self, tile):
        vect = self._count_mat(tile)
        rate = 0.005 * (8 * tile.width * tile.height - 6 * tile.width - 6 * tile.height + 4)
        indices = numpy.where(vect >= rate)[0]
        value = self.normalize(vect[indices])
        return [indices, value]

    def calc(self, tile, configuration):
        mat = self._count_mat(tile)
        res = self.normalize(mat[configuration["indices"]])
        return res

    def get_descriptor_object(self, tile_stream):
        with ThreadPoolExecutor() as executor:
            descr_obj = list(executor.map(self._calc, tile_stream))
            indices = numpy.empty([0], dtype=numpy.int32)
            for descr in descr_obj:
                indices = numpy.union1d(indices, descr[0])
            descr_arr = numpy.zeros([len(descr_obj), len(indices)])
            for i in range(len(descr_obj)):
                descr_arr[i][numpy.searchsorted(indices, descr_obj[i][0])] = descr_obj[i][1]
            return {
                "descriptor_array": descr_arr,
                "descriptor_configuration": {
                    "indices": indices
                }
            }

    @staticmethod
    def name():
        return 'Color Co-occurence'
