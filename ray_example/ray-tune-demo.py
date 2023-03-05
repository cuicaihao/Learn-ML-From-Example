import functools
import os
import time
import numpy as np
import ray
from ray import tune
from ray.tune.suggest.hyperopt import HyperOptSearch


def timeit(func):
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(
            "function [{}] finished in {} ms".format(
                func.__name__, int(elapsed_time * 1_000)
            )
        )
        return result

    return new_func


def simulate_single_thread(num_sims: int):
    return sum(np.random.normal(0, 1, num_sims))


@timeit
def simulate(num_threads: int) -> float:
    number_of_simulations_to_run = 100_000_000
    number_of_simulations_per_thread = int(number_of_simulations_to_run / num_threads)

    workfn = ray.remote(simulate_single_thread)

    results = ray.get(
        [
            workfn.remote(params)
            for params in [number_of_simulations_per_thread] * num_threads
        ]
    )

    return sum(results)


def loss_fn(a: float, b: float, c: float) -> float:
    # minimised at:
    #   a=10
    #   b=10
    #   c=0
    #   minimum_value=-5
    return c - a * b / (a + b)


def objective_fn(params: dict) -> None:
    # each trial gets a package of 1 CPU for main process and 3 CPUs for multiprocessing
    # so we can run a distributed ray process inside this trial
    # note that we don't need to call `ray.init()` as it's already running
    simulate(num_threads=3)

    # calculate loss
    loss = loss_fn(a=params["a"], b=params["b"], c=params["c"])

    # report trial results back to main process
    tune.report(iterations=0, loss=loss)


def main():
    searcher = HyperOptSearch()

    analysis = tune.run(
        objective_fn,
        metric="loss",
        mode="min",
        search_alg=searcher,
        num_samples=100,
        max_concurrent_trials=8,
        verbose=1,
        resources_per_trial=tune.PlacementGroupFactory(
            [
                {"CPU": 1},  # this bundle will be used by the trainable itself
                {"CPU": 3},  # this bundle will be used within a trial
            ],
            strategy="PACK",
        ),
        config={
            "a": tune.quniform(0, 10, 0.1),
            "b": tune.quniform(0, 10, 0.1),
            "c": tune.quniform(0, 10, 0.1),
        },
    )

    return analysis


if __name__ == "__main__":
    main()
