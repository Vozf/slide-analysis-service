from collections import OrderedDict

from slide_analysis_service.similarities.euclidean_similarity_class import EuclideanSimilarity
from slide_analysis_service.similarities.linear_similarity_class import LinearSimilarity
from slide_analysis_service.similarities.chi2_similarity_class import Chi2Similarity

all_similarities = [EuclideanSimilarity, LinearSimilarity, Chi2Similarity]
all_similarities_dict = OrderedDict([
    ("linear", LinearSimilarity),
    ("euclidean", EuclideanSimilarity),
    ("chi2", Chi2Similarity),
])
