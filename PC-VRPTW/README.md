# PC-VRPTW

These instances are based on the GH1000 instances.
See also the `VRPTW/` folder in this repository for details.

The instances are exactly as the GH1000 instances, but then in VRPLIB format (instead of Solomon), downloaded from the [LKH-3 webpage](http://webhotel4.ruc.dk/~keld/research/LKH-3/).
The data is the same, but a new `PRIZE_SECTION` has been added.
The prizes listed in that section are generated as follows.

Let $q_i$ be the demand of client $i$.
The prize $p_i$ is given by $10 * h_i \times q_i$, where $h_i$ is sampled i.i.d. from $U[0.75, 2.25]$.
These prizes are similar to those used by Bulhões et al. (2018) and Stenger et al. (2013), but scaled to the larger distances of the GH1000 distances.

Stenger, A. et al. (2013). The prize-collecting vehicle routing problem with
single and multiple depots and non-linear cost. EURO Journal on Transportation
and Logistics, 2(1–2): 57-87. https://doi.org/10.1007/s13676-013-0022-4.

Bulhões, T. et al. (2018). The vehicle routing problem with service level
constraints. European Journal of Operational Research, 265(2): 544–558.
https://doi.org/10.1016/j.ejor.2017.08.027.
