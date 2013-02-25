"""
Common functions/classes for dataprep.
"""
import sys


def get_inout_files(infilename, outfilename):
    """
    Gets infile, and outfile, which are opened versions of infilename,
    outfilename.

    Parameters
    ----------
    infilename : String
        Name of file to read.  If None, we will read from stdin
    outfilename : String
        Name of file to write.  If None, we will write to stdout

    Returns
    -------
    The tuple (infile, outfile)
    """
    if infilename:
        infile = open(infilename, 'r')
    else:
        infile = sys.stdin

    if outfilename:
        outfile = open(outfilename, 'w')
    else:
        outfile = sys.stdout

    return infile, outfile


def close_files(infile, outfile):
    """
    Closes the files if and only if they are not equal to sys.stdin, sys.stdout
    """
    if infile != sys.stdin:
        infile.close()
    if outfile != sys.stdout:
        outfile.close()
