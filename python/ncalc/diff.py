def fwd(y, h):
	dy = (y[1:] - y[:-1])/h
	return dy

def cntrd(y, h):
	dy = (y[2:]-y[:-2])/(2.0*h)
	return dy
