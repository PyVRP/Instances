"""
Script that contains the functions to calculate the BKS of a given instance.

poetry run python bks.py \
solutions/ails2021/*.sol \
solutions/pyvrp/*.sol \
solutions/queiroga2021/*.sol \
--instance_dir instances \
--mock
"""

import argparse
from numbers import Number
from pathlib import Path

import numpy as np
import vrplib


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("candidates", type=Path, nargs="+")
    parser.add_argument("--instance_dir", type=Path)
    parser.add_argument("--mock", action="store_true")

    return parser.parse_args()


_INT_MAX = np.iinfo(np.int64).max


class InstanceParser:
    """
    read() helper that parses VRPLIB data into meaningful parts for further
    processing.
    """

    def __init__(self, instance: dict, round_func):
        self.instance = instance
        self.round_func = round_func

    @property
    def num_locations(self) -> int:
        return self.instance["dimension"]

    @property
    def num_depots(self) -> int:
        return self.instance.get("depot", np.array([0])).size

    @property
    def num_clients(self) -> int:
        return self.num_locations - self.num_depots

    @property
    def num_vehicles(self) -> int:
        return self.instance.get("vehicles", self.num_locations - 1)

    def type(self) -> str:
        return self.instance.get("type", "")

    def edge_weight(self) -> np.ndarray:
        return self.round_func(self.instance["edge_weight"])

    def demands(self) -> np.ndarray:
        if "demand" not in self.instance and "linehaul" not in self.instance:
            return np.zeros(self.num_locations, dtype=np.int64)

        return self.round_func(
            self.instance.get("demand", self.instance.get("linehaul"))
        )

    def coords(self) -> np.ndarray:
        if "node_coord" not in self.instance:
            return np.zeros((self.num_locations, 2), dtype=np.int64)

        return self.round_func(self.instance["node_coord"])

    def capacities(self) -> np.ndarray:
        if "capacity" not in self.instance:
            return np.full(self.num_vehicles, _INT_MAX)

        capacities = self.instance["capacity"]

        if isinstance(capacities, Number):
            # Some instances describe a uniform capacity as a single value
            # that applies to all vehicles.
            capacities = np.full(self.num_vehicles, capacities)

        return self.round_func(capacities)

    def unit_distance_costs(self) -> np.ndarray:
        if "vehicles_unit_distance_cost" not in self.instance:
            return np.ones(self.num_vehicles, dtype=np.int64)

        return self.round_func(self.instance["vehicles_unit_distance_cost"])

    def fixed_costs(self) -> np.ndarray:
        if "vehicles_fixed_cost" not in self.instance:
            return np.zeros(self.num_vehicles, dtype=np.int64)

        return self.round_func(self.instance["vehicles_fixed_cost"])


class InfeasibilityError(Exception):
    pass


class HFVRPChecker:
    def __init__(self, instance, routes):
        self.instance = instance
        self.routes = routes

    def cost(self):
        """
        Returns the cost, i.e., the total traveled distance.
        """
        distances = self.instance.edge_weight()
        unit_distance_costs = self.instance.unit_distance_costs()
        fixed_costs = self.instance.fixed_costs()
        cost = 0

        for idx, route in enumerate(self.routes):
            if route:
                frm, to = [0, *route], [*route, 0]
                unit_cost = unit_distance_costs[idx]
                fixed_cost = fixed_costs[idx]
                cost += fixed_cost + unit_cost * distances[frm, to].sum()

        return cost

    def feasible(self):
        """
        Checks whether the solution is feasible.
        """
        return self.all_clients_visited() and self.load_feasible()

    def all_clients_visited(self):
        """
        Checks that all clients are visited.
        """
        visits = [client for route in self.routes for client in route]
        num_locs = self.instance.num_locations

        if len(visits) != num_locs - 1:
            raise InfeasibilityError("Clients visited multiple times.")

        if set(visits) != set(range(1, num_locs)):
            raise InfeasibilityError("Not all clients are visited.")

        return True

    def load_feasible(self):
        """
        Checks that all routes are load feasible, i.e., vehicle capacities
        are not exceeded.
        """
        capacity = self.instance.capacities()
        demands = self.instance.demands()

        for idx, route in enumerate(self.routes):
            if demands[route].sum() > capacity[idx]:
                raise InfeasibilityError(f"Capacity exceeded for route {idx}.")

        return True


def no_rounding(args):
    return args


def main(candidates: list[Path], instance_dir: Path, mock: bool):
    print(f"Checking {len(candidates)} solutions.")

    bks = {}  # type: ignore

    for loc in candidates:
        cand = vrplib.read_solution(loc)

        # Check feasibility and recompute costs.
        instance = vrplib.read_instance(instance_dir / (loc.stem + ".vrp"))
        parser = InstanceParser(instance, no_rounding)
        checker = HFVRPChecker(parser, cand["routes"])
        checker.feasible()

        cand["cost"] = checker.cost()

        if loc.stem not in bks or cand["cost"] < bks[loc.stem]["cost"]:
            # No solution yet or it's an improving solution.
            bks[loc.stem] = cand

    for name, sol in bks.items():
        if not mock:
            out_loc = instance_dir / (name + ".sol")

            with open(out_loc, "w") as fh:
                for idx, route in enumerate(sol["routes"], 1):
                    clients = " ".join(str(c) for c in route)
                    fh.write(f"Route #{idx}: {clients}\n")

                fh.write(f"Cost: {sol['cost']:.2f}\n")


if __name__ == "__main__":
    args = parse_args()
    main(args.candidates, args.instance_dir, args.mock)
