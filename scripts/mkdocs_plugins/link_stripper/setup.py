from setuptools import setup, find_packages

setup(
    name='link-stripper',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'mkdocs==1.6.0',
        'beautifulsoup4==4.12.3'
    ]
)

