from . import diff
from . import diff2
from . import intg
from . import test

def eval(f, x):
        """\
        evaluate f at x
        """
        try:
                y = f(x)
        except:
                import numpy as np
                y = np.zeros(len(x))
                for i,xx in enumerate(x):
                        y[i] = f(xx)
        return y
