"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .RotatingMachineDynamics import RotatingMachineDynamics


@dataclass(config=DataclassConfig)
class AsynchronousMachineDynamics(RotatingMachineDynamics, ModuleType):
    """
    Asynchronous machine whose behaviour is described by reference to a standard model expressed in either time constant
      reactance form or equivalent circuit form or by definition of a user-defined model. Parameter details:
      Asynchronous machine parameters such as Xl, Xs, etc. are actually used as inductances in the model, but are
      commonly referred to as reactances since, at nominal frequency, the PU values are the same. However, some
      references use the symbol L instead of X.

    AsynchronousMachine: Asynchronous machine to which this asynchronous machine dynamics model applies.
    TurbineGovernorDynamics: Turbine-governor model associated with this asynchronous machine model.
    MechanicalLoadDynamics: Mechanical load model associated with this asynchronous machine model.
    WindTurbineType1or2Dynamics: Wind generator type 1 or type 2 model associated with this asynchronous machine model.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return AsynchronousMachineDynamics(*args, **kwargs)

    AsynchronousMachine: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.DY,
        ],
    )

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # TurbineGovernorDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # MechanicalLoadDynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    # *Association not used*
    # Type M:0..1 in CIM  # pylint: disable-next=line-too-long
    # WindTurbineType1or2Dynamics : Optional[str] = Field(default=None, in_profiles = [Profile.DY, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.DY,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import AsynchronousMachineDynamics"
# work as well as
# "from AsynchronousMachineDynamics import AsynchronousMachineDynamics".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = AsynchronousMachineDynamics
