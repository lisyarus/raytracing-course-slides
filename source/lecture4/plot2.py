#!/usr/bin/env python3

import math
import numpy
import matplotlib.pyplot as pyplot

def f(x):
	return numpy.sin(x)

def sample1(N):
	return numpy.random.uniform(high=math.pi/2.0, size=N)

def p1(x):
	return numpy.ones(x.shape) * 2.0 / math.pi

def sample2(N):
	return numpy.maximum.reduce([sample1(N), sample1(N)])

def p2(x):
	return x * 8.0 / math.pi / math.pi

def monte_carlo(x, f, p, indices):
	return numpy.cumsum(f(x) / p(x)) / indices

N = 1000
indices = numpy.arange(1, N+1)

x1 = sample1(N)
y1 = monte_carlo(x1, f, p1, indices)

x2 = sample2(N)
y2 = monte_carlo(x2, f, p2, indices)

pyplot.plot(indices, y1, label="p1")
pyplot.plot(indices, y2, label="p2")
pyplot.plot([1, N], [1,1], '--', label="true")
pyplot.legend()
pyplot.show()