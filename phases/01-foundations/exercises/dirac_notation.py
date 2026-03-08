"""Dirac Notation for Quantum Computing.

Exercises covering bra-ket notation, the language of quantum mechanics.
Builds on linear algebra to express quantum states and operations concisely.
"""

import numpy as np
from numpy.typing import NDArray


# Standard basis states
KET_0 = np.array([1, 0], dtype=complex)
KET_1 = np.array([0, 1], dtype=complex)


def ket(label: str) -> NDArray:
    """Return the standard basis ket vector for the given label.

    Supports: '0', '1', '+', '-', 'i', '-i'
    |0> = [1, 0]^T
    |1> = [0, 1]^T
    |+> = (|0> + |1>) / sqrt(2)
    |-> = (|0> - |1>) / sqrt(2)
    |i> = (|0> + i|1>) / sqrt(2)
    |-i> = (|0> - i|1>) / sqrt(2)
    """
    raise NotImplementedError


def bra(label: str) -> NDArray:
    """Return the bra vector (conjugate transpose of ket).

    <label| = |label>^dagger
    """
    raise NotImplementedError


def braket(bra_label: str, ket_label: str) -> complex:
    """Compute the inner product <bra_label|ket_label>.

    This gives the probability amplitude for transitioning
    from |ket_label> to |bra_label>.
    """
    raise NotImplementedError


def ketbra(ket_label: str, bra_label: str) -> NDArray:
    """Compute the outer product |ket_label><bra_label|.

    This creates a projection operator (when ket=bra) or
    a transition operator (when ket!=bra).
    """
    raise NotImplementedError


def projector(label: str) -> NDArray:
    """Compute the projector |label><label|.

    Projectors satisfy P^2 = P and are used in measurement.
    """
    raise NotImplementedError


def measurement_probability(state: NDArray, basis_label: str) -> float:
    """Compute probability of measuring |basis_label> given |state>.

    P(basis_label) = |<basis_label|state>|^2

    This is the Born rule — the fundamental link between
    quantum amplitudes and observable probabilities.
    """
    raise NotImplementedError


def post_measurement_state(state: NDArray, outcome_label: str) -> NDArray:
    """Return the state after measuring outcome |outcome_label>.

    After measurement, the state collapses to:
    |outcome_label><outcome_label|state> / ||<outcome_label|state>||

    Returns the normalized post-measurement state.
    Raises ValueError if measurement probability is zero.
    """
    raise NotImplementedError


def multi_qubit_ket(labels: str) -> NDArray:
    """Construct a multi-qubit computational basis state.

    Examples:
        '00' -> |00> = |0> ⊗ |0> = [1, 0, 0, 0]^T
        '01' -> |01> = |0> ⊗ |1> = [0, 1, 0, 0]^T
        '10' -> |10> = |1> ⊗ |0> = [0, 0, 1, 0]^T
        '11' -> |11> = |1> ⊗ |1> = [0, 0, 0, 1]^T

    Only supports '0' and '1' characters.
    """
    raise NotImplementedError


def bell_state(name: str) -> NDArray:
    """Construct a Bell state.

    |Φ+> = (|00> + |11>) / sqrt(2)    name='phi+'
    |Φ-> = (|00> - |11>) / sqrt(2)    name='phi-'
    |Ψ+> = (|01> + |10>) / sqrt(2)    name='psi+'
    |Ψ-> = (|01> - |10>) / sqrt(2)    name='psi-'
    """
    raise NotImplementedError
