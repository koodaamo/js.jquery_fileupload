from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='js.jquery_fileupload',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Petri Savolainen',
      author_email='petri.savolainen@koodaamo.fi',
      url='https://github.com/koodaamo/js.jquery_fileupload',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'fanstatic',
      ],
      entry_points = {
       'fanstatic.libraries': ['jquery_fileupload = js.jquery_fileupload.resources:library',],
      },
      )
