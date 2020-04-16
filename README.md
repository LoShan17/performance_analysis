## Performance study using numpy, numba and vectorization techniques
I wanted to compare profiled results (using standard Python cProfile) between standard
vectorized numpy syntax, numba loops implementations (with a "jit", "njit" comparison),
and a standard Python loop over a numpy array.

The two numba implementations use also an externally defined function that can be applied inside the loop since it is jit compiled as well.

Over multiple runs there is actually a bit of volatility between the standard numpy implementation and the two versions of just in time compiled solutions coming from numba.
Overall numba compiled implementation and standard numpy look equivalent.
And they both are about a factor of 100 faster compared to a simple Python loop over an array.

---------------------------------------------------------------------------------
Following are reported a few profiled runs of performance_analysis.py
---------------------------------------------------------------------------------
10540012 function calls (10518380 primitive calls) in 14.170 seconds

Ordered by: internal time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1   11.961   11.961   13.166   13.166 performance_analysis.py:26(loop_np_returns)
9999999    1.205    0.000    1.205    0.000 performance_analysis.py:5(simple_returns)
1    0.122    0.122    0.122    0.122 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
1579    0.081    0.000    0.081    0.000 ffi.py:105(__call__)
1    0.078    0.078    0.078    0.078 performance_analysis.py:16(loop_numba_returns_njit)
1    0.078    0.078    0.078    0.078 performance_analysis.py:9(loop_numba_returns)
1    0.075    0.075    0.075    0.075 performance_analysis.py:23(vectorized_np_returns)
---------------------------------------------------------------------------------
10540023 function calls (10518391 primitive calls) in 12.989 seconds

Ordered by: internal time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1   11.070   11.070   11.968   11.968 performance_analysis.py:26(loop_np_returns)
9999999    0.898    0.000    0.898    0.000 performance_analysis.py:5(simple_returns)
1    0.117    0.117    0.117    0.117 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
1    0.083    0.083    0.083    0.083 performance_analysis.py:16(loop_numba_returns_njit)
1    0.077    0.077    0.077    0.077 performance_analysis.py:9(loop_numba_returns)
1579    0.076    0.000    0.076    0.000 ffi.py:105(__call__)
1    0.074    0.074    0.074    0.074 performance_analysis.py:23(vectorized_np_returns)---------------------------------------------------------------------------------
10540222 function calls (10518582 primitive calls) in 14.061 seconds

Ordered by: internal time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1   11.956   11.956   13.004   13.004 performance_analysis.py:26(loop_np_returns)
9999999    1.048    0.000    1.048    0.000 performance_analysis.py:5(simple_returns)
1    0.139    0.139    0.139    0.139 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
1    0.114    0.114    0.114    0.114 performance_analysis.py:16(loop_numba_returns_njit)
1579    0.083    0.000    0.083    0.000 ffi.py:105(__call__)
1    0.074    0.074    0.074    0.074 performance_analysis.py:9(loop_numba_returns)
1    0.072    0.072    0.072    0.072 performance_analysis.py:23(vectorized_np_returns)
---------------------------------------------------------------------------------
10540208 function calls (10518568 primitive calls) in 13.662 seconds

Ordered by: internal time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1   11.704   11.704   12.633   12.633 performance_analysis.py:26(loop_np_returns)
9999999    0.929    0.000    0.929    0.000 performance_analysis.py:5(simple_returns)
1    0.124    0.124    0.124    0.124 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
1    0.085    0.085    0.085    0.085 performance_analysis.py:16(loop_numba_returns_njit)
1    0.078    0.078    0.078    0.078 performance_analysis.py:23(vectorized_np_returns)
1579    0.076    0.000    0.076    0.000 ffi.py:105(__call__)
1    0.075    0.075    0.075    0.075 performance_analysis.py:9(loop_numba_returns)
---------------------------------------------------------------------------------
10540200 function calls (10518560 primitive calls) in 14.899 seconds

Ordered by: internal time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1   12.645   12.645   13.747   13.747 performance_analysis.py:26(loop_np_returns)
9999999    1.102    0.000    1.102    0.000 performance_analysis.py:5(simple_returns)
1    0.120    0.120    0.120    0.120 {method 'randint' of 'numpy.random.mtrand.RandomState' objects}
1    0.095    0.095    0.095    0.095 performance_analysis.py:9(loop_numba_returns)
1579    0.094    0.000    0.094    0.000 ffi.py:105(__call__)
1    0.081    0.081    0.081    0.081 performance_analysis.py:23(vectorized_np_returns)
1    0.076    0.076    0.076    0.076 performance_analysis.py:16(loop_numba_returns_njit)
---------------------------------------------------------------------------------
