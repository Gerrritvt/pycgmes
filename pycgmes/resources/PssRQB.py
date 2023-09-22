"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .PowerSystemStabilizerDynamics import PowerSystemStabilizerDynamics


@dataclass(config=DataclassConfig)
class PssRQB(PowerSystemStabilizerDynamics, ModuleType):
    """
    Power system stabilizer type RQB. This power system stabilizer is intended to be used together with excitation
      system type ExcRQB, which is primarily used in nuclear or thermal generating units.

    ki2: Speed input gain (Ki2). Typical value = 3,43.
    ki3: Electrical power input gain (Ki3). Typical value = -11,45.
    ki4: Mechanical power input gain (Ki4). Typical value = 11,86.
    t4m: Input time constant (T4M) (>= 0). Typical value = 5.
    tomd: Speed delay (TOMD) (>= 0). Typical value = 0,02.
    tomsl: Speed time constant (TOMSL) (>= 0). Typical value = 0,04.
    t4mom: Speed time constant (T4MOM) (>= 0). Typical value = 1,27.
    sibv: Speed deadband (SIBV). Typical value = 0,006.
    kdpm: Lead lag gain (KDPM). Typical value = 0,185.
    t4f: Lead lag time constant (T4F) (>= 0). Typical value = 0,045.
    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return PssRQB(*args, **kwargs)

    ki2: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki3: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    ki4: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4m: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tomd: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    tomsl: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4mom: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

    sibv: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    kdpm: float = Field(
        default=0.0,
        in_profiles=[
            Profile.DY,
        ],
    )

    t4f: int = Field(
        default=0,
        in_profiles=[
            Profile.DY,
        ],
    )

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
# "import PssRQB"
# work as well as
# "from PssRQB import PssRQB".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = PssRQB
