import setuptools

import slide_analysis_service

with open('requirements.txt') as file:
    INSTALL_REQUIRES = [l.strip() for l in file.readlines() if l]

setuptools.setup(name='slide_analysis_service',
                 version=slide_analysis_service.__version__,
                 url='https://github.com/Vozf/slide-analysis-service/',
                 license='???',  # todo: add
                 description='???',  # todo: add
                 packages=setuptools.find_packages(exclude=['doc']),
                 scripts=[],
                 install_requires=INSTALL_REQUIRES,
                 )
