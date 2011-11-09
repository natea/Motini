from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Motini',
      version=version,
      description="Motini is a web-based tool to easily theme websites with a point-n-click interface.",
      long_description=open("README.rst").read(),
#       + "\n\n" +
#                       open(os.path.join("docs", "HELP.txt")).read() +
#                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],      
      keywords='javascript, theming, jquery',
      author='Nate Aune',
      author_email='natea@jazkarta.com',
      url='http://natea.github.com/Motini',
      license='MIT',
#      packages=['motini'],
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
#      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'Deliverance',
        'Mako',
      ],
      entry_points="""
      [console_scripts]
      motini = motini.motini_simple:main

      [paste.app_factory]
      main = motini.motini_simple:app_factory
      """
      )


