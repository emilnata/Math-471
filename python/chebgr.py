def chebn(x, n):
        """\
        eval T_n(x)
        """
        import numpy as np
        for xx in x:
                assert -1 <= xx and xx <= 1
        
        th = np.arccos(x)
        return np.cos(n*th)

def plot(n, c):
        from matplotlib import pyplot as plt
        import numpy as np
        x = np.linspace(-1,1,500)
        y = chebn(x, n)
        plt.plot(x, y, lw = 2, c = c)

if __name__ == '__main__':
        plot(0, 'm')
        plot(1, 'k')
        plot(2, 'r')
        plot(3, 'g')
        plot(4, 'b')
        plot(5, 'y')
        from matplotlib import pyplot as plt
        plt.axis('tight')
        plt.grid()
        plt.show()
