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
args = list(range(1, N+1, 1))
args


# %%
list(map(recursive_fibonacci, args))

# %%
with concurrent.futures.ProcessPoolExecutor(max_workers=N) as executor:
        results = executor.map(recursive_fibonacci, args)

# %%
print(list(results))

# %%
