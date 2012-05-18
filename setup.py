#!/usr/bin/env python

from distutils.core import setup

setup(name='logster',
      version='20120405',
      description='Tail a log file and filter each line to generate metrics '
              'that can be sent to common monitoring packages.',
      author='Mike Brittain',
      author_email='mike@mikebrittain.com',
      url='https://github.com/etsy/logster',
      py_modules=['logster_helper'],
      packages=['parsers'],
      package_dir={'':''},
      scripts=['logster'],
     )
