
#
# Simple bisection implementation.
#
#	def fn(x):
#		return x * x
#
#	bisection(1, 2, fn, 1000, 0.01)
#
def bisection(a, b, fn, n0, tol):
	i = 1

	while i <= n0:
		p = (a + b) / 2.0
		fp = fn(p)

		if fp == 0 or abs(b - a) / 2.0 < tol
			return p

		fa = fn(a)
		i = i + 1

		if fa * fp > 0
			a = p
		else:
			b = p

	return None