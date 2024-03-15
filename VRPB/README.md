# VRPB

VRP with backhauls instances of Queiroga et al. (2020).
Downloaded from [VRP-REP](http://www.vrp-rep.org/references/item/queiroga-et-al-2019.html) and modified to fit the VRPLIB format. 

These instances are generated based on the CVRP instances proposed by Uchoa et al. (2017). 
For each CVRP instance, 3 VRPB variants are created with 50%, 66% and 80% of linehaul customers, respectively. 
For example, the CVRP instance X-n1001-k22 is converted to three VRPB instances X-n1001-50-k22, X-n1001-66-k28, X-n1001-80-k34. 

This repository only includes the 90 largest VRPB instances (three per CVRP instance), which we use for benchmarking PyVRP.
These instances range in size from 523 to 1000 customers. 
The other instances can be found in [this zip](https://github.com/PyVRP/PyVRP/files/14434517/VRPB.zip).


### References

Queiroga, E. et al. (2020). On the exact solution of vehicle routing problems with backhauls. European Journal of Operational Research, 287(1), 76–89. https://doi.org/10.1016/j.ejor.2020.04.047.

Uchoa, E. et al. (2017). New benchmark instances for the Capacitated Vehicle Routing Problem. European Journal of Operational Research, 257(3), 845–858. https://doi.org/10.1016/j.ejor.2016.08.012.
