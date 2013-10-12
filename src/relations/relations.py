#!/usr/bin/env python
from optparse import OptionParser
from collections import defaultdict
from sys import stdin, stdout


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
    polytope [0,2]. (The echo function simulates piping in a file.)
    $ echo -e '0\n1\n2' | python relations.py
    """
    usage = "usage: %prog [options] dataset"
    usage += '\n'+main.__doc__
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-n", "--variable_start",
        help="Start variable count at this number. [default: %default]",
        action="store", dest="variableStart", default=0)
    parser.add_option(
        "-i", "--infile",
        help="Filename for input file.",
        action="store", dest="infile", default=None)
    parser.add_option(
        "-o", "--outfile",
        help="Filename for output file.",
        action="store", dest="outfile", default=None)

    (options, args) = parser.parse_args()
    assert len(args) <= 1

    if options.infile:
        infile = open(options.infile)
    else:
        infile = stdin

    if options.outfile:
        outfile = open(options.outfile, 'w')
    else:
        outfile = stdout
        
    relations(infile, outfile, variableStart=options.variableStart)

    infile.close()
    outfile.close()


def relations(infile, outfile, variableStart):
    latticePoints = loadPoints(infile, delimiter=',')
    variableDict = getVariableDict(latticePoints, variableStart)
    variables = variableDict.keys()
    variables.sort()
    relations = getRelations(variableDict)
    numRelations = reduce(lambda x, y: x + len(y) - 1, relations, 0)
    prettyPrint(outfile, variables, variableDict, relations, numRelations)


def makeStringRep(point):
    """
    Convert list of integers to comma-separated string for hashing.
    """
    point = [str(num) for num in point]
    rep = ",".join(point)
    return rep


def loadPoints(infile, delimiter=','):
    """
    Take a file object whose lines are comprised of delimter-separated list of
    integers and return a list of lists of those lines split at the dilimiters
    and convert the strings to integer objects. Check to make sure values are
    valid integers and that each line has the same number of items in the
    comma-separated list.
    """
    latticePoints = []
    for vector in infile:
        point = vector.strip().split(delimiter)
        try:
            point = [int(num) for num in point]
        except ValueError:
            raise Exception("Must input integer vector")
        latticePoints.append(point)
    dim = len(latticePoints[0])
    for point in latticePoints:
        if len(point) != dim:
            raise Exception("All points must be same dimension")
    return latticePoints


def getRelations(variableDict):
    """
    Return a list of pairs of variables whose corresponding pair of points sum
    to the same point. (This probably makes no sense.)
    """
    relationsDict = defaultdict(list)
    variables = variableDict.keys()
    for var1 in variables:
        for var2 in variables:
            if var1 <= var2:
                key = addPoints(variableDict[var1], variableDict[var2])
                key = makeStringRep(key)
                relationsDict[key].append([var1, var2])
    relations = []
    for key in relationsDict:
        relation = relationsDict[key]
        if len(relation) > 1:
            relations.append(relation)
    return relations


def addPoints(point1, point2):
    """
    Return the vector sum of two lists of integers.
    """
    result = []
    for num1, num2 in zip(point1, point2):
        result.append(point1 + point2)
    return result

def prettyPrint(outfile, variables, variableDict, relations, numRelations):
    """
    Print out result statistics to outfile.
    """
    outfile.write("Variables:\n")
    for variable in variables:
        outfile.write('\t' + variable + ' <----> ')
        outfile.write(makeStringRep(variableDict[variable]) + '\n')
    outfile.write(str(numRelations) + " Relations:\n")
    if not relations:
        outfile.write('\tNone\n')
    else:
        for relation in relations:
            relation.sort()
            tempString = '\t'
            for var1, var2 in relation:
                tempString = tempString + var1 + var2 + ' = '
            outfile.write(tempString[:-3] + '\n')


def getVariableDict(latticePoints, variableStart):
    """
    Take a list of lattice points and return a dictionary mapping a formal
    variable to each lattice point.
    """
    variableStart = int(variableStart)
    variableDict = {}
    for num, point in enumerate(latticePoints, variableStart):
        variableDict['x' + str(num)] = point
    return variableDict


if __name__=='__main__':
    main()
