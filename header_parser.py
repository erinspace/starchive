import xml.etree.ElementTree as ET, glob
from astropy.io import fits

raw_FITS = './raw_FITS/'

local_file_names = glob.glob(raw_FITS +'*.FITS')

for filename in local_file_names:
    FITS_file = fits.open(filename)
    scidata =  FITS_file[0].header

    ## To print out the FITS header nicely
    for field in scidata:
        if field:
            print field, '=', scidata[field]