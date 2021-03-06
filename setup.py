#!/usr/bin/env python
from setuptools import setup

version = '1.6.2.1'
classifiers = ["Development Status :: 5 - Production/Stable",
               "License :: OSI Approved :: Apache Software License",
               "Programming Language :: Python",
               "Programming Language :: Python :: 2.6",
               "Programming Language :: Python :: 2.7",
               "Programming Language :: Python :: 3.2",
               "Programming Language :: Python :: 3.3",
               "Programming Language :: Python :: Implementation :: PyPy"]   

setup(name='cloudmesh_timestring',
      version=version,
      description="Human expressed time to Dates and Ranges. This is a modified version from the oriinal code with an Openstack compatiple pytz dependency.",
      long_description="""Converting strings of into representable time via Date and Range objects.
 Plus features to compare and adjust Dates and Ranges.""",
      classifiers=classifiers,
      keywords='date time range datetime datestring',
      author='@stevepeak',
      author_email='steve@stevepeak.net',
      url='http://github.com/stevepeak/timestring',
      license='http://www.apache.org/licenses/LICENSE-2.0',
      packages=['timestring'],
      include_package_data=True,
      zip_safe=True,
      install_requires=["pytz>=2015.2"],
      entry_points={'console_scripts': ['timestring=timestring:main']})
