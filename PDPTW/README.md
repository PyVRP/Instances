# PDPTW

This folder contains all Li & Lim PDPTW instances with 100 up to 1000 customers.
The 1000-customer instances are in this folder, and the smaller instances are in the `Li100/` up to `Li800/` subfolders.
The original instances are downloaded from [SINTEF](https://www.sintef.no/projectweb/top/pdptw/li-lim-benchmark/) and modified to fit PyVRP's VRPLIB format.
Distances are Euclidean and follow PyVRP's `exact` convention, that is, each value is scaled by 1000 and rounded to the nearest integer.
The objective is to minimise the total distance traveled, as opposed to the classical hierarchical objective that first minimises the number of vehicles and then the total distance.
The solution cost represents the total distance traveled.

> Solutions in this folder are the best solutions we found using multiple solvers under the distance-minimisation objective; they are not the best-known solutions from the literature.
