# VRPTW-RT

This directory includes instances and solutions for the Vehicle Routing Problem with Time Windows and Release Times (VRPTW-RT).

These instances are based on the instances provided during the [EURO meets NeurIPS 2022 Vehicle Routing Competition](https://github.com/ortec/euro-neurips-vrp-2022-quickstart).
We took the 100 static instances with the highest number of customers.
For each instance, we used the dynamic environment provided in the competition repository to create a dynamic VRPTW instance with seed 0, 100 requests per sample, and an epoch duration of 1800 seconds.
The release time of each request then corresponds to the start time of the epoch in which it the request was revealed. 
Moreover, we used the Euclidean distances based on the node coordinates instead of using the explicitly provided distances matrix.

The best-known solutions reported in this directory follow the convention to minimize the total distance traveled with distances and durations rounded to the nearest decimal.
