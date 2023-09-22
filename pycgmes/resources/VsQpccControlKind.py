"""
Generated from the CGMES 3 files via cimgen: https://github.com/sogno-platform/cimgen
"""

import sys
from types import ModuleType

from functools import cached_property
from pydantic.dataclasses import dataclass
from ..utils.dataclassconfig import DataclassConfig
from ..utils.profile import BaseProfile, Profile

from ..utils.base import Base


@dataclass(config=DataclassConfig)
class VsQpccControlKind(Base, ModuleType):
    """
    Kind of reactive power control at point of common coupling for a voltage source converter.

    """

    def __call__(self, *args, **kwargs):
        # Dark magic - see last lines of the file.
        return VsQpccControlKind(*args, **kwargs)

    # No attributes defined for this class.

    @cached_property
    def possible_profiles(self) -> set[BaseProfile]:
        """
        A resource can be used by multiple profiles. This is the set of profiles
        where this element can be found.
        """
        return {
            Profile.SSH,
        }


# This + inheriting from ModuleType + __call__:
# makes:
# "import VsQpccControlKind"
# work as well as
# "from VsQpccControlKind import VsQpccControlKind".
# You would get a typechecker "not callable" error, but this might be useful for
# backward compatibility.
sys.modules[__name__].__class__ = VsQpccControlKind
