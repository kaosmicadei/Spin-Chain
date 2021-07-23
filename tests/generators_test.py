import sys
sys.path.append(sys.path[0] + '/../src')
from generators import HalfSpinOperator

N = 2
op = HalfSpinOperator(N)

for i in 'xyz+-':
    print(f'operator: {i}', end='\n\n')
    for j in range(N):
        print(f'spin: {j}', end='\n\n')
        print(op.sigma[i][j], end='\n\n')
    print('---', end='\n\n')
