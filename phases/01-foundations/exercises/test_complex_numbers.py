"""Tests for complex number exercises."""

import numpy as np
import pytest

from complex_numbers import (
    complex_conjugate,
    complex_multiply_polar,
    euler_formula_verify,
    from_polar,
    modulus,
    nth_roots_of_unity,
    to_polar,
)


class TestComplexConjugate:
    def test_real_number(self):
        assert complex_conjugate(3 + 0j) == 3 + 0j

    def test_imaginary_number(self):
        assert complex_conjugate(2 + 3j) == 2 - 3j

    def test_negative_imaginary(self):
        assert complex_conjugate(1 - 4j) == 1 + 4j

    def test_pure_imaginary(self):
        assert complex_conjugate(5j) == -5j

    def test_zero(self):
        assert complex_conjugate(0j) == 0j


class TestModulus:
    def test_real(self):
        assert modulus(3 + 0j) == pytest.approx(3.0)

    def test_unit_complex(self):
        assert modulus(3 + 4j) == pytest.approx(5.0)

    def test_pure_imaginary(self):
        assert modulus(5j) == pytest.approx(5.0)

    def test_unit_circle(self):
        z = np.exp(1j * np.pi / 4)
        assert modulus(z) == pytest.approx(1.0)


class TestPolarConversion:
    def test_to_polar_positive_real(self):
        r, theta = to_polar(1 + 0j)
        assert r == pytest.approx(1.0)
        assert theta == pytest.approx(0.0)

    def test_to_polar_pure_imaginary(self):
        r, theta = to_polar(1j)
        assert r == pytest.approx(1.0)
        assert theta == pytest.approx(np.pi / 2)

    def test_to_polar_negative_real(self):
        r, theta = to_polar(-1 + 0j)
        assert r == pytest.approx(1.0)
        assert abs(theta) == pytest.approx(np.pi)

    def test_roundtrip(self):
        z = 3 + 4j
        r, theta = to_polar(z)
        z_back = from_polar(r, theta)
        assert z_back.real == pytest.approx(z.real)
        assert z_back.imag == pytest.approx(z.imag)

    def test_from_polar_unit_circle(self):
        z = from_polar(1.0, np.pi / 3)
        assert z.real == pytest.approx(np.cos(np.pi / 3))
        assert z.imag == pytest.approx(np.sin(np.pi / 3))


class TestComplexMultiplyPolar:
    def test_multiply_real(self):
        result = complex_multiply_polar(2 + 0j, 3 + 0j)
        assert result.real == pytest.approx(6.0)
        assert result.imag == pytest.approx(0.0, abs=1e-10)

    def test_multiply_imaginary(self):
        result = complex_multiply_polar(1j, 1j)
        assert result.real == pytest.approx(-1.0)
        assert result.imag == pytest.approx(0.0, abs=1e-10)

    def test_multiply_general(self):
        z1, z2 = 1 + 1j, 1 - 1j
        result = complex_multiply_polar(z1, z2)
        expected = z1 * z2
        assert result.real == pytest.approx(expected.real)
        assert result.imag == pytest.approx(expected.imag, abs=1e-10)


class TestNthRootsOfUnity:
    def test_square_roots(self):
        roots = nth_roots_of_unity(2)
        assert len(roots) == 2
        assert roots[0].real == pytest.approx(1.0)
        assert roots[1].real == pytest.approx(-1.0)

    def test_fourth_roots(self):
        roots = nth_roots_of_unity(4)
        assert len(roots) == 4
        for root in roots:
            assert modulus(root) == pytest.approx(1.0)
            assert root**4 == pytest.approx(1.0, abs=1e-10)

    def test_roots_sum_to_zero(self):
        for n in [3, 5, 7]:
            roots = nth_roots_of_unity(n)
            total = sum(roots)
            assert total.real == pytest.approx(0.0, abs=1e-10)
            assert total.imag == pytest.approx(0.0, abs=1e-10)


class TestEulerFormula:
    def test_zero(self):
        assert euler_formula_verify(0.0)

    def test_pi(self):
        assert euler_formula_verify(np.pi)

    def test_pi_over_2(self):
        assert euler_formula_verify(np.pi / 2)

    def test_arbitrary(self):
        assert euler_formula_verify(1.234)
