from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Motini',
      version=version,
      description="Motini is a web-based tool to easily theme websites with a point-n-click interface.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='javascript, theming, jquery',
      author='Nate Aune',
      author_email='natea@jazkarta.com',
      url='http://natea.github.com/Motini',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'staticlxml',
          'Deliverance',
      ],
      entry_points={
        'console_scripts': [
          'motini = motini.motini_simple:main',
          ]},      
      )
