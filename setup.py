from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name = 'Manga Manager',
    version = '1.0.0',
    packages = find_packages(),
    install_requires=[
        'click',
        'typing_extensions',
        'colorama',
        'watchdog'
    ],
    entry_points = '''
        [console_scripts]
        tachi=ManageAnime:ManageMain
    '''
)