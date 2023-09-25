"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

from functools import cached_property
from typing import Optional
from pydantic import Field
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from .EnergyArea import EnergyArea


@dataclass(config=DataclassConfig)
class SubLoadArea(EnergyArea):
    """
    The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load
      scaling.

    LoadArea: The LoadArea where the SubLoadArea belongs.
    LoadGroups: The Loadgroups in the SubLoadArea.
    """

    LoadArea: Optional[str] = Field(
        default=None,
        in_profiles=[
            Profile.EQ,
        ],
    )

    # *Association not used*
    # Type M:1..n in CIM  # pylint: disable-next=line-too-long
    # LoadGroups : list = Field(default_factory=list, in_profiles = [Profile.EQ, ])

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.EQ,
        }
