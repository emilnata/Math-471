import lgrng as lg
import numpy as np
from numpy import array

def hat(x):
        return 1.0 - abs(x)

def sin4px(x):
	return np.sin(4*np.pi*x)


def pblm5():
	nlist = array([5, 10, 20, 30, 40, 50, 100])
	elist = np.empty(nlist.shape)
	xx = np.linspace(-1,1,4000)*0.99+1e-3
	
	from matplotlib import pyplot as plt
	for i,n in enumerate(nlist):
		x = lg.gr.unif(n)
		elist[i] = lg.demo(hat, x, xx, showplot='no')
		plt.close()
		
	plt.semilogy(nlist, elist, lw = 2, c='r')
	plt.axis('tight')
	plt.grid()
	plt.title('error in |x|, interp at unif pts, vs n')
	plt.show()
	

def pblm6():
	nlist = array([5, 10, 20, 30, 40, 50, 100, 400, 800])
	elist = np.empty(nlist.shape)
	xx = np.linspace(-1,1,4000)*0.99+1e-3
	
	from matplotlib import pyplot as plt
	for i,n in enumerate(nlist):
		x = lg.gr.cheb(n)
		elist[i] = lg.demo(hat, x, xx, showplot='no')

	plt.loglog(nlist, elist, lw = 2, c='r')
	plt.axis('tight')
	plt.grid()
	plt.title('error in |x|, interp at cheb pts, vs n')
	plt.show()
		
def pblm7():
	nlist = array([5, 10, 20, 30, 40, 50, 100])
	elist = np.empty(nlist.shape)
	xx = np.linspace(-1,1,4000)*0.99+1e-3
	
	from matplotlib import pyplot as plt
	for i,n in enumerate(nlist):
		x = lg.gr.cheb(n)
		elist[i] = lg.demo(sin4px, x, xx, showplot='no')
		
	
	plt.semilogy(nlist, elist, lw = 2, c='r')
	plt.axis('tight')
	plt.grid()
	plt.title('error in $sin4\pi x$, interp at cheb pts, vs n')
	plt.show()
	
