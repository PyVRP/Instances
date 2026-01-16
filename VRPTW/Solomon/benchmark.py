import argparse
from functools import partial
from pathlib import Path

import numpy as np
from tqdm.contrib.concurrent import process_map

from pyvrp import read, read_solution, solve, CostEvaluator
from pyvrp.stop import MaxRuntime


def _solve(path: Path, max_runtime: int, seed: int) -> float:
    data = read(path, round_func="dimacs")
    stop = MaxRuntime(max_runtime)
    result = solve(data, stop, seed=seed, display=False)
    return result.cost()


def _bks(path: Path) -> float:
    data = read(path, round_func="dimacs")
    sol_path = path.with_suffix(".sol")
    bks_sol = read_solution(sol_path, data)
    return CostEvaluator([], 0, 0).cost(bks_sol)


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("--max_runtime", type=int, default=10)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--num_procs", type=int, default=8)
    parser.add_argument(
        "--detailed", action="store_true", help="Print gap for each instance"
    )
    args = parser.parse_args()

    dir_path = Path(__file__).parent
    instances = sorted(dir_path.glob("*.vrp"))

    solve_func = partial(_solve, max_runtime=args.max_runtime, seed=args.seed)
    costs = process_map(solve_func, instances, max_workers=args.num_procs)
    bks_costs = [_bks(path) for path in instances]
    names = [inst.stem for inst in instances]

    detailed = []
    for cost, bks_cost, name in zip(costs, bks_costs, names):
        gap = (cost - bks_cost) / bks_cost * 100
        detailed.append((name, cost, bks_cost, gap))

    gaps = np.array([gap for *_, gap in detailed])
    num_opt = sum(gap == 0 for gap in gaps)

    if args.detailed:
        print(f"\n{'Instance':<10} {'Cost':>10} {'BKS':>10} {'Gap (%)':>10}")
        print("-" * 44)
        for name, cost, bks_cost, gap in sorted(detailed):
            print(f"{name:<10} {cost:>10} {bks_cost:>10} {gap:>10.2f}")
        print("-" * 44)

    print(f"\nSummary (runtime={args.max_runtime}s, seed={args.seed}):")
    print(f"  Instances: {len(gaps)}")
    print(f"  Optimal:   {num_opt}")
    print(f"  Avg gap:   {gaps.mean():.2f}% (+/- {gaps.std():.2f}%)")


if __name__ == "__main__":
    main()
