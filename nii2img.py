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
    'output_prefix': "img",
    'verbose': False
}


def parse_params(argv, params):
    try:
        short_opts = "s:e:a:o:v"
        long_opts = ["start_slice=", "end_slice=", "alternate_slice=", "output_prefix="]
        opts, args = getopt.getopt(argv, short_opts, long_opts)
        if len(args) == 1:
            params['nii_filename'] = args[0]
        else:
            raise
    except:
        print "Error! Invalid option(s)."
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-s", "--start_slice"):
            params['start_slice'] = int(arg)
        elif opt in ("-e", "--end_slice"):
            params['end_slice'] = int(arg)
        elif opt in ("-a", "--alternate_slice"):
            params['alternate_slice'] = int(arg)
        elif opt in ("-o", "--output_prefix"):
            params['output_prefix'] = arg
        elif opt in ("-v", "--verbose"):
            params['verbose'] = True


# load nifti file according to parameters above
def load_nii(params):
    if params['verbose']:
        print "Loading NIfTI file"

    img = nib.load(params['nii_filename'])
    data = img.get_data()
    return data


# normalize the color value range in the original nii image
def normalize_nii(params, data):
    if params['verbose']:
        print "Normalizing intensities"


# extract the images from the file you wish to continue with, alternation, start and end slice
def extract_img(params, data):
    if params['verbose']:
        print "Extracting images"

    counter = 0
    start_slice = params['start_slice'] or 0
    start_slice = start_slice - 1 if start_slice > 0 else start_slice
    end_slice = params['end_slice'] or data.shape[2]
    data = data[:, :, range(start_slice, end_slice)]
    for i in range(0, data.shape[2]):
        if (i % params['alternate_slice']) == 0:
            slice = numpy.rot90(data[:, :, i])
            image_name = params['output_prefix'] + str(counter) + ".png"
            scipy.misc.imsave(image_name, slice)
            counter += 1
            if params['verbose']:
                sys.stdout.write(".")
                sys.stdout.flush()

    if params['verbose']:
        print ""


if __name__ == '__main__':
    parse_params(sys.argv[1:], params)
    data = load_nii(params)
    normalize_nii(params, data)
    extract_img(params, data)
    if params['verbose']:
        print "Finished"
