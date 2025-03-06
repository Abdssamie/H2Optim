import pytest
from app.constants import (get_water_density,
                           get_water_dynamic_viscosity,
                           get_water_kinematic_viscosity,
                           ureg)


def test_get_water_density_at_20c():
    """Test that get_water_density returns the correct density at 20°C."""
    density = get_water_density(20)
    assert density.magnitude == pytest.approx(0.9982, rel=1e-4)  # Use pytest.approx for floating-point comparison
    assert density.units == ureg.gram / ureg.centimeter ** 3


def test_get_water_density_with_quantity():
    """Test that get_water_density works correctly when given a pint.Quantity."""
    density = get_water_density(ureg.Quantity(20, ureg.degC))
    assert density.magnitude == pytest.approx(0.9982, rel=1e-4)
    assert density.units == ureg.gram / ureg.centimeter ** 3


def test_get_water_density_out_of_range():
    """Test that get_water_density returns a default value for out-of-range temperatures."""
    density = get_water_density(ureg.Quantity(100, ureg.degC))
    assert density.magnitude == pytest.approx(0.9982, rel=1e-4)  # Check against the 20°C default
    assert density.units == ureg.gram / ureg.centimeter ** 3


def test_get_water_density_invalid_input():
    """Test get_water_density raises TypeError for invalid input types"""
    with pytest.raises(TypeError):
        get_water_density("20")  # String not accepted
    with pytest.raises(TypeError):
        get_water_density([20])  # List not accepted.


def test_get_water_dynamic_viscosity_at_20C():
    """Test that get_water_dynamic_viscosity returns the correct viscosity at 20°C."""
    viscosity = get_water_dynamic_viscosity(ureg.Quantity(20, ureg.degC))
    assert viscosity.magnitude == pytest.approx(1.0016, rel=1e-4)
    assert viscosity.units == ureg.mPa * ureg.second


def test_get_water_dynamic_viscosity_with_quantity():
    """Test that get_water_dynamic_viscosity with quantity input."""
    viscosity = get_water_dynamic_viscosity(ureg.Quantity(20, ureg.degC))
    assert viscosity.magnitude == pytest.approx(1.0016, rel=1e-4)
    assert viscosity.units == ureg.mPa * ureg.second


def test_get_water_dynamic_viscosity_out_of_range():
    """Test that get_water_dynamic_viscosity returns a default value for out-of-range temperatures."""
    viscosity = get_water_dynamic_viscosity(100)
    assert viscosity.magnitude == pytest.approx(1.0016, rel=1e-4)  # Check against 20C default.
    assert viscosity.units == ureg.mPa * ureg.second


def test_get_water_dynamic_viscosity_invalid_input():
    """Test that get_water_dynamic_viscosity raise TypeError with invalid input"""
    with pytest.raises(TypeError):
        get_water_dynamic_viscosity("20")
    with pytest.raises(TypeError):
        get_water_dynamic_viscosity([20])


def test_get_water_kinematic_viscosity_at_20c():
    """Test that get_water_kinematic_viscosity returns the correct viscosity at 20°C."""
    viscosity = get_water_kinematic_viscosity(ureg.Quantity(20, ureg.degC))
    assert viscosity.magnitude == pytest.approx(1.0034, rel=1e-4)
    assert viscosity.units == ureg.millimeter**2 / ureg.second


def test_get_water_kinematic_viscosity_with_quantity():
    """Test that get_water_kinematic_viscosity with quantity as input."""
    viscosity = get_water_kinematic_viscosity(20)
    assert viscosity.magnitude == pytest.approx(1.0034, rel=1e-4)
    assert viscosity.units == ureg.millimeter**2 / ureg.second


def test_get_water_kinematic_viscosity_out_of_range():
    """Test that get_water_kinematic_viscosity returns a default value for out-of-range temperatures."""
    viscosity = get_water_kinematic_viscosity(100)
    assert viscosity.magnitude == pytest.approx(1.0034, rel=1e-4)  # Check against the 20°C default.
    assert viscosity.units == ureg.millimeter**2 / ureg.second


def test_get_water_kinematic_viscosity_invalid_input():
    """Test that get_water_kinematic_viscosity raises an error if given an invalid type input."""
    with pytest.raises(TypeError):
        get_water_kinematic_viscosity("20")  # String
    with pytest.raises(TypeError):
        get_water_kinematic_viscosity([20])  # List
