#!/usr/bin/python

import sys
import getopt
import nibabel as nib
import numpy
import scipy

# params is the dictionary holding all needed parameters for the script
params = {
  'nii_filename': "",
  'start_slice': 0,
  'end_slice': None,
  'alternate_slice': 1,
  'output_prefix': "img"
}

def parse_params(argv, params):
  try:
    short_opts = "s:e:a:o:"
    long_opts =  ["start_slice=","end_slice=","alternate_slice=","output_prefix="]
    opts, args = getopt.getopt(argv, short_opts, long_opts)
    print args
    if len(args) == 1:
      params['nii_filename'] = args[0]
    else
      raise
  except:
    print "error"
    sys.exit(2)
  
  for opt,arg in opts:
      if opt in ("-s", "--start_slice"):
        params['start_slice'] = arg 
      else if opt in ("-e", "--end_slice"):
        params['end_slice'] = arg
      else if opt in ("-a", "--alternate_slice"):
        params['alternate_slice'] = arg
      else if opt in ("-o", "--output_prefix"):
        params['output_prefix'] = arg

# load nifti file according to parameters above
def load_nii():
  pass

# normalize the color value range in the original nii image
def normalize_nii():
  pass

# extract the images from the file you wish to continue with a.s.o.
def extract_img():
  pass
  

if __name__ == '__main__':
  parse_params(sys.argv[1:], params)



#~ img = nib.load(nifti_filename)
#~ hdr =  img.get_header()
#~ data = img.get_data()
#~ 
#~ slice = numpy.rot90(data[:,:,150])
#~ scipy.misc.imsave('test150.png',slice)
