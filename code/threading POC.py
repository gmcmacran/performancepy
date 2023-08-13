##########################################
# Overview
#
# A simple python script that uses
# threads. Goal is  to sucessfully
# use threads. Not concenered with
# performance.
##########################################

# %%
import concurrent.futures

# %%
def recursive_fibonacci(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * recursive_fibonacci(x-1)

# %%
N = 4
args = list(range(1558-N, 1558, 1))
args

# %%
with concurrent.futures.ThreadPoolExecutor(max_workers=N) as executor:
        results = executor.map(recursive_fibonacci, args)

# %%
list(results)

