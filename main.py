import numpy as np
from chain import Chain

zero = np.array([[.9, 0.],
                 [0., .1]])

# Initialisation
N = 5
dt = 0.001
chain = Chain(N, coupling_constant=0.5, omega=0.5, message_state=zero, dt=dt)

# Evolution
time_interval = int(np.pi / dt)
timesteps = 20
step_length = int(np.pi / dt / timesteps)

evolution = [ np.array([chain.bloch_vector(i) for i in range(chain.dimension)]) ]
for t in range(time_interval):
    chain.next()
    if t % step_length:
        evolution.append(np.array([ chain.bloch_vector(i) for i in range(chain.dimension) ]))
evolution = np.array(evolution)
print(evolution[:,:,2])
