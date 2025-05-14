# MTVRPTWR

This folder contains multi-trip VRPTW with release dates instances from Yang (2023) and Yang (2024).
Downloaded from [Github](https://github.com/Yu1423/CMTVRPTWX) and modified to fit the VRPLIB format.

The instances are based on the Solomon (100 clients) instances and Gehring and Homberger instances (200 clients).
Compared to the original instances, the multi-trip instances have different number of vehicles and vehicle capacities, and it is allowed to reload vehicles.
Release times were generated following the procedure described in Cattaruzza et al. (2016).

The BKS presented here include reload depot visits within routes by explicitly including depot indices in the solution representation. 
Location numbering starts at 0, with depots assigned lower indices. 
For example, in a problem with only one depot, "Route #1: 1 0 2" indicates that this route visits client 1, returns to depot 0 to reload, and then serves client 2.
Finally, the solution costs adhere to the rounding convention where all distances and durations are rounded to one decimal place (e.g., 1052.2). 

### References

Cattaruzza, D., Absi, N., & Feillet, D. (2016). The Multi-Trip Vehicle Routing
Problem with Time Windows and Release Dates. Transportation Science, 50(2), 
676–693. https://doi.org/10.1287/trsc.2015.0608

Yang, Y. (2023). An Exact Price-Cut-and-Enumerate Method for the
Capacitated Multitrip Vehicle Routing Problem with Time Windows.
Transportation Science 57(1): 230-251. https://doi.org/10.1287/trsc.2022.1161

Yang, Y. (2024). DeLuxing: Deep Lagrangian Underestimate Fixing for 
Column-Generation-Based Exact Methods. Operations Research. 
https://doi.org/10.1287/opre.2023.0398
