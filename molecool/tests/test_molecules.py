"""
This module contains the test functions for the molecules module
"""
import molecool
import numpy as np

def test_compute_molecular_mass():
    symbols = ["C", "H", "H", "H", "H"] #Methane
    calculated_mm = molecool.molecules.compute_molecular_mass(symbols)
    expected_mm = 16.04 #g/mol
    assert np.isclose(calculated_mm, expected_mm, rtol=1e-2), "Expected and calculated molecular masses not equal!"