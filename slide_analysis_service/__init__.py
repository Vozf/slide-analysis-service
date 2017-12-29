__version__ = '1.0'

from slide_analysis_service.interface import SlideAnalysisService


if __name__ == '__main__':
    default_img = '/home/vozman/Pictures/46433.svs'
    print('Test')

    slideAnalysisService = SlideAnalysisService()
    print(slideAnalysisService.get_descriptors())
    print(slideAnalysisService.get_similarities())
    print(slideAnalysisService.get_directory())
    slide = slideAnalysisService.get_slide(default_img,
                                           slideAnalysisService.get_descriptors()[1]())
    print(slide)
    print(slide.is_ready())
    if not slide.is_ready():
        slide.precalculate()
    similar = slide.find((0, 0, 256, 256), slideAnalysisService.get_similarities()[1]())
    print(similar)

    print('All done')