import timeit
from functools import partial
from .origmike import main as mn

argv = [0, "databases/small.db", "sequences/1.txt"]
mn()
