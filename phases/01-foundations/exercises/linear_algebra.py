"""Linear Algebra for Quantum Computing.

Exercises covering vector operations, matrix properties, and
eigentheory — the mathematical backbone of quantum mechanics.
"""

import numpy as np
from numpy.typing import NDArray


def inner_product(v1: NDArray, v2: NDArray) -> complex:
    """Compute the inner product <v1|v2> = v1^dagger @ v2.

    In quantum mechanics, <psi|phi> gives the overlap between states.
    Note: uses conjugate-linear convention (conjugate the first argument).
    """
    raise NotImplementedError


def is_normalized(v: NDArray, tol: float = 1e-10) -> bool:
    """Check if a vector is normalized (unit length).

    Quantum states must be normalized: <psi|psi> = 1.
    """
    raise NotImplementedError


def normalize(v: NDArray) -> NDArray:
    """Return a normalized copy of vector v.

    v_normalized = v / ||v||
    """
    raise NotImplementedError


def outer_product(v1: NDArray, v2: NDArray) -> NDArray:
    """Compute the outer product |v1><v2| = v1 @ v2^dagger.

    Outer products build projection operators and density matrices.
    """
    raise NotImplementedError


def is_hermitian(M: NDArray, tol: float = 1e-10) -> bool:
    """Check if matrix M is Hermitian (M = M^dagger).

    Hermitian matrices represent physical observables in QM.
    They have real eigenvalues and orthogonal eigenvectors.
    """
    raise NotImplementedError


def is_unitary(M: NDArray, tol: float = 1e-10) -> bool:
    """Check if matrix M is unitary (M @ M^dagger = I).

    Unitary matrices represent quantum gates / time evolution.
    They preserve inner products and probabilities.
    """
    raise NotImplementedError


def commutator(A: NDArray, B: NDArray) -> NDArray:
    """Compute the commutator [A, B] = AB - BA.

    Non-zero commutator means observables can't be simultaneously measured
    (uncertainty principle). Returns a new matrix.
    """
    raise NotImplementedError


def tensor_product(A: NDArray, B: NDArray) -> NDArray:
    """Compute the tensor (Kronecker) product A ⊗ B.

    Tensor products combine quantum systems:
    |psi> ⊗ |phi> represents a composite system.
    """
    raise NotImplementedError


def spectral_decomposition(M: NDArray) -> tuple[NDArray, NDArray]:
    """Compute the spectral decomposition of a Hermitian matrix.

    M = sum_i lambda_i |v_i><v_i|

    Returns (eigenvalues, eigenvectors) where eigenvectors are columns.
    Eigenvalues sorted in ascending order.
    """
    raise NotImplementedError


def expectation_value(operator: NDArray, state: NDArray) -> float:
    """Compute <psi|O|psi> — the expectation value of operator O in state |psi>.

    This is the average measurement outcome for observable O.
    Result must be real for Hermitian operators.
    """
    raise NotImplementedError
