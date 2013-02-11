from numpy import array, loadtxt
from itertools import product as prod

class Relations():
    '''
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
    '''

    def __init__(self, lattice_points):
        self.lattice_points = lattice_points
        self.v_dict = {}
        for num, thing in enumerate(self.lattice_points):
            self.v_dict['x'+str(num)] = array(thing)
        self.keys = self.v_dict.keys()

    def compute_relations(self):
        temp_result = []
        keys = self.keys
        v_dict = self.v_dict
        for (t1, (t2, (t3, t4))) in prod(keys, prod(keys, prod(keys, keys))):
            if (v_dict[t1] + v_dict[t2] == v_dict[t3] + v_dict[t4]).all():
                if (t1 <= t2) and (t3 <= t4) and (t1 + t2 != t3 + t4) and (t1 <= t3):
                    temp_result.append([t1 + t2, t3 + t4])
        
        temp_filter = []

        for t1, t2 in prod(temp_result, temp_result):
            if (t1[1] == t2[0]) and ([t1[0], t2[1]] in temp_result):
                temp_filter.append([t1[0],t2[1]])

        self.result = [crap for crap in temp_result if not(crap in temp_filter)]
