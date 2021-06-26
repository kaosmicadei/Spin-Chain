import numpy as np
from generators import OpGenerator
from hamiltonian import XYModel

# Spin chain initialisation
N = 3
op = OpGenerator(N)
hamiltonian = XYModel(op)

# State preparation
beta = 0.1
thermal_chain = np.exp(-beta * np.diag(hamiltonian.H0))
partition_func = np.sum(thermal_chain)
thermal_chain = np.diag(thermal_chain / partition_func)

# State to be transmited through the chain
message_state = op.z_projector[0][0]

# Initial state of the whole chain
init_state = np.matmul(message_state, thermal_chain)
print(init_state)
