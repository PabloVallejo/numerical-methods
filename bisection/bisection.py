from numpy import *

#
# Simple bisection implementation.
#
#	def fn(x):
#		return x * x
#
#	bisection(1, 2, fn, 1000, 0.01)
#
# def bisection(a, b, fn, n0, tol):
# 	i = 1

# 	while i <= n0:
# 		p = (a + b) / 2.0
# 		fp = fn(p)

# 		if fp == 0 or abs(b - a) / 2.0 < tol
# 			return p

# 		fa = fn(a)
# 		i = i + 1

# 		if fa * fp > 0
# 			a = p
# 		else:
# 			b = p

# 	return None

def fn(x):
	return x**2 + exp(-2 * x) - (2 * x * exp(-x))

def dfn(x):
	return 2 * exp(-2 * x) * (exp(x) + 1) * (exp(x) * x - 1)

def netwon(f, df, x_0, maxiter=50, xtol=1.9e-6, ftol=1.0e-6):
	x = float(x_0)
	for i in xrange(maxiter):
		dx = -f(x) / df(x)

		x = x + dx
		print i
		if abs(dx / x) < xtol and abs(f(x)) < ftol:
			print i
			return x

	return 'No hubo convergencia'


def sn(x):
	return sin(2/x)

def secant(f, x0, x1, tol=0.001, nmax=100):
	n = 1

	while n <= nmax:
		x2 = x1 - f(x1) * ( (x1 - x0) / (f(x1) - f(x0)))

		if abs(x2 - x1) < tol:
			print n
			return x2

		else:
			x0 = x1
			x1 = x2

		n = n + 1

	return False

