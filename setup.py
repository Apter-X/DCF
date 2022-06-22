from setuptools import find_packages, setup

setup(
    name='DCF',
    packages=find_packages(include=['classes']),
    version='0.1.0',
    description='Data cleaner based on pandas',
    author='Iliass Raihani',
    license='MIT',
    install_requires=['pandas', 'numpy']
)
