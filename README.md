# Alcoved-Polytopes

A short description of what each program does.

AlcPolyClean.py : Generated 2-dimensional alcoved polygons and calcultates the area and number of boundary points.

findAllInvalidpts.py : Explicitly calculates every non-valid point up to a set limit. Very slow.

isPointValid.py : Explicitly works out if a coefficient pair (c1,c2) is valid. If it is, it returns the alcoved polygons which correspond to this Ehrhart polynomial.

nonSolutionsMod3.py : made to solve a certain equation modulo 3. Can be run with arbitrary modulus, but that is not relevant to us.

thirdDim.py : Similar to AlcPolyClean, but for three-dimensional alcoved plytopes. Runs much more slowly. Cannot explicitly find non-valid points.
