from setuptools import setup, find_packages

setup(
    name='dscraper',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'fake-useragent',
        'selenium',
    ]
)