import numpy as np

class HalfSpinOperator:
    """Creates the 1/2-spin operators
            σx, σy, σz, σ+, σ-
    for all the spins in a spin chain with lengh N.
    """
    sigma = {}
    z_projector = {}

    def __init__(self, chain_lenght):
        self.dimension = chain_lenght
        self.sigma['x'] = self.__generate_operator(sigma_x, chain_lenght)
        self.sigma['y'] = self.__generate_operator(sigma_y, chain_lenght)
        self.sigma['z'] = self.__generate_operator(sigma_z, chain_lenght)
        self.sigma['+'] = self.__generate_operator(sigma_plus, chain_lenght)
        self.sigma['-'] = self.__generate_operator(sigma_minus, chain_lenght)
        self.z_projector[0] = self.__generate_operator(basis_z[0], chain_lenght)
        self.z_projector[1] = self.__generate_operator(basis_z[1], chain_lenght)

    def __generate_operator(self, op, chain_lenght):
        acc = []
        for i in range(chain_lenght):
            acc.append(self.__core_generate_operator(op, chain_lenght, i))
        return acc

    def __core_generate_operator(self, op, chain_length, index):
        chain = 1
        for i in range(chain_length):
            chain = np.kron(chain, op if i == index else identity)
        return chain


# Single operators definitions
identity = np.eye(2)
sigma_x = np.array([[0., 1.],
                    [1., 0.]])

sigma_y = np.array([[0., -1.j],
                    [1.j, 0.]])

sigma_z = np.array([[1., 0.],
                    [0., -1.]])

sigma_plus = .5 * (sigma_x + 1j * sigma_y)
sigma_minus = .5 * (sigma_x - 1j * sigma_y)

basis_z = np.array([
    # Projector: |0><0|
    [[1., 0.],
     [0., 0.]],
    # Projector: |1><1|
    [[0., 0.],
     [0., 1.]]
])