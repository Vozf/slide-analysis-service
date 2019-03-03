from setuptools import setup, find_packages

setup(
    name='slide_analysis_service',
    version='1.3',
    packages=find_packages(),
    install_requires=['matplotlib',
                      'numpy',
                      'scikit-image',
                      'scipy',
                      'tqdm',
                      ],
    url='',
    license='MIT',
    author='vozman',
    author_email='vozman@yandex.ru',
    description='',
    include_package_data=True,
)
