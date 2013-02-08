from numpy import array
from itertools import product as prod

class Relations():
    '''
    This computes the relations coming from the standard projective embedding of
    a toric polytope. The inputs are the integer lattice points within a
    (closed) toric polytope. The order of the inputted lattice points
    corresponds gives variables 'x0', ..., 'xN' where N is the total number of
    lattice points in P. The lattice points should be inputed as a list of lists
    of integers--where the dimension determines the lenth of the interior lists.

    CAVEAT: I JUST REALIZED THAT THE RELATIONS THAT ARE GIVEN ARE NOT NECESSARILY
    MINIMAL. (THOUGH THE CODE DOES PRECLUDE NON-MINIMAL RELATIONS OF LENGTH 2...

    Example:

    rel = Relations([[0,0],[0,1],[1,0],[1,1]])
    rel.compute_relations()
    rel.result = [['x0x3','x1x2']]
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
