from app.wastewater_treatment.parameters import terminal_settling_velocity, ureg
from app.units import DEFAULT_DENSITY_UNIT
import pytest


def test_terminal_settling_velocity_example_7_1():
    """
    Test the terminal_settling_velocity function against Example 7.1
    from the textbook "Fundamentals of Wastewater Treatment and Engineering".
    """

    # --- Given Data (from Example 7.1) ---
    particle_diameter = 0.6 * ureg.mm  # Particle diameter
    particle_density = 2.65 * ureg.gram / ureg.centimeter ** 3  # Specific gravity of 2.65
    water_density = 997 * ureg.kg / ureg.meter ** 3  # Water density at 25°C
    water_viscosity = 0.89e-3 * ureg.pascal * ureg.second  # Water dynamic viscosity at 25°C
    gravity = 9.81 * ureg.meter / ureg.second ** 2
    expected_velocity = 0.114 * ureg.meter / ureg.second  # Expected result from the book

    # --- Call the function ---
    calculated_velocity = terminal_settling_velocity(
        particle_diameter=particle_diameter,
        particle_density=particle_density,
        water_density=water_density,
        gravity=gravity,
        water_dyn_viscosity=water_viscosity,
    )

    # --- Assertions (check against expected results) ---

    # Use pytest.approx for floating-point comparisons with tolerance
    assert calculated_velocity.to(ureg.m / ureg.s).magnitude == pytest.approx(
        expected_velocity.to(ureg.m / ureg.s).magnitude, rel=1e-2)  # 1% relative tolerance


def test_terminal_settling_velocity_invalid_input():
    """Test cases for invalid input (ValueError and TypeError)."""

    # Invalid particle_diameter (negative)
    with pytest.raises(ValueError):
        terminal_settling_velocity(particle_diameter=-0.0006*ureg.meter,
                                   particle_density=2650 * DEFAULT_DENSITY_UNIT)

    # Invalid particle_density (zero)
    with pytest.raises(ValueError):
        terminal_settling_velocity(particle_diameter=0.0006*ureg.meter, particle_density=0*DEFAULT_DENSITY_UNIT)

    # Invalid water_density (negative)
    with pytest.raises(ValueError):
        terminal_settling_velocity(
            particle_diameter=0.0006*ureg.meter, particle_density=2650*DEFAULT_DENSITY_UNIT, water_density=-997*DEFAULT_DENSITY_UNIT
        )

    # Invalid particle_density < water_density
    with pytest.raises(ValueError):
        terminal_settling_velocity(
            particle_diameter=0.0006 * ureg.m,
            particle_density=900 * DEFAULT_DENSITY_UNIT,
            water_density=997 * DEFAULT_DENSITY_UNIT
        )

    # Invalid type (string for particle_diameter)
    with pytest.raises(TypeError):
        terminal_settling_velocity(particle_diameter="0.0006", particle_density=2650*DEFAULT_DENSITY_UNIT)


def test_terminal_settling_velocity_stokes_flow():
    """Test cases for stokes flow."""
    calculated_velocity = terminal_settling_velocity(
        particle_diameter=0.0001 * ureg.m,  # Small diameter for Stokes flow
        particle_density=1500 * ureg.kg / ureg.m ** 3,
        water_density=997 * ureg.kg / ureg.m ** 3,
        water_dyn_viscosity=0.001 * ureg.pascal * ureg.second,
    )

    # Expected Stokes velocity (calculated manually)
    expected_velocity = ((9.81 * ureg.m / ureg.s ** 2) * (
                1500 * ureg.kg / ureg.m ** 3 - 997 * ureg.kg / ureg.m ** 3) * (0.0001 * ureg.m) ** 2) / (
                                    18 * 0.001 * ureg.pascal * ureg.second)
    assert calculated_velocity.to(ureg.m / ureg.s).magnitude == pytest.approx(
        expected_velocity.to(ureg.m / ureg.s).magnitude, rel=1e-2)


def test_terminal_settling_velocity_no_convergence():
    """Test the case where the iterative method does not converge."""
    with pytest.raises(ValueError, match="Settling velocity calculation did not converge"):
        terminal_settling_velocity(
            particle_diameter=0.01 * ureg.meter,  # Unrealistic, large diameter
            particle_density=1000 * ureg.kg / ureg.m ** 3,
            max_iterations=3,  # Force non-convergence with low max_iterations
        )

