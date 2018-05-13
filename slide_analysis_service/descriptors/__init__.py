from collections import OrderedDict

from slide_analysis_service.descriptors.histogram_descriptor_class import HistogramDescriptor
from slide_analysis_service.descriptors.test_descriptor_class import TestDescriptor
from slide_analysis_service.descriptors.co_occurrence_descriptor_class import CoOccurrenceDescriptor
all_descriptors = [TestDescriptor, HistogramDescriptor, CoOccurrenceDescriptor]
all_descriptors_dict = OrderedDict([
    ("histogram", HistogramDescriptor),
    ("cooccurence", CoOccurrenceDescriptor),
])

from slide_analysis_service.descriptors.constants import COLOR_RANGE
