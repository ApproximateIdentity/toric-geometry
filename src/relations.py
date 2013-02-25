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
        "-o", "--outfilename",
        help="Write to this file rather than stdout.  [default: %default]",
        action="store", dest="outfilename", default=None)
    parser.add_option(
        "-n", "--variable_start",
        help="Start variable count at this number. [default: %default]",
        action="store", dest="variable_start", default=0)

    (options, args) = parser.parse_args()
    ### Parse args
    assert len(args) <= 1
    infilename = args[0] if args else None

    ## Get infile and outfile.
    infile, outfile = common.get_inout_files(infilename, options.outfilename)

    _relations(infile, outfile, variable_start=options.variable_start)

    ## Close the files iff not stdin, stdout
    common.close_files(infile, outfile)

def _relations(infile, outfile, variable_start):
    lattice_points = loadtxt(infile, dtype='int', delimiter=',')
    variable_dict = _get_variable_dict(lattice_points, variable_start)
    variables = variable_dict.keys()
    variables.sort()
    relations = _get_relations(variable_dict)
    num_relations = reduce(lambda x, y: x + len(y) - 1, relations, 0)
    _pretty_print(outfile, variables, variable_dict, relations, num_relations)


def _get_relations(variable_dict):
    relations_dict = {}
    variables = variable_dict.keys()
    for var1, var2 in prod(variables, variables):
        if var1 <= var2:
            key = (variable_dict[var1] + variable_dict[var2]).tostring()
            if key in relations_dict:
                relations_dict[key].append([var1, var2])
            else:
                relations_dict[key] = [[var1, var2]]
    relations = []
    for thing in relations_dict:
        if len(relations_dict[thing]) > 1:
            relations.append(relations_dict[thing])
    return relations


def _pretty_print(outfile, variables, variable_dict, relations, num_relations):
    outfile.write("Variables:\n")
    for variable in variables:
        outfile.write('\t' + variable + ' <----> ')
        outfile.write(str(variable_dict[variable].tolist()) + '\n')
    outfile.write(str(num_relations) + " Relations:\n")
    if not relations:
        outfile.write('\tNone\n')
    else:
        for relation in relations:
            relation.sort()
            temp_string = '\t'
            for pair in relation:
                temp_string = temp_string + pair[0] + pair[1] + ' = '
            outfile.write(temp_string[:-3] + '\n')


def _get_variable_dict(lattice_points, variable_start):
    variable_start = int(variable_start)
    variable_dict = {}
    for num, point in enumerate(lattice_points, variable_start):
        variable_dict['x' + str(num)] = point
    return variable_dict


if __name__=='__main__':
    main()
