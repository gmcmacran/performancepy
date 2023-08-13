
# Project overview

This repo explores different ways off making python fast.

Ideas explored:

- Cython
- Threading
- Multiprocessing

# Cython

Cython did not install in my main conda environment. I created an
environment for this project. Installing it along with other packages is
a problem for another day.

conda create -n tempEnv python=3.10 cython ipykernel

fibonacci.pyx defines two cython functions. cython_performance_test does
a simple benchmark.

# Threading POC

A very simple example of multithreading in python.

# Multiprocessing POC

A very simple example of multiprocessing in python. Per official docs,
multiprocessing does not work with an interactive console! Thus this
method is not very useful to me. Code should work if executed the
correct way. However, I did not bother to figure out how to call it
correctly. I am always in an interactive console.
