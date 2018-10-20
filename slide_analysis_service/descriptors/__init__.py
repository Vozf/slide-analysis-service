from collections import OrderedDict

from slide_analysis_service.descriptors.adaptive_histogram_descriptor_class import \
    AdaptiveHistogramDescriptor
from slide_analysis_service.descriptors.histogram_descriptor_class import HistogramDescriptor
from slide_analysis_service.descriptors.test_descriptor_class import TestDescriptor
from slide_analysis_service.descriptors.co_occurrence_descriptor_class import CoOccurrenceDescriptor
from slide_analysis_service.descriptors.constants import COLOR_RANGE

all_descriptors = [TestDescriptor, HistogramDescriptor, AdaptiveHistogramDescriptor, CoOccurrenceDescriptor]
all_descriptors_dict = OrderedDict([
    ("histogram", HistogramDescriptor),
    ("adaptive_histogram", AdaptiveHistogramDescriptor),
    ("cooccurence", CoOccurrenceDescriptor),
])

