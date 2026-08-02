# Arc routing problems

This directory contains GVRP transformations of the `DI-NEARP` and `egl-g` arc routing instances.
The transformed instances use the VRPLIB extensions supported by PyVRP.

## Transformation

Each required node becomes one required client.
Each required undirected edge becomes two optional clients, one for each service direction.
The two directional clients are placed in a mutually exclusive group, so exactly one direction is selected.
Each transformed client keeps the demand of the original required element.

The explicit edge-weight matrix combines shortest-path deadheading with the service cost of the destination client.
This makes the GVRP objective equal to the original CARP or NEARP objective.
The matrix is asymmetric because each directional client has different entry and exit nodes.

## Solutions

The solution files are converted from the reference solutions distributed with the source instances in PyARP.
They use the standard VRPLIB route format and have been checked with PyVRP for completeness, capacity feasibility, fleet feasibility, group feasibility, and objective value.

## References

Thibaut Vidal (2017).
Node, edge, arc routing and turn penalties: Multiple problems - one neighborhood extension.
_Operations Research_, 65(4), 992-1010.
https://doi.org/10.1287/opre.2017.1595

L. Y. O. Li and R. W. Eglese (1996).
An interactive algorithm for vehicle routeing for winter-gritting.
_Journal of the Operational Research Society_, 47, 217-228.

J. M. Belenguer and E. Benavent (2003).
A cutting plane algorithm for the capacitated arc routing problem.
_Computers & Operations Research_, 30(5), 705-728.
