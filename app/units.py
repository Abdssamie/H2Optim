import pint

ureg = pint.UnitRegistry()


DEFAULT_LENGTH_UNIT = ureg.meter
DEFAULT_DENSITY_UNIT = ureg.kg / ureg.meter**3
DEFAULT_VISCOSITY_UNIT = ureg.mPa * ureg.s  # Use mPa.s
DEFAULT_GRAVITY_UNIT = ureg.meter / ureg.second**2
DEFAULT_TEMPERATURE_UNIT = ureg.degC
DEFAULT_DRAG_COEFFICIENT = ureg.dimensionless  # Unitless.
