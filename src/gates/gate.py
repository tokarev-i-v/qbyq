from typing import Iterable
import typing
import numpy as np
from src.gates.operator import Operator

class Gate:
    def __init__(self, operator:Iterable, qubits:Iterable, controlled:bool = False, parametrized:bool = False):
        self.qubits = qubits
        self.operator = operator
        self.controlled = controlled
        self.parametrized = parametrized

    def apply(self, state):
        return self.operator @ state

    def expand_by_identical(self) -> Gate:
        for i in self.qubits:
            q = self.qubits[i]

    def make_controlled(self, control_qubits_count: int):
        """returns controlled version of this gate"""

        pass