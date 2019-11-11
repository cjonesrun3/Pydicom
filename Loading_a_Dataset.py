"""
Documentation - https://pydicom.github.io/pydicom/stable/getting_started.html

"""

import numpy  # Required to use pixel_array
import pydicom
from pydicom.data import get_testdata_files

target_file = get_testdata_files('liver.dcm')[0]  # Using Pydicom's included test data
ds = pydicom.dcmread(target_file)

print(ds)  # Returns entire dataset associated with image
print(ds.pixel_array)  # Returns array with bytes from image - requires numpy

print(ds.dir('pat'))  # Allows you to search dataset keys


