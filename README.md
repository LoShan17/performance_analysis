# Performance study using numpy, numba and vectorization techniques
I wanted to compare profiled results (using standard Python cProfile) between standard
vectorized numpy syntax, numba loops implementations (both "vectorize" and "jit"),
and a standard Python loop over a numpy array.
