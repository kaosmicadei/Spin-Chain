import numpy as np

identity = np.eye(2)
sigmaX = np.array([[0., 1.], [1., 0.]])
sigmaY = np.array([[0., -1.j], [1.j, 0.]])
sigmaZ = np.array([[1., 0.], [0., -1.]])
sigmaPlus = .5 * (sigmaX + 1j * sigmaY)
sigmaMinus = .5 * (sigmaX - 1j * sigmaY)

basisZ = np.array([
    # Projector: |0><0|
    [[1., 0.], [0., 0.]],
    # Projector: |1><1|
    [[0., 0.], [0., 1.]]
])

def core_generate_operator(op, chain_length, index):
    chain = 1
    for ii in np.arange(chain_length):
        chain = np.kron(chain, op if ii == index else identity)
    return chain

def generate_operator(op, chain_lenght):
    acc = []
    for ii in np.arange(chain_lenght):
        acc.append(core_generate_operator(op, chain_lenght, ii))
    return acc
