from pathlib import Path

import vrplib

SCALE = 100  # scaling factor for hetereogenous vehicle costs


def parse_num(num: str):
    try:
        return int(num)
    except ValueError:
        val = float(num)
        return int(val) if val.is_integer() else val


def split_and_convert(line):
    return [parse_num(num) for num in line.split()]


def parse(path):
    with open(path, "r") as fh:
        lines = fh.readlines()

    # The instances are not perfectly formatted as VRPLIB instance. "GOOD"
    # lines are the ones that are already in VRPLIB format, "BAD" are the ones
    # that need to be parsed separately.
    GOOD = lines[:5] + lines[14:]
    BAD = lines[5:14]

    instance = vrplib.parse.parse_vrplib("".join(GOOD))

    num_types = int(BAD[0].split(":")[1])
    capacities = split_and_convert(BAD[2])
    fixed_costs = [round(val * SCALE) for val in split_and_convert(BAD[4])]
    variable_costs = [round(val * SCALE) for val in split_and_convert(BAD[6])]
    num_vehicles = split_and_convert(BAD[8])

    vehicles_capacity = []
    vehicles_fixed_cost = []
    vehicles_unit_distance_cost = []

    for veh_type in range(num_types):
        num = num_vehicles[veh_type]
        vehicles_capacity.extend(num * [capacities[veh_type]])
        vehicles_fixed_cost.extend(num * [fixed_costs[veh_type]])
        vehicles_unit_distance_cost.extend(num * [variable_costs[veh_type]])

    data = {
        "NAME": path.stem.upper(),
        "COMMENT": instance["comment"].replace('"', "")
        + " Converted to PyVRP's VRPLIB dialect.",
        "TYPE": instance["type"],
        "DIMENSION": instance["dimension"],
        "VEHICLES": sum(num_vehicles),
        "EDGE_WEIGHT_TYPE": instance["edge_weight_type"],
        "NODE_COORD_SECTION": instance["node_coord"],
        "DEMAND_SECTION": instance["demand"],
        "CAPACITY_SECTION": vehicles_capacity,
        "VEHICLES_FIXED_COST_SECTION": vehicles_fixed_cost,
        "VEHICLES_UNIT_DISTANCE_COST_SECTION": vehicles_unit_distance_cost,
        "DEPOT_SECTION": [1],
    }

    if all(val == 0 for val in data["VEHICLES_FIXED_COST_SECTION"]):
        del data["VEHICLES_FIXED_COST_SECTION"]

    if all(val == 1 for val in data["VEHICLES_UNIT_DISTANCE_COST_SECTION"]):
        del data["VEHICLES_UNIT_DISTANCE_COST_SECTION"]

    return data


if __name__ == "__main__":
    OUT = Path("instances/")

    # Run from inside HFVRP/ directory.
    for loc in Path("raw/instances").glob("*.vrp"):
        parsed = parse(loc)
        out_loc = OUT / loc.with_suffix(".vrp").name
        vrplib.write_instance(out_loc, parsed)
