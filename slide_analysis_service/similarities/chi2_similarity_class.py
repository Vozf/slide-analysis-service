import numpy as np

from slide_analysis_service.descriptors import COLOR_RANGE


class Chi2Similarity:
    def __init__(self):
        self.eps = 0.00000001

    def compare(self, descriptors_array, hist):
        distances = 0.5 * np.sum((descriptors_array - hist) ** 2 / (descriptors_array + hist + self.eps), axis=1)
        return 1 - distances

    @staticmethod
    def name():
        return 'Chi-squared'
