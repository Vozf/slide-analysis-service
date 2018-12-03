# Use this script to precalculate descriptors for slides.
# Example: python precalculate.py path/to/folder

import glob
import sys
from pathlib import Path

from slide_analysis_service import SlideAnalysisService

if len(sys.argv) != 2:
    raise RuntimeError('Number of arguments should be one. Please pass path to slides folder')

path = sys.argv[1]

saserv = SlideAnalysisService()
images = glob.glob(str(Path(path) / '**' / '*.tif'), recursive=True)
print(f'Found total {len(images)} images'
      f' and {len(SlideAnalysisService.get_descriptors().keys())} descriptors')
for img in images:
    for descriptor in SlideAnalysisService.get_descriptors().keys():
        slide = saserv.get_slide(img, descriptor)
        print(img)
        if not slide.is_ready():
            slide.precalculate()

