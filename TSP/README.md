# TSP

This folder contains a subset of instances from the Traveling Salesman Problem Library (TSPLIB) by Reinelt (1991).
The instances are downloaded from the [DIMACS archive](http://archive.dimacs.rutgers.edu/Challenges/TSP/download.html).
Solutions were obtained by running [LKH v2.0.11](http://webhotel4.ruc.dk/~keld/research/LKH/) over multiple runs.
Most solutions are optimal (marked as `Optimal: True` in the solution files), and the true optimal values can be found on the [TSPLIB95 website](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html).
The non-optimal solutions are extremely close to optimal, with the largest gap being 0.292% for `fl3795` (84 away from optimal).

All instances have been modified to fit the VRPLIB format: the file extension was changed from `.tsp` to `.vrp`, and a `VEHICLES : 1` field was added to the header. Moreover, as there are no depots in TSP, it's assumed that the first node is the depot.

The following instances were excluded from this collection:
- `si1032.tsp`: uses upper diagonal row edge weight format
- `pla85900.tsp` and `pla33810.tsp`: too large
- `d1655.tsp` and `vm1748.tsp`: rounding issues

### References

Reinelt, G. (1991). TSPLIB—A traveling salesman problem library. ORSA Journal on Computing, 3(4), 376–384. https://doi.org/10.1287/ijoc.3.4.376
