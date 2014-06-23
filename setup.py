from setuptools import find_packages, setup

setup(
    name='TracHamsterPlugin', version='1.0.0',
    packages=find_packages(exclude=['*.tests*']),
    install_requires=[],
    entry_points = {
        'trac.plugins': [
            'trachamsterplugin = trachamsterplugin',
        ],
    },
)