import timeit
import numpy as np
from math import factorial


def cos_approx(x,order):
    return sum((-1)**n * x**(2*n)/(2*factorial(n)) for n in range(order+1))

a = 3.14/3
order = 10
def benchmark_cos_approx():
    cos_approx(a,order)
    pass

def benchmark_cos():
    np.cos(a)
    pass

execution_time = timeit.Timer(benchmark_cos_approx).timeit(number = 100000)/100000
print("Execution of cos_approx took " + str(execution_time*1e9) + " ns")

execution_time = timeit.Timer(benchmark_cos).timeit(number = 100000)/100000
print("Execution of np.cos took " + str(execution_time*1e9) + " ns")

