import ncalc
from ncalc.test import f #sin(pi*x)
from ncalc.test import df #pi*cos(pi*x)


def error(h):
    """\
    error(h): x = n*[0,h,..99*h]
    find error in df computed using fwd differences
    return error (h = const intvl spacing)
    """
    import numpy as np
    x = np.arange(0,100)
    x = 1.0+ 1.0*h*x
    
    y = f(x)
    dy = df(x)
    dyf = ncalc.diff.fwd(y, h)
    err = max(abs(dy[:-1]-dyf))
    return err

def demo():
    nlist = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 10**9,
         10**10, 10**11, 10**12, 10**13, 10**14, 10**15]
         
    l = len(nlist)
    import numpy as np
    err = np.empty(l)
    h = np.empty(l)
    
    for i,n in enumerate(nlist):
        h[i] = 1.0/n
        err[i] = error(h[i])

    from matplotlib import pyplot as plt
    plt.loglog(h, err)
    plt.xlabel('h')
    plt.ylabel('error in fwd difference')
