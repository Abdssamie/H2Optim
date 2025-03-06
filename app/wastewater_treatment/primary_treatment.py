import pint
from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Literal, Union, Optional
from app.units import ureg
import math


# Consult the pdf about water treatment in the docs folder for more info about
# sedimantation tanks design parameters

# The following assumptions are made:
# 1. There is no settling of particles in the inlet and outlet zones.
# 2. Particles settle in the sludge zone and are not resuspended.
# 3. Plug flow conditions exist.


class SedimentationTank(BaseModel):
    """Represents a sedimentation tank (clarifier)."""

    flow_rate: pint.Quantity = Field(..., gt=0)
    peaking_factor: pint.Quantity = Field(..., gt=0)
    influent_tss: pint.Quantity = Field(..., gt=0)
    influent_bod: pint.Quantity = Field(..., gt=0)
    surface_overflow_velocity: pint.Quantity = Field(..., gt=0)
    # The rate vo at which the particles settle in the tank is equal to the rate at
    # which clarified water flows out from the tank.
    # This rate is a design parameter and is called the surface overflow rate.
    tank_type: Literal["circular", "rectangular"] = Field(default="rectangular")
    detention_time: pint.Quantity = Field(..., gt=0)
    weir_length: pint.Quantity = Field(..., gt=0)
    weir_loading_rate: pint.Quantity = Field(..., gt=0)
    # The weir loading rate:
    # is the effluent flow rate over the weir divided by the weir length.

    # # To add average flow rate and peak flow rate design parameters
    # # This encompasses the use of equalization which is not yet implemented
    # average_flow_rate: pint.Quantity = Field(..., gt=0)
    # peak_flow_rate: pint.Quantity = Field(..., gt=0)
    # # Flow equalization is a method of damping the variations in flow rates,
    # # so that the unit processes receive nearly constant flow rates (Metcalf and
    # # Eddy, 2003).
    length_to_width_ratio: float = Field(4.0, gt=0)  # For rectangular tanks, default 4:1
    side_water_depth: Optional[pint.Quantity] = Field(None, gt=0)

    # if on of these values are true we have to account for that and
    # modify the design parameters
    short_circuiting: bool = Field(default=False)
    inlet_turbulence: bool = Field(default=False)
    outlet_turbulence: bool = Field(default=False)

    length: Optional[pint.Quantity]
    width: Optional[pint.Quantity]
    height: Optional[pint.Quantity]
    diameter: Optional[pint.Quantity]
    depth: Optional[pint.Quantity]
    volume: Optional[pint.Quantity]
    surface_area: Optional[pint.Quantity]
    effluent_tss: Optional[pint.Quantity] = None
    effluent_bod: Optional[pint.Quantity] = None
    tss_removal_efficiency: Optional[pint.Quantity] = None
    bod_removal_efficiency: Optional[pint.Quantity] = None

    @field_validator("tank_type")
    def _check_tank_type(self, value):
        if value not in ("rectangular", "circular"):  # Not needed with Literal
            raise ValueError("Invalid tank type")
        return value

    def calculate_design(self):
        """Calculates the design parameters of the sedimentation tank."""

        # Ensure we have an over_flow_rate
        if self.surface_overflow_velocity is None:
            if self.detention_time is not None and self.side_water_depth is not None:
                self.surface_overflow_velocity = self.side_water_depth / self.detention_time
            else:  # No overflow rate, no detention time
                raise ValueError("Either overflow_rate or detention_time and side_water_depth must be provided.")
        # Calculate surface area
        self.surface_area = (self.flow_rate / self.surface_overflow_velocity).to("m^2")

        # Calculate dimensions based on tank type
        if self.tank_type == "rectangular":
            self.width = (self.surface_area / self.length_to_width_ratio) ** 0.5
            self.length = self.width * self.length_to_width_ratio
            self.diameter = None  # Clear diameter
        elif self.tank_type == "circular":
            self.diameter = (4 * self.surface_area / math.pi) ** 0.5
            self.length = None  # Clear length/width
            self.width = None

        # calculate volume
        if self.detention_time is None:
            if self.side_water_depth is not None:
                self.volume = self.surface_area * self.side_water_depth
                self.detention_time = (self.volume / self.flow_rate).to(ureg.hour)  # Calculate the detention time
            else:
                raise ValueError("Either side_water_depth or detention_time must be provided.")

        else:  # Detention time given
            self.volume = self.flow_rate * self.detention_time
            if self.side_water_depth is None:  # Calculate  side_water_depth
                self.side_water_depth = (self.volume / self.surface_area).to(ureg.meter)

        # Calculate effluent concentrations
        self.effluent_tss = self.influent_tss * (1 - self.tss_removal_efficiency)
        self.effluent_bod = self.influent_bod * (1 - self.bod_removal_efficiency)

        return self  

    class Config:
        arbitrary_types_allowed = True  # Allow pint.Quantity
