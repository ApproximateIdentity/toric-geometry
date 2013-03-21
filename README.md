toric-geometry
==============

Note
-----
This repository is a work in progress and you can safely assume that this file
is not updated with the latest information on what's been coded. I am making an
attempt at following best practices such as test-driven development, extreme
programming, etc. so this is as much a CS design project as a mathematical one.
If you have any questions, feel free to email/message me.

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

Dependencies
-----
python 2.7, numpy
