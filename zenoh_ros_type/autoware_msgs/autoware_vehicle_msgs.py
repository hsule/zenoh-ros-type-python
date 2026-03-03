from dataclasses import dataclass

from pycdr2 import Enum, IdlStruct
from pycdr2.types import uint8

from ..rcl_interfaces.builtin_interfaces import Time


@dataclass
class GearCommand(IdlStruct, typename='GearCommand'):
    stamp: Time

    class COMMAND(Enum):
        NONE = 0
        NEUTRAL = 1
        DRIVE = 2
        REVERSE = 20
        PARK = 22
        LOW = 23

    command: uint8
