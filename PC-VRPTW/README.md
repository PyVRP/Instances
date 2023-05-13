# PC-VRPTW

These instances are based on the GH1000 instances.
See also the `VRPTW/` folder in this repository for details.

The instances are exactly as the GH1000 instances, but then in VRPLIB format (instead of Solomon), downloaded from the [LKH-3 webpage](http://webhotel4.ruc.dk/~keld/research/LKH-3/).
The data is the same, but a new `PRIZE_SECTION` has been added.
The prizes listed in that section are generated as follows.

Let $q_i$ be the demand of client $i$.
The prize $p_i$ is given by $h \times q_i$, where $h$ is sampled from $U[0.75, 2.25]$.
These prizes are the same as those used by Bulhões et al. (2018), and, in expectation, very similar to those used by Strenger et al. (2013).

Stenger, Andreas  et al. (2013). The prize-collecting vehicle routing problem
with single and multiple depots and non-linear cost. EURO Journal on
Transportation and Logistics, 2(1–2): 57-87. 
https://doi.org/10.1007/s13676-013-0022-4.

Bulhões, T. et al. (2018). The vehicle routing problem with service level
constraints. European Journal of Operational Research, 265(2): 544–558.
https://doi.org/10.1016/j.ejor.2017.08.027.
