###################################
# Overview
#
# Simple script to compare four functions.
#
# 1: py_recursive_fibonacci (regular python)
# 2: py_iterative_fibonacci (regular python)
# 3: recursive_fibonacci (cython)
# 4: iterative_fibonacci (cython)
###################################

# %%
import pyximport
pyximport.install()
import os
import time
from fibonacci import recursive_fibonacci, iterative_fibonacci

# %%
os.chdir("S://Python//projects//performancepy")

# %%
def py_recursive_fibonacci(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * py_recursive_fibonacci(x-1)
    
def py_iterative_fibonacci(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        for i in range(x-1, 1, -1):
            x = x*i
        return x

# %%
# Anthing larger than 2970 causes recurive python function to error.
x = 2970

# %%
start = time.time()
py_recursive_fibonacci(x)
end = time.time()
computeTime = str(end - start)
print("Python recursive_fibonacci: " + computeTime)

# %%
start = time.time()
recursive_fibonacci(x)
end = time.time()
computeTime = str(end - start)
print("Cython recursive_fibonacci: " + computeTime)

# %%
start = time.time()
py_iterative_fibonacci(x)
end = time.time()
computeTime = str(end - start)
print("Python iterative_fibonacci: " + computeTime)

# %%
start = time.time()
iterative_fibonacci(x)
end = time.time()
computeTime = str(end - start)
print("Cython iterative_fibonacci: " + computeTime)

# %%
