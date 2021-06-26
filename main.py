from generators import *

N = 3
sx = generate_operator(sigmaX, N)
for i in range(N):
    print(sx[i], '\n')
