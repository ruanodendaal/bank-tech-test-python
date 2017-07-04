try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Bank tech test in Python',
    'author': 'Ruan Odendaal',
    'url': '',
    'download_url': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['banking'],
    'scripts': [],
    'name': 'banking'
}

setup(**config)
