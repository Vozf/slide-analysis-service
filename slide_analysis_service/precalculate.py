# Use this script to precalculate descriptors for slides.
# Example: python precalculate.py path/to/folder

import glob
import sys
from pathlib import Path
from openslide import OpenSlide
from tqdm import tqdm

from slide_analysis_service import SlideAnalysisService


def precalculate(path, recursive=False):
    saserv = SlideAnalysisService()
    img_paths = glob.glob(str(Path(path) / '**' / '*.*'), recursive=recursive)
    print(f'Found total {len(img_paths)} files'
          f' and {len(SlideAnalysisService.get_descriptors().keys())} descriptors')
    for path in tqdm(img_paths):
        if not OpenSlide.detect_format(path):
            return

        for descriptor in SlideAnalysisService.get_descriptors().keys():
            slide = saserv.get_slide(path, descriptor)
            if not slide.is_ready():
                slide.precalculate()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise RuntimeError('Number of arguments should be one. Please pass path to slides folder')
    path = sys.argv[1]
    precalculate(path, recursive=True)
