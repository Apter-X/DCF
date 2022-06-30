from setuptools import find_packages, setup

setup(
    name='clean-panda',
    packages=find_packages(include=['clean_panda']),
    version='0.1.2',
    description='Data cleaner based on pandas',
    author='Iliass Raihani',
    license='MIT',
    install_requires=['pandas', 'numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.2'],
    test_suite='tests',
)
