import sys
sys.path.append(sys.path[0] + '/../src')
from generators import HalfSpinOperator
from hamiltonian import XYModel

N = 2
op = HalfSpinOperator(N)
h = XYModel(op)

print('H0:', end='\n\n')
print(h.H0, end='\n\n')
print('Hint:', end='\n\n')
print(h.Hint)