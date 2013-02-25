#!/usr/bin/env python
from optparse import OptionParser
from numpy import array, loadtxt
from itertools import product as prod
import sys
import src.common as common


def main():
    r"""
    DESCRIPTION
    -----------
    Returns the relations of the projective embedding of a toric variety coming
    from it toric polytope.

    NOTES
    -----
    The lattice points of the polytope should be given in an input text file or
    they should be piped in (but care must be taken to add newline
    characters--i.e. '\n'--in between the lattice points. The names of the
    variables are chosen in the order the lattice points are given.

    EXAMPLES
    ---------
    Return the relations for P^1 polarized by O(2)--which corresponds to the
    polytope [0,2].  The example file contains the points 0, 1, and 2 each on
    their own line.
    $ python relations.py ../examples/P1O2
    """
    usage = "usage: %prog [options] dataset"
    usage += '\n'+main.__doc__
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-v", "--variety",
        help="String defining which variety. Options are Hirz or Proj2.",
        action="store", dest='variety', default=None)
    parser.add_option(
        "-s", "--lattice-size",
        help="String defining size of lattice.",
        action="store", dest='lattice_size', default=None)
    parser.add_option(
        "-o", "--outfilename",
        help="Write to this file rather than stdout.  [default: %default]",
        action="store", dest='outfilename', default=None)

    (options, args) = parser.parse_args()

    ### Parse args
    assert options.variety
    assert options.lattice_size

    infilename = args[0] if args else None

    ## Get the infile/outfile
    infile, outfile = common.get_inout_files(infilename, options.outfilename)

    ### Call the function that does the real work
    produce_lattice_points(infile, outfile, variety=options.variety,
                           lattice_size=options.lattice_size)

    ## Close the files iff not stdin, stdout
    common.close_files(infile, outfile)


def produce_lattice_points(infile, outfile, variety, lattice_size):
    lattice_size = int(lattice_size)
    if variety == 'Proj':
        outfile.write('0,0\n')
    for x in range(1, lattice_size):
        outfile.write(str(x) + ',' + '0\n')
    for y in range(1, lattice_size):
        for x in range(y, lattice_size):
            outfile.write(str(x) + ',' + str(y) + '\n')


if __name__ == '__main__':
    main()
