"""Tests for Dirac notation exercises."""

import numpy as np
import pytest

from dirac_notation import (
    bell_state,
    bra,
    braket,
    ket,
    ketbra,
    measurement_probability,
    multi_qubit_ket,
    post_measurement_state,
    projector,
)


class TestKet:
    def test_ket_0(self):
        np.testing.assert_array_equal(ket('0'), np.array([1, 0], dtype=complex))

    def test_ket_1(self):
        np.testing.assert_array_equal(ket('1'), np.array([0, 1], dtype=complex))

    def test_ket_plus(self):
        result = ket('+')
        expected = np.array([1, 1], dtype=complex) / np.sqrt(2)
        np.testing.assert_array_almost_equal(result, expected)

    def test_ket_minus(self):
        result = ket('-')
        expected = np.array([1, -1], dtype=complex) / np.sqrt(2)
        np.testing.assert_array_almost_equal(result, expected)

    def test_ket_i(self):
        result = ket('i')
        expected = np.array([1, 1j], dtype=complex) / np.sqrt(2)
        np.testing.assert_array_almost_equal(result, expected)


class TestBra:
    def test_bra_is_conjugate_transpose(self):
        k = ket('i')
        b = bra('i')
        np.testing.assert_array_almost_equal(b, np.conj(k))


class TestBraKet:
    def test_orthogonal(self):
        assert braket('0', '1') == pytest.approx(0.0)

    def test_normalized(self):
        assert braket('0', '0') == pytest.approx(1.0)

    def test_plus_zero(self):
        assert abs(braket('+', '0')) == pytest.approx(1 / np.sqrt(2))


class TestKetBra:
    def test_projector_shape(self):
        result = ketbra('0', '0')
        assert result.shape == (2, 2)

    def test_projector_idempotent(self):
        P = ketbra('0', '0')
        np.testing.assert_array_almost_equal(P @ P, P)


class TestProjector:
    def test_idempotent(self):
        P = projector('+')
        np.testing.assert_array_almost_equal(P @ P, P)

    def test_trace_one(self):
        P = projector('0')
        assert np.trace(P) == pytest.approx(1.0)


class TestMeasurement:
    def test_certain_outcome(self):
        assert measurement_probability(ket('0'), '0') == pytest.approx(1.0)

    def test_impossible_outcome(self):
        assert measurement_probability(ket('0'), '1') == pytest.approx(0.0)

    def test_equal_superposition(self):
        assert measurement_probability(ket('+'), '0') == pytest.approx(0.5)
        assert measurement_probability(ket('+'), '1') == pytest.approx(0.5)

    def test_probabilities_sum_to_one(self):
        state = np.array([0.6, 0.8j], dtype=complex)
        p0 = measurement_probability(state, '0')
        p1 = measurement_probability(state, '1')
        assert p0 + p1 == pytest.approx(1.0)


class TestPostMeasurement:
    def test_collapse_to_zero(self):
        result = post_measurement_state(ket('+'), '0')
        np.testing.assert_array_almost_equal(result, ket('0'))

    def test_collapse_to_one(self):
        result = post_measurement_state(ket('+'), '1')
        np.testing.assert_array_almost_equal(result, ket('1'))

    def test_impossible_raises(self):
        with pytest.raises(ValueError):
            post_measurement_state(ket('0'), '1')


class TestMultiQubitKet:
    def test_00(self):
        result = multi_qubit_ket('00')
        expected = np.array([1, 0, 0, 0], dtype=complex)
        np.testing.assert_array_equal(result, expected)

    def test_01(self):
        result = multi_qubit_ket('01')
        expected = np.array([0, 1, 0, 0], dtype=complex)
        np.testing.assert_array_equal(result, expected)

    def test_11(self):
        result = multi_qubit_ket('11')
        expected = np.array([0, 0, 0, 1], dtype=complex)
        np.testing.assert_array_equal(result, expected)

    def test_three_qubits(self):
        result = multi_qubit_ket('101')
        assert len(result) == 8
        assert result[5] == pytest.approx(1.0)  # |101> = index 5


class TestBellStates:
    def test_phi_plus(self):
        state = bell_state('phi+')
        expected = (multi_qubit_ket('00') + multi_qubit_ket('11')) / np.sqrt(2)
        np.testing.assert_array_almost_equal(state, expected)

    def test_psi_minus(self):
        state = bell_state('psi-')
        expected = (multi_qubit_ket('01') - multi_qubit_ket('10')) / np.sqrt(2)
        np.testing.assert_array_almost_equal(state, expected)

    def test_bell_states_normalized(self):
        for name in ['phi+', 'phi-', 'psi+', 'psi-']:
            state = bell_state(name)
            assert np.linalg.norm(state) == pytest.approx(1.0)

    def test_bell_states_orthogonal(self):
        states = [bell_state(n) for n in ['phi+', 'phi-', 'psi+', 'psi-']]
        for i in range(4):
            for j in range(4):
                overlap = np.abs(np.vdot(states[i], states[j]))
                if i == j:
                    assert overlap == pytest.approx(1.0)
                else:
                    assert overlap == pytest.approx(0.0, abs=1e-10)
