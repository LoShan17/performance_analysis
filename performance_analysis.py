import numpy as np
from numba import jit, vectorize
import time

@jit(nopython=True)
def simple_returns(t1, t0):
    return t1/t0 - 1

@jit(nopython=True)
def loop_numba_returns(array: np.array) -> np.array:
    returns = np.zeros(len(array) -1)
    for index in range(len(array) - 1):
        returns[index] = simple_returns(array[index + 1], array[index])
    return returns

def vectorized_np_returns(array: np.array) -> np.array:
    return array[1:]/array[:-1] - 1

def loop_np_returns(array: np.array) -> np.array:
    returns = np.zeros(len(array) -1)
    for index in range(len(array) - 1):
        returns[index] = simple_returns(array[index + 1], array[index])
    return returns

if __name__ == "__main__":
    example_array = np.random.randint(low=50, high=100, size=10000000)

    loop_numba_start = time.time()
    r1 = loop_numba_returns(example_array)
    loop_numba_end = time.time()

    vectorized_np_start = time.time()
    r2 = vectorized_np_returns(example_array)
    vectorized_np_end = time.time()

    loop_np_start = time.time()
    r3 = loop_np_returns(example_array)
    loop_np_end = time.time()

    print(r1)
    print(r2)
    print(r3)
