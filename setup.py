from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='PyGB',
    version='0.0.1',
    author= 'Heru Handika & Jacob A. Esselstyn',
    author_email= 'hhandika.us@gmail.com',
    description= 'A command-line application to prepare GenBank sequence submission',
    long_description= long_description,
    long_description_content_type='text/markdown',
    # url='https://github.com/hhandika/',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
    ],
    python_requires='>=3.6',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pygb=pgb.py_gb_preparator:main
    ''',
)