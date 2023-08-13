#######################################################
# Overview
#
# Script defines two versions of fibonacci sequences.
# This code will be cythonized. No types or anything
# specific provided. Goal is to take python syntax
# and make it faster.
#
# Reference: https://ron.sh/compiling-python-code-with-cython/#:~:text=What%20Cython%20does%20is%20convert%20your%20Python%20code,depends%20on%20how%20optimized%20your%20Python%20code%20is.
#######################################################

#!/usr/bin/env tempEnv

# %%
def recursive_fibonacci(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * recursive_fibonacci(x-1)
    
def iterative_fibonacci(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        i = 2
        for i in range(x-1, 1, -1):
            x = x*i
        return x

# %%
