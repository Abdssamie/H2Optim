import logging

import pint
from typing import Union, Optional
from app.constants import (get_water_dynamic_viscosity,
                           get_water_density,
                           _gravity,
                           )

from app.units import (
    DEFAULT_TEMPERATURE_UNIT,
    ureg
)



def terminal_settling_velocity(
        particle_diameter: pint.Quantity,
        particle_density: pint.Quantity,
        water_density: Optional[pint.Quantity] = None,  # Optional now
        gravity: pint.Quantity = _gravity,
        water_dyn_viscosity: Optional[pint.Quantity] = None,  # Optional now
        temperature: Union[float, pint.Quantity] = 20,
        drag_coefficient: Optional[float] = None,  # Optional, will be calculated
        shape_factor: float = 1.0,
        tolerance: float = 0.001,  # Add tolerance for convergence
        max_iterations: int = 100,  # Add max iterations
) -> pint.Quantity:
    """Calculates the terminal settling velocity of a particle.

    Args:
        particle_diameter: Particle diameter.
        particle_density: Particle density.
        water_density:  Water density. Defaults to density at 20°C.
        gravity: Acceleration due to gravity. Defaults to standard gravity.
        water_dyn_viscosity: Dynamic viscosity of water. Defaults to viscosity at 20°C.
        temperature: Temperature to get the corresponding viscosity and density.
                     Defaults to 20°C.  Used only if water_density/viscosity are None.
        drag_coefficient: Initial guess for drag coefficient (dimensionless).  If None,
                         it will be calculated iteratively.
        shape_factor: Shape factor of the particle (dimensionless). Defaults to 1
            (perfectly spherical).
        tolerance: Relative tolerance for convergence.
        max_iterations: Maximum number of iterations.

    Returns:
        Terminal settling velocity.

    Raises:
        TypeError: If inputs are not of the correct type.
        ValueError: If physically impossible values are provided or no convergence.
    """

    # --- Input Type Validation (Simplified) ---
    if not isinstance(particle_diameter, pint.Quantity):
        raise TypeError("particle_diameter must be a pint.Quantity")
    if not isinstance(particle_density, pint.Quantity):
        raise TypeError("particle_density must be a pint.Quantity")
    if not isinstance(temperature, (int, float, pint.Quantity)):  # Temp can be a float
        raise TypeError("temperature must be a number or a pint.Quantity")
    if not isinstance(shape_factor, (int, float)):
        raise TypeError("shape_factor must be a number.")
    if not isinstance(tolerance, (int, float)):
        raise TypeError("tolerance must be a number")
    if not isinstance(max_iterations, int):
        raise TypeError("max_iterations must be an integer.")

    # Handle temperature (make sure it's a quantity)
    if isinstance(temperature, (int, float)):
        temperature = ureg.Quantity(temperature, DEFAULT_TEMPERATURE_UNIT)

    # ---  Provide default values or calculate if necessary ---
    # Use provided values or get from temperature.
    if water_density is None:
        water_density = get_water_density(temperature)
    if water_dyn_viscosity is None:
        water_dyn_viscosity = get_water_dynamic_viscosity(temperature)

    # --- Input Value Validation ---
    if particle_diameter.magnitude <= 0:
        raise ValueError("particle_diameter must be greater than zero")
    if particle_density.magnitude <= 0:
        raise ValueError("particle_density must be greater than zero")
    if water_density.magnitude <= 0:
        raise ValueError("water_density must be greater than zero")
    if gravity.magnitude <= 0:
        raise ValueError("gravity must be greater than zero")
    if water_dyn_viscosity.magnitude <= 0:
        raise ValueError("water_dyn_viscosity must be greater than zero")
    if particle_density <= water_density:
        raise ValueError("Particle density must be greater than water density for settling.")
    if drag_coefficient is not None and drag_coefficient <= 0:
        raise ValueError("Drag Coefficient must be positive")
    if max_iterations <= 0:
        raise ValueError("Max iteration must be greater than zero")
    if not 0 < tolerance < 1:
        raise ValueError("Tolerance must be between 0 and 1")
    # --- Iterative Calculation ---

    # 1. Initial Guess (Stokes' Law)
    v_stokes = (
            (gravity * (particle_density - water_density) * (particle_diameter ** 2))
            / (18 * water_dyn_viscosity)
    )
    v_t = v_stokes  # Initial guess

    # 2. Iteration Loop
    for _ in range(max_iterations):
        reynolds_number = find_reynolds_number(
            v_t, particle_diameter, water_dyn_viscosity, water_density, shape_factor
        )

        # Calculate drag coefficient based on Reynolds number
        if reynolds_number < 1:
            v_t_new = v_stokes  # Keep stokes velocity
            return v_t_new.to(ureg.m / ureg.s)
        elif 1 <= reynolds_number <= 10 ** 3:
            drag_coefficient = 24 / reynolds_number + 3 / reynolds_number ** 0.5 + 0.34
        else:
            drag_coefficient = 0.4

        # Calculate new settling velocity
        v_t_new = (
                          (4 * gravity * particle_diameter * (particle_density - water_density))
                          / (3 * drag_coefficient * water_density)
                  ) ** 0.5

        # Check for convergence
        relative_difference = abs(v_t_new - v_t) / abs(v_t)  # Avoid division by zero
        if relative_difference < tolerance:
            logging.debug(f"Terminal velocity: {v_t_new.to(ureg.m / ureg.s)}")
            return v_t_new.to(ureg.m / ureg.s)

        v_t = v_t_new  # Update vt for the next iteration

    # If max_iterations reached without convergence, raise an error
    raise ValueError(
        f"Settling velocity calculation did not converge within {max_iterations} iterations."
    )


def find_reynolds_number(velocity: pint.Quantity,
                         particle_diameter: pint.Quantity,
                         water_dyn_viscosity: pint.Quantity,
                         water_density: pint.Quantity,
                         shape_factor: Union[int, pint.Quantity] = 1):
    """
    Calculates the Reynolds number for a particle settling in water.

    Args:
        velocity : pint.Quantity. The velocity of the particle.
        particle_diameter : pint.Quantity. The diameter of the particle.
        water_dyn_viscosity : pint.Quantity. The dynamic viscosity of water.
        water_density : pint.Quantity. The density of water.
        shape_factor : The shape factor of the particle. Defaults to 1.

    Returns
        pint.Quantity: The Reynolds number of the particle.
    """
    return velocity * shape_factor * water_density * particle_diameter / water_dyn_viscosity
