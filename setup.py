from setuptools import setup
import os


if os.path.isfile('requirements.txt'):
    with open('requirements.txt', 'r') as requirements_file:
        install_requires = requirements_file.read().splitlines()
for package in install_requires:
    if package.startswith('git'):
        pname = package.split('/')[-1].split('.')[0]
        install_requires[install_requires.index(package)] = pname + ' @ ' + package
setup(
    name='timsMAP',
    version='1.0.0',
    url='https://github.com/rashepherd/timsMAP',
    license='Apache License',
    author='Robert A. Shepherd',
    author_email='rashephe@ucsc.edu',
    packages=['bin'],
    entry_points={'console_scripts': ['get_feature_intensities=bin.run:run',
                                      'get_batch_feature_intensities=bin.run_batch:run',
                                      'get_feature_map=bin.run_batch_map:run']},
    install_requires=install_requires
)
