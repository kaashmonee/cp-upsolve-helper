import unittest
import time

INF = 1e11

def run(cl):
    def wrapper():
        unittest.TextTestRunner().run(unittest.TestSuite([unittest.TestLoader().loadTestsFromTestCase(cl)]))
    wrapper()

def timeit(fun):
    def wrapper(self=None):
        print(f"timing {fun.__name__}")
        result = 0
        if self is None:
            start = time.time()
            result = fun()
            end = time.time()
        else:
            start = time.time()
            result = fun(self)
            end = time.time()
        print("elapsed:", end-start)
        return result
    return wrapper
