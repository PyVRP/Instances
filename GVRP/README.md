# GVRP

The M and G instances in this directory with 100-300 clients are due to Bektaş et al. (2011).
The L instances of size 500-1200 clients are due to Vidal et al. (2015), where they are presented for the Clustered VRP (CluVRP).
We interpret these instances as Generalized VRPs, and round the node coordinate data to integers (by multiplying the original floating point values by 1000 and truncating to integers).
Finally, the instances are all formatted to fit PyVRP's VRPLIB format.

### References

Tolga Bektaş, Güneş Erdoğan, and Stefan Røpke (2011). Formulations and
Branch-and-Cut Algorithms for the Generalized Vehicle Routing Problem.
_Transportation Science_, 45(3): 299 - 316.
https://doi.org/10.1287/trsc.1100.0352.

Thibaut Vidal, Maria Battarra, Anand Subramanian, and Güneş Erdogan (2015).
Hybrid metaheuristics for the Clustered Vehicle Routing Problem.
_Computers & Operations Research_, 58: 87 - 99.
https://doi.org/10.1016/j.cor.2014.10.019.
