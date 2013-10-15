toric-geometry
==============

Note
-----
This repository is a work in progress and you can safely assume that this file
is not updated with the latest information on what's been coded. If you have
any questions, feel free to email/message me.

Summary
-----
This repostitory contains command-line utilities which are meant to simplify
certain computations involving toric varieties. As written, these utitilities
are meant to be run a linux machine though I assume they work with minor
modifications on other systems.

n-dimensional projective toric varieties are mathematical objects that are
highly symmetric.  As such, many computations simplify to computations
involving convex polytopes in n real dimensions. This repository only considers
2-dimensional varieties at the moment, meaning that main object of study are
convex polytopes in the plane.

Relations
-----
The program relations.py computes the necessary information for the projective
embedding coming from a toric polytope.

Lattice Generator
-----
The program latticeGenerator.py simply prints the lattice points corresponding
to polytopes of different sizes coming from either P^2 or P^2 blown up at one
point (the first Hirzebruch surface). It is merely a convenient helper function
to see a family of possible embeddings from relations.py.

Other
-----
There are other programs of varying completeness in the src/ directory. If
you're curious, look around, but beware of any dragons you may find.

Dependencies
-----
python 2.7
