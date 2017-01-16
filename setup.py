from setuptools import setup

setup(
    name="nb_cat",
    version="0.1",
    author="D. I. Cortes",
    description='Print notebook contents in a terminal',
    url='https://github.com/davidcortesortuno/nb_cat',
    install_requires=[
        'nbformat',
    ],
    py_modules=['nb_cat'],
    scripts=['bin/nb_cat']
)
