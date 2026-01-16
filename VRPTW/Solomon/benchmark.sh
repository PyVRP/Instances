#!/usr/bin/env bash
uv run --with pyvrp==0.11 benchmark.py --max_runtime 10 --detailed --seed 0 --num_procs 12
