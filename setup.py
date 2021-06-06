from setuptools import setup

setup(
    name='mypackage',
    version='0.0.1',
    packages=['mypackage1','mypackage2'],
    install_requires=[
        'bentoml',
        'scikit-learn',
    ],
)
