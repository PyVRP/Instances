# HFVRP

Heterogeneous fleet instances of Pessoa et al. (2018).
Downloaded from the [supplementary materials](https://www.sciencedirect.com/science/article/pii/S0377221718303126?via%3Dihub) associated with the paper and modified to fit PyVRP's VRPLIB format.

These instances are generated based on the CVRP instances proposed by Uchoa et al. (2017). 
For each CVRP instance in the X set, a new HFVRP instance was created of one the following types:

1. HVRP, with limited fleet and fixed and variable costs;
2. HD, with limited fleet and variable costs;
3. FSMFD, with unlimited fleet and fixed and variable costs;
4. FSMF, with unlimited fleet and fixed costs;
5. FSMD, with unlimited fleet and variable costs.

See Pessoa et al. (2018) for more details about the generation procedure. 

Because PyVRP only handles integer values, we scaled the original HFVRP instances by multiplying all unit distance costs and fixed vehicle costs by 100.
It is also assumed that unit distance costs are not rounded or scaled when using different rounding conventions. 

The BKS presented here align the routes with the vehicles: thus, "Route 1" corresponds to "Vehicle 1" in the instance data.
Similarly "Route 2" corresponds to "Vehicle 2", and so on.
In this way it is unambiguous which vehicle is supposed to execute which route.


### References
Pessoa, A. et al. (2018). Enhanced Branch-Cut-and-Price algorithm for heterogeneous fleet vehicle routing problems. European Journal of Operational Research, 270(2), 530–543. https://doi.org/10.1016/j.ejor.2018.04.009

Uchoa, E. et al. (2017). New benchmark instances for the Capacitated Vehicle Routing Problem. European Journal of Operational Research, 257(3), 845–858. https://doi.org/10.1016/j.ejor.2016.08.012.
