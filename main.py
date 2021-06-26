import numpy as np
from chain import Chain

zero = np.array([[.5, .5],
                 [.5, .5]])

N = 3
chain = Chain(N, coupling_constant=-0.5, omega=0.5, message_state=zero)

for i in range(N):
    print(f"{i}: {chain.bloch_vector(i)}",)
