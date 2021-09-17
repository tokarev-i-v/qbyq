from src.circuit.circuit import QuantumCircuit
from src.state.state import QuantumState
from src.gates import pauli
from src.algorithms.decomposition.sc import make_cs_decompose
import numpy as np
from scipy.stats import unitary_group

operator = np.array([
    [1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,-1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,-1,0],
    [0,0,0,0,0,0,0,1],
],)
# print(make_cs_decompose(operator, 4, 4))

qs = QuantumState(vec=np.array([0, 1, 0, 1]))

print(qs)
