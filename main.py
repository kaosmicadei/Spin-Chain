import numpy as np
from generators import HalfSpinOperator
from hamiltonian import XYModel

# =========================
# SPIN CHAIN INITIALISATION
# =========================
N = 3
op = HalfSpinOperator(N)
hamiltonian = XYModel(op, coupling_constant=-0.5, omega=0.5)


# =================
# STATE PREPARATION
# =================

# Thermal chain:
#       Here the partition function is been considered as the trace of the whole
#       chain. The issue is the first Hilbert space is not populated yet,
#
#           chain = 1 ⊗ exp(-beta H0) ⟹ Tr chain = 2*Z.
#
#       So it's necessary "fix" the normalisation before add the initial state
#       of the first spin.
beta = 1
thermal_chain = np.exp(-beta * np.diag(hamiltonian.H0))
partition_function = np.sum(thermal_chain)
thermal_chain = 2.0 * np.diag(thermal_chain / partition_function)

# State to be transmited through the chain
message_state = op.z_projector[0][0]

# Whole initial system
init_state = np.matmul(message_state, thermal_chain)
print(init_state)
