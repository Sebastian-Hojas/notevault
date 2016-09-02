from setuptools import setup

setup(
    name='SortNote',
    version='0.1.0',
    author='Sebastian Hojas',
    author_email='later@irrelevant.at',
    packages=['sortnote', 'sortnote.test'],
    # scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/sortnote/',
    license='LICENSE.txt',
    description='Brings order to a world of chaos.',
    long_description=open('README.md').read(),
    install_requires=[
        "python-crontab >= 2.1.1",
    ],
    entry_points = {
        "console_scripts": ['sortnote = sortnote.__main__:main']
    },
)