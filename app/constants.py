import pint
from typing import Union
from app.helpers import closest_key_binary_search
from app.units import ureg

# --- Physical Constants ---
STANDARD_GRAVITY = 9.80665 * ureg.meter / ureg.second ** 2
STANDARD_ATMOSPHERIC_PRESSURE = 101325 * ureg.pascal
PI = 3.141592653589793

WATER_SURFACE_TENSION = {
    20: 0.0728 * ureg.newton / ureg.meter,  # Surface tension at 20°C

}

# --- Typical Wastewater Characteristics (Ranges - for defaults) ---
#  These should be *ranges* or *typical values*, NOT single constants.
#  Users should ALWAYS be able to override these.
TYPICAL_BOD_RANGE = (100, 300) * ureg.milligram / ureg.liter  # Range for influent BOD
TYPICAL_TSS_RANGE = (100, 350) * ureg.milligram / ureg.liter  # Range for influent TSS
TYPICAL_TKN_RANGE = (20, 85) * ureg.milligram / ureg.liter  # Total Kjeldahl Nitrogen
TYPICAL_TP_RANGE = (4, 15) * ureg.milligram / ureg.liter  # Total Phosphorus
TYPICAL_PH_RANGE = (6.5, 8.5) * ureg.dimensionless  # pH range

# --- Common Conversion Factors (within pint, you don't *usually* need these, but they're handy) ---
# These are better handled directly by pint's conversion capabilities.
#  But, if you *really* want them:
MGD_TO_CUBIC_METERS_PER_DAY = 3785.411784  # 1 MGD = 3785.41 m³/day (no pint units here, just conversion factor)

# --- Design Parameters (Typical Ranges) ---
PRIMARY_CLARIFIER_OVERFLOW_RATE_RANGE = (24, 60) * ureg.meter ** 3 / (ureg.meter ** 2 * ureg.day)  # Typical range
PRIMARY_CLARIFIER_DETENTION_TIME_RANGE = (1.5, 2.5) * ureg.hour
PRIMARY_CLARIFIER_SLR = (10, 40) * ureg.kg / (ureg.meter ** 2 * ureg.day)
PRIMARY_CLARIFIER_WLR = (125, 500) * ureg.meter ** 3 / (ureg.meter * ureg.day)
ACTIVATED_SLUDGE_F_M_RATIO_RANGE = (0.2, 0.6) * ureg.day ** -1  # Food/Microorganism ratio
ACTIVATED_SLUDGE_MLSS_RANGE = (1500, 5000) * ureg.milligram / ureg.liter  # Mixed Liquor Suspended Solids
ACTIVATED_SLUDGE_SRT_RANGE = (3, 15) * ureg.day  # Solids Retention Time (Sludge Age)
SECONDARY_CLARIFIER_OVERFLOW_RATE_RANGE = (16, 40) * ureg.meter ** 3 / (ureg.meter ** 2 * ureg.day)
SECONDARY_CLARIFIER_SLR_RANGE = (50, 200) * ureg.kg / (ureg.meter ** 2 * ureg.day)

# --- Other Constants ---
IDEAL_GAS_CONSTANT = 8.314 * ureg.joule / (ureg.mole * ureg.kelvin)


# Constants (using _ for internal use, as these shouldn't be changed outside this module)
_drag_coefficient = 0.5  # Placeholder value
_particle_diameter = 0.003 * ureg.meter
_particle_density = 1.045 * ureg.gram / ureg.centimeter ** 3
_water_density = 0.9982 * ureg.gram / ureg.centimeter ** 3
_gravity = 9.81 * ureg.meter / ureg.second ** 2

# Dynamic Viscosity of Water (approximate value at 20°C)
# 0.0010005 Pa*s = 0.0010005 N*s/m2
_water_dyn_viscosity = 1.0016 * ureg.mPa * ureg.s

_shape_factor = 1  # For perfect spheres


WATER_PROPERTIES = {
    "kinematic_viscosity": {
        1.6: 1.6735 * ureg.millimeter**2 / ureg.second,
        1.5: 1.7351 * ureg.millimeter**2 / ureg.second,
        4: 1.5673 * ureg.millimeter**2 / ureg.second,
        5: 1.5182 * ureg.millimeter**2 / ureg.second,
        6: 1.4715 * ureg.millimeter**2 / ureg.second,
        7: 1.4271 * ureg.millimeter**2 / ureg.second,
        8: 1.3847 * ureg.millimeter**2 / ureg.second,
        9: 1.3444 * ureg.millimeter**2 / ureg.second,
        10: 1.3059 * ureg.millimeter**2 / ureg.second,
        11: 1.2692 * ureg.millimeter**2 / ureg.second,
        12: 1.2341 * ureg.millimeter**2 / ureg.second,
        13: 1.2005 * ureg.millimeter**2 / ureg.second,
        14: 1.1683 * ureg.millimeter**2 / ureg.second,
        15: 1.1375 * ureg.millimeter**2 / ureg.second,
        16: 1.1081 * ureg.millimeter**2 / ureg.second,
        17: 1.0798 * ureg.millimeter**2 / ureg.second,
        18: 1.0526 * ureg.millimeter**2 / ureg.second,
        19: 1.0266 * ureg.millimeter**2 / ureg.second,
        20: 1.0034 * ureg.millimeter**2 / ureg.second,
        21: 0.9795 * ureg.millimeter**2 / ureg.second,
        22: 0.9565 * ureg.millimeter**2 / ureg.second,
        23: 0.9344 * ureg.millimeter**2 / ureg.second,
        24: 0.9131 * ureg.millimeter**2 / ureg.second,
        25: 0.8926 * ureg.millimeter**2 / ureg.second,
        26: 0.8729 * ureg.millimeter**2 / ureg.second,
        27: 0.8539 * ureg.millimeter**2 / ureg.second,
        28: 0.8355 * ureg.millimeter**2 / ureg.second,
        29: 0.8178 * ureg.millimeter**2 / ureg.second,
        30: 0.8007 * ureg.millimeter**2 / ureg.second,
        31: 0.7842 * ureg.millimeter**2 / ureg.second,
        32: 0.7682 * ureg.millimeter**2 / ureg.second,
        33: 0.7528 * ureg.millimeter**2 / ureg.second,
        34: 0.7379 * ureg.millimeter**2 / ureg.second,
        35: 0.7234 * ureg.millimeter**2 / ureg.second,
        36: 0.7095 * ureg.millimeter**2 / ureg.second,
        37: 0.6959 * ureg.millimeter**2 / ureg.second,
        38: 0.6828 * ureg.millimeter**2 / ureg.second,
        39: 0.6702 * ureg.millimeter**2 / ureg.second,
        40: 0.6579 * ureg.millimeter**2 / ureg.second,
        45: 0.5958 * ureg.millimeter**2 / ureg.second,
        50: 0.5531 * ureg.millimeter**2 / ureg.second,
        55: 0.5109 * ureg.millimeter**2 / ureg.second,
        60: 0.4740 * ureg.millimeter**2 / ureg.second,
        65: 0.4329 * ureg.millimeter**2 / ureg.second,
        70: 0.4127 * ureg.millimeter**2 / ureg.second,
        75: 0.3872 * ureg.millimeter**2 / ureg.second,
        80: 0.3643 * ureg.millimeter**2 / ureg.second,
    },
    "dynamic_viscosity": {
        1.6: 1.6736 * ureg.mPa * ureg.s,
        1.5: 1.7351 * ureg.mPa * ureg.s,
        4: 1.5674 * ureg.mPa * ureg.s,
        5: 1.5182 * ureg.mPa * ureg.s,
        6: 1.4716 * ureg.mPa * ureg.s,
        7: 1.4272 * ureg.mPa * ureg.s,
        8: 1.3849 * ureg.mPa * ureg.s,
        9: 1.3447 * ureg.mPa * ureg.s,
        10: 1.3063 * ureg.mPa * ureg.s,
        11: 1.2696 * ureg.mPa * ureg.s,
        12: 1.2347 * ureg.mPa * ureg.s,
        13: 1.2012 * ureg.mPa * ureg.s,
        14: 1.1692 * ureg.mPa * ureg.s,
        15: 1.1386 * ureg.mPa * ureg.s,
        16: 1.1092 * ureg.mPa * ureg.s,
        17: 1.0811 * ureg.mPa * ureg.s,
        18: 1.0541 * ureg.mPa * ureg.s,
        19: 1.0282 * ureg.mPa * ureg.s,
        20: 1.0016 * ureg.mPa * ureg.s,
        21: 0.9775 * ureg.mPa * ureg.s,
        22: 0.9544 * ureg.mPa * ureg.s,
        23: 0.9321 * ureg.mPa * ureg.s,
        24: 0.9107 * ureg.mPa * ureg.s,
        25: 0.8900 * ureg.mPa * ureg.s,
        26: 0.8701 * ureg.mPa * ureg.s,
        27: 0.8509 * ureg.mPa * ureg.s,
        28: 0.8324 * ureg.mPa * ureg.s,
        29: 0.8145 * ureg.mPa * ureg.s,
        30: 0.7972 * ureg.mPa * ureg.s,
        31: 0.7805 * ureg.mPa * ureg.s,
        32: 0.7644 * ureg.mPa * ureg.s,
        33: 0.7488 * ureg.mPa * ureg.s,
        34: 0.7337 * ureg.mPa * ureg.s,
        35: 0.7191 * ureg.mPa * ureg.s,
        36: 0.7050 * ureg.mPa * ureg.s,
        37: 0.6913 * ureg.mPa * ureg.s,
        38: 0.6780 * ureg.mPa * ureg.s,
        39: 0.6652 * ureg.mPa * ureg.s,
        40: 0.6527 * ureg.mPa * ureg.s,
        45: 0.5958 * ureg.mPa * ureg.s,
        50: 0.5465 * ureg.mPa * ureg.s,
        55: 0.5036 * ureg.mPa * ureg.s,
        60: 0.4660 * ureg.mPa * ureg.s,
        65: 0.4329 * ureg.mPa * ureg.s,
        70: 0.4035 * ureg.mPa * ureg.s,
        75: 0.3774 * ureg.mPa * ureg.s,
        80: 0.3540 * ureg.mPa * ureg.s,
    },
    "density": {
        1.6: 0.99993 * ureg.gram / ureg.centimeter ** 3,
        1.5: 0.99993 * ureg.gram / ureg.centimeter ** 3,
        4: 0.99997 * ureg.gram / ureg.centimeter ** 3,
        5: 0.99997 * ureg.gram / ureg.centimeter ** 3,
        6: 0.99997 * ureg.gram / ureg.centimeter ** 3,
        7: 0.99998 * ureg.gram / ureg.centimeter ** 3,
        8: 0.99999 * ureg.gram / ureg.centimeter ** 3,
        9: 0.9998 * ureg.gram / ureg.centimeter ** 3,
        10: 0.9997 * ureg.gram / ureg.centimeter ** 3,
        11: 0.9996 * ureg.gram / ureg.centimeter ** 3,
        12: 0.9995 * ureg.gram / ureg.centimeter ** 3,
        13: 0.9994 * ureg.gram / ureg.centimeter ** 3,
        14: 0.9992 * ureg.gram / ureg.centimeter ** 3,
        15: 0.9991 * ureg.gram / ureg.centimeter ** 3,
        16: 0.9989 * ureg.gram / ureg.centimeter ** 3,
        17: 0.9988 * ureg.gram / ureg.centimeter ** 3,
        18: 0.9986 * ureg.gram / ureg.centimeter ** 3,
        19: 0.9984 * ureg.gram / ureg.centimeter ** 3,
        20: 0.9982 * ureg.gram / ureg.centimeter ** 3,
        21: 0.998 * ureg.gram / ureg.centimeter ** 3,
        22: 0.9978 * ureg.gram / ureg.centimeter ** 3,
        23: 0.9975 * ureg.gram / ureg.centimeter ** 3,
        24: 0.9973 * ureg.gram / ureg.centimeter ** 3,
        25: 0.997 * ureg.gram / ureg.centimeter ** 3,
        26: 0.9968 * ureg.gram / ureg.centimeter ** 3,
        27: 0.9965 * ureg.gram / ureg.centimeter ** 3,
        28: 0.9962 * ureg.gram / ureg.centimeter ** 3,
        29: 0.9959 * ureg.gram / ureg.centimeter ** 3,
        30: 0.9956 * ureg.gram / ureg.centimeter ** 3,
        31: 0.9953 * ureg.gram / ureg.centimeter ** 3,
        32: 0.995 * ureg.gram / ureg.centimeter ** 3,
        33: 0.9947 * ureg.gram / ureg.centimeter ** 3,
        34: 0.9944 * ureg.gram / ureg.centimeter ** 3,
        35: 0.994 * ureg.gram / ureg.centimeter ** 3,
        36: 0.9937 * ureg.gram / ureg.centimeter ** 3,
        37: 0.9933 * ureg.gram / ureg.centimeter ** 3,
        38: 0.993 * ureg.gram / ureg.centimeter ** 3,
        39: 0.9926 * ureg.gram / ureg.centimeter ** 3,
        40: 0.9922 * ureg.gram / ureg.centimeter ** 3,
        45: 0.9902 * ureg.gram / ureg.centimeter ** 3,
        50: 0.988 * ureg.gram / ureg.centimeter ** 3,
        55: 0.9857 * ureg.gram / ureg.centimeter ** 3,
        60: 0.9832 * ureg.gram / ureg.centimeter ** 3,
        65: 0.9806 * ureg.gram / ureg.centimeter ** 3,
        70: 0.9778 * ureg.gram / ureg.centimeter ** 3,
        75: 0.9748 * ureg.gram / ureg.centimeter ** 3,
        80: 0.9718 * ureg.gram / ureg.centimeter ** 3,
    }
}


def get_water_density(temperature: Union[int, float, pint.Quantity]) -> pint.Quantity:
    """Gets the density of water at a given temperature.
        Temperature must be in Celsius. The result is in g/cm^3
    Args:
        temperature: The temperature (in Celsius if a float, or with units).

    Returns:
        The density of water.  Returns a default value if temperature is out of range.
    """
    if isinstance(temperature, pint.Quantity):
        temperature = temperature.to(ureg.degC).magnitude

    if 1.6 <= temperature <= 80:  # Use most precise value in the look up table
        # Find the closest temperature in the dictionary
        closest_temp = closest_key_binary_search(WATER_PROPERTIES["density"], temperature)
        return WATER_PROPERTIES["density"][closest_temp]
    else:
        # Return default density for 20 °C
        return 0.9982 * ureg.gram / ureg.centimeter ** 3


def get_water_dynamic_viscosity(temperature: Union[int, float, pint.Quantity]) -> pint.Quantity:
    """
    Gets the dynamic viscosity of water at a given temperature.
        Temperature must be in Celsius. The result is in mPa.s
    Args:
        temperature: The temperature (in Celsius if a float, or with units).

    Returns:
        The dynamic viscosity of water.  Returns a default value if temperature is out of range.
    """

    if isinstance(temperature, pint.Quantity):
        temperature = temperature.to(ureg.degC).magnitude

    if 1.6 <= temperature <= 80:  # Use most precise value in the look-up table
        # Find the closest temperature in the dictionary
        closest_temp = closest_key_binary_search(WATER_PROPERTIES["dynamic_viscosity"], temperature)
        return WATER_PROPERTIES["dynamic_viscosity"][closest_temp]
    else:
        # Return default density for 20 °C
        return 1.0016 * ureg.mPa * ureg.s


def get_water_kinematic_viscosity(temperature: Union[int, float, pint.Quantity]) -> pint.Quantity:
    """
    Gets the kinematic viscosity of water at a given temperature.
        Temperature must be in Celsius. The result is in mm^2/s
    Args:
        temperature: The temperature (in Celsius if a float, or with units).

    Returns:
        The kinematic viscosity of water.  Returns a default value if temperature is out of range.
    """
    if isinstance(temperature, pint.Quantity):
        temperature = temperature.to(ureg.degC).magnitude

    if 1.6 <= temperature <= 80:  # Use most precise value in the look up table
        # Find the closest temperature in the dictionary
        closest_temp = closest_key_binary_search(WATER_PROPERTIES["kinematic_viscosity"], temperature)
        return WATER_PROPERTIES["kinematic_viscosity"][closest_temp]
    else:
        # Return default density for 20 °C
        return 1.0034 * ureg.millimeter**2 / ureg.second
