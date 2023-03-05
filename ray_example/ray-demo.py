import functools
import os
import time
import numpy as np
import ray


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


def main():
    ray.init()
    print(f"number of CPUs available: {os.cpu_count()}")
    simulate(num_threads=1)
    simulate(num_threads=os.cpu_count())


if __name__ == "__main__":
    main()
