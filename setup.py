import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system.
sys.path.pop(0)
from setuptools import setup


setup(name='micropython-png',
      version='0.0.1',
      description='Minimal port of PyPNG for MicroPython',
      long_description="A pure-MicroPython implementation of a PNG reader, "
          "adapted from PyPNG.  The PNG writing functionality from PyPNG is "
          "not implemented because of MicroPython's lack of support for zlib "
          "compression.",
      url='https://github.com/Ratfink/micropython-png',
      author='Clayton G. Hobbs',
      author_email = "clay@lakeserv.net",
      license='MIT',
      py_modules=['png'],
      install_requires=['micropython-itertools'])
