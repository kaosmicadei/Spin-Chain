from generators import OpGenerator
import numpy as np

class XYModel:
    H0 = 0
    Hint = 0

    def __init__(self, op: OpGenerator):
        self.dimension = op.dimension

        for i in range(1, op.dimension):
            self.H0 += op.sigma['z'][i]

        for i in range(op.dimension-1):
            self.Hint += np.matmul(op.sigma['x'][i], op.sigma['x'][i+1]) + \
                         np.real(np.matmul(op.sigma['y'][i], op.sigma['y'][i+1]))
