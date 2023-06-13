"""
This module contains the test functions for the measure module
"""
import molecool
import pytest
import numpy as np
from molecool.measure import calculate_angle, calculate_distance

def test_calculate_distance():
    r1 = np.array([0,0,1.0])
    r2 = np.array([0,0,0])
    expected_distance = 1.0
    calculated_distance = molecool.measure.calculate_distance(r1,r2)
    assert calculated_distance == expected_distance, "Distance for test case should be 1"

@pytest.mark.parametrize(
    "p1, p2, expected_distance",
    [
    (np.array([0,0,0]), np.array([0,0,1]), 1),
    (np.array([0,0,0]), np.array([0,0,5]), 5),
    (np.array([0,0,0]), np.array([0,0,20]), 20)
    ])

def test_calculate_distance_many(p1,p2,expected_distance):
    calculated_distance = molecool.measure.calculate_distance(p1,p2)
    assert np.isclose(calculated_distance,expected_distance, rtol=1e-2)