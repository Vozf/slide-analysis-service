import numpy as np
from slide_analysis_service.descriptors import COLOR_RANGE


class LinearSimilarity:
    def __init__(self):
        pass

    def compare(self, descriptors_array, hist):
        t = np.promote_types(hist.dtype, np.byte)
        distances = np.sum(np.abs(descriptors_array.astype(t) - hist.astype(t)), axis=1)
        return 1 - distances / 2