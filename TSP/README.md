# TSP

The Traveling Salesman Problem Library (TSPLIB) by Reinelt (1991).
Downloaded from the [DIMACS archive](http://archive.dimacs.rutgers.edu/Challenges/TSP/download.html).
This repository includes the large instances (1000+ clients), which we use for benchmarking PyVRP.
The following instances were excluded from this collection:
- `si1032.tsp`: uses upper diagonal row edge weight format
- `pla85900.tsp` and `pla33810.tsp`: too large
- `d1655.tsp` and `vm1748.tsp`: rounding issues

All instances have been modified to fit the VRPLIB format: the file extension was changed from `.tsp` to `.vrp`, and a `VEHICLES : 1` field was added to the header. 
Since there are no depots in TSP, it's assumed that the first node is the depot.

Solutions were obtained by running [LKH v2.0.11](http://webhotel4.ruc.dk/~keld/research/LKH/) over multiple runs.
Most solutions are optimal (marked as `Optimal: True` in the solution files), and the true optimal values can be found on the [TSPLIB95 website](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html).
The non-optimal solutions are very close to optimal:
- brd14051: 0.002% gap (8 units away from 469385)
- d15112: 0.001% gap (16 units away)
- d18512: 0.003% gap (18 units away)
- fl1400: 0.184% gap
- fl1577: 0.022% gap
- fl3795: 0.292% gap (largest gap - 84 units away)
- rl1889: 0.004% gap (13 units away)
- usa13509: 0.000% gap (15 units away)

### References

Reinelt, G. (1991). TSPLIB—A traveling salesman problem library. ORSA Journal on Computing, 3(4), 376–384. https://doi.org/10.1287/ijoc.3.4.376
