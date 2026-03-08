"""Tests for linear algebra exercises."""

import numpy as np
import pytest

from linear_algebra import (
    commutator,
    expectation_value,
    inner_product,
    is_hermitian,
    is_normalized,
    is_unitary,
    normalize,
    outer_product,
    spectral_decomposition,
    tensor_product,
)

# Common quantum computing matrices
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
PAULI_Z = np.array([[1, 0], [0, -1]], dtype=complex)
HADAMARD = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
IDENTITY = np.eye(2, dtype=complex)

# Common states
KET_0 = np.array([1, 0], dtype=complex)
KET_1 = np.array([0, 1], dtype=complex)
KET_PLUS = np.array([1, 1], dtype=complex) / np.sqrt(2)
KET_MINUS = np.array([1, -1], dtype=complex) / np.sqrt(2)


class TestInnerProduct:
    def test_orthogonal(self):
        assert inner_product(KET_0, KET_1) == pytest.approx(0.0)

    def test_self(self):
        assert inner_product(KET_0, KET_0) == pytest.approx(1.0)

    def test_plus_minus(self):
        assert inner_product(KET_PLUS, KET_MINUS) == pytest.approx(0.0, abs=1e-10)

    def test_conjugate_symmetry(self):
        v1 = np.array([1, 1j], dtype=complex)
        v2 = np.array([1j, 1], dtype=complex)
        assert inner_product(v1, v2) == pytest.approx(np.conj(inner_product(v2, v1)))


class TestNormalization:
    def test_already_normalized(self):
        assert is_normalized(KET_0)

    def test_not_normalized(self):
        assert not is_normalized(np.array([1, 1], dtype=complex))

    def test_normalize(self):
        v = np.array([3, 4], dtype=complex)
        result = normalize(v)
        assert is_normalized(result)
        assert result[0] == pytest.approx(3.0 / 5.0)


class TestOuterProduct:
    def test_projection(self):
        proj = outer_product(KET_0, KET_0)
        expected = np.array([[1, 0], [0, 0]], dtype=complex)
        np.testing.assert_array_almost_equal(proj, expected)

    def test_shape(self):
        result = outer_product(KET_0, KET_1)
        assert result.shape == (2, 2)


class TestMatrixProperties:
    def test_pauli_hermitian(self):
        assert is_hermitian(PAULI_X)
        assert is_hermitian(PAULI_Y)
        assert is_hermitian(PAULI_Z)

    def test_pauli_unitary(self):
        assert is_unitary(PAULI_X)
        assert is_unitary(PAULI_Y)
        assert is_unitary(PAULI_Z)

    def test_hadamard_unitary(self):
        assert is_unitary(HADAMARD)

    def test_hadamard_hermitian(self):
        assert is_hermitian(HADAMARD)

    def test_non_unitary(self):
        M = np.array([[1, 2], [3, 4]], dtype=complex)
        assert not is_unitary(M)


class TestCommutator:
    def test_self_commutes(self):
        result = commutator(PAULI_X, PAULI_X)
        np.testing.assert_array_almost_equal(result, np.zeros((2, 2)))

    def test_pauli_xy(self):
        result = commutator(PAULI_X, PAULI_Y)
        expected = 2j * PAULI_Z
        np.testing.assert_array_almost_equal(result, expected)

    def test_pauli_yz(self):
        result = commutator(PAULI_Y, PAULI_Z)
        expected = 2j * PAULI_X
        np.testing.assert_array_almost_equal(result, expected)


class TestTensorProduct:
    def test_identity_tensor(self):
        result = tensor_product(IDENTITY, IDENTITY)
        expected = np.eye(4, dtype=complex)
        np.testing.assert_array_almost_equal(result, expected)

    def test_ket_tensor(self):
        result = tensor_product(KET_0, KET_1)
        expected = np.array([0, 1, 0, 0], dtype=complex)
        np.testing.assert_array_almost_equal(result, expected)

    def test_shape(self):
        result = tensor_product(PAULI_X, PAULI_Z)
        assert result.shape == (4, 4)


class TestSpectralDecomposition:
    def test_pauli_z(self):
        eigenvalues, eigenvectors = spectral_decomposition(PAULI_Z)
        assert eigenvalues[0] == pytest.approx(-1.0)
        assert eigenvalues[1] == pytest.approx(1.0)

    def test_reconstruction(self):
        eigenvalues, eigenvectors = spectral_decomposition(PAULI_X)
        reconstructed = sum(
            eigenvalues[i] * np.outer(eigenvectors[:, i], np.conj(eigenvectors[:, i]))
            for i in range(len(eigenvalues))
        )
        np.testing.assert_array_almost_equal(reconstructed, PAULI_X)


class TestExpectationValue:
    def test_z_in_ket0(self):
        assert expectation_value(PAULI_Z, KET_0) == pytest.approx(1.0)

    def test_z_in_ket1(self):
        assert expectation_value(PAULI_Z, KET_1) == pytest.approx(-1.0)

    def test_x_in_plus(self):
        assert expectation_value(PAULI_X, KET_PLUS) == pytest.approx(1.0)

    def test_z_in_plus(self):
        assert expectation_value(PAULI_Z, KET_PLUS) == pytest.approx(0.0, abs=1e-10)
