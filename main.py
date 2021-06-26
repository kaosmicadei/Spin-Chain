import numpy as np
from generators import OpGenerator
from hamiltonian import Hamiltonian

N = 3
op = OpGenerator(N)
hamiltonian = Hamiltonian(op)
print(hamiltonian.H0, '\n')
print(hamiltonian.Hint, '\n')
