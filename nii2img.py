#!/usr/bin/python

import sys
import getopt
import nibabel as nib
import numpy
import scipy

# params is the dictionary holding all needed parameters for the script
# think about adding an -m option for introducing a mask
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
    else:
      raise
  except:
    print "error"
    sys.exit(2)
  
  for opt,arg in opts:
      if opt in ("-s", "--start_slice"):
        params['start_slice'] = int(arg) 
      elif opt in ("-e", "--end_slice"):
        params['end_slice'] = int(arg)
      elif opt in ("-a", "--alternate_slice"):
        params['alternate_slice'] = int(arg)
      elif opt in ("-o", "--output_prefix"):
        params['output_prefix'] = arg
        

# load nifti file according to parameters above
def load_nii(params):
  img = nib.load(params['nii_filename'])
  data = img.get_data()
  return data

# normalize the color value range in the original nii image
def normalize_nii():
  pass

# extract the images from the file you wish to continue with, alternation, start and end slice
def extract_img(params, data):
  counter = 0
  end_slice = params['end_slice'] or data.shape[2]
  for i in range(params['start_slice'], end_slice):
    if (i % params['alternate_slice']) == 0:
      slice = numpy.rot90(data[:,:,i])
      image_name = params['output_prefix'] + str(counter) + ".png"
      scipy.misc.imsave(image_name, slice)
      counter = counter + 1
      
if __name__ == '__main__':
  parse_params(sys.argv[1:], params)
  data = load_nii(params)
  extract_img(params, data)

#~ img = nib.load(nifti_filename)
#~ hdr =  img.get_header()
#~ data = img.get_data()
#~ data.shape # gives you the three dimension values
#~ slice = numpy.rot90(data[:,:,150])
#~ scipy.misc.imsave('test150.png', slice)
