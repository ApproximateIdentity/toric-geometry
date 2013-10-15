#!/usr/bin/env python
from optparse import OptionParser
from sys import stdout


def main():
    r"""
    DESCRIPTION
    -----------
    Generate the lattice points for either P^2 or P^2 blown up at one point
    (the first Hirzebruch surface). Result is written either to standard out or
    to the given file.

    NOTES
    -----
    The lattice points of the polytope should be given in an input text file or
    they should be piped in (but care must be taken to add newline
    characters--i.e. '\n'--in between the lattice points. The names of the
    variables are chosen in the order the lattice points are given.
    """
    usage = "usage: %prog [options] dataset"
    usage += '\n'+main.__doc__
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-v", "--variety",
        help="String defining which variety. Options are Hirz or Proj.",
        action="store", dest='variety', default=None)
    parser.add_option(
        "-s", "--lattice-size",
        help="String defining size of lattice.",
        action="store", dest='latticeSize', default=None)
    parser.add_option(
        "-o", "--outfilename",
        help="Write to this file rather than stdout.  [default: stdout]",
        action="store", dest='outfilename', default=None)

    (options, args) = parser.parse_args()

    assert options.variety
    assert options.latticeSize

    variety = options.variety
    latticeSize = int(options.latticeSize)

    if options.outfilename:
        outfile = open(options.outfilename, 'w')
    else:
        outfile = stdout

    printLatticePoints(outfile, variety=variety, latticeSize=latticeSize)

    outfile.close()


def printLatticePoints(outfile, variety, latticeSize):
    if variety == 'Proj':
        outfile.write('0,0\n')
    for x in range(1, latticeSize):
        outfile.write(str(x) + ',' + '0\n')
    for y in range(1, latticeSize):
        for x in range(y, latticeSize):
            outfile.write(str(x) + ',' + str(y) + '\n')


if __name__ == '__main__':
    main()
