#!/usr/bin/env python3

import numpy
import matplotlib.pyplot as pyplot

def f(x):
	return numpy.where(x < 0.5, numpy.zeros(x.shape), x * x)

def sample1(N):
	return numpy.random.uniform(size=N)

def p1(x):
	return numpy.ones(x.shape)

def sample2(N):
	return numpy.random.uniform(low=0.5, size=N)

def p2(x):
	return 2.0 * numpy.ones(x.shape)

def monte_carlo(x, f, p, indices):
	return numpy.cumsum(f(x) / p(x)) / indices

N = 1000
indices = numpy.arange(1, N+1)

x1 = sample1(N)
y1 = monte_carlo(x1, f, p1, indices)

x2 = sample2(N)
y2 = monte_carlo(x2, f, p2, indices)

pyplot.plot(indices, y1, label="U(0,1)")
pyplot.plot(indices, y2, label="U(1/2,1)")
pyplot.legend()
pyplot.show()