import numpy as np
from chain import Chain

rho = np.array([[.7 , -.1j],
                [.1j,  .3 ]])

# Initialisation
N = 5
dt = 0.001
chain = Chain(N, coupling_constant=0.5, omega=0.5, message_state=rho, dt=dt)

# Evolution
time_interval = int(np.pi / dt)
timesteps = 20
step_length = int(np.pi / dt / timesteps)

evolution = [ np.array([chain.bloch_vector(i) for i in range(chain.dimension)]) ]
for t in range(time_interval):
    chain.next()
    if t % step_length:
        evolution.append(np.array([ chain.bloch_vector(i) for i in range(chain.dimension) ]))

# Final result
print('\ninitial chain:\n')
print(evolution[1])
print('\nfinal chain:\n')
print(evolution[-1])

