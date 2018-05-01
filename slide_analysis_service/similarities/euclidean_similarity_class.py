import numpy as np


class EuclideanSimilarity:
    def __init__(self):
        pass

    def compare(self, descriptors_array, hist):
        distances = np.linalg.norm(descriptors_array - hist, axis=1)
        return 1 - distances / np.sqrt(2)
