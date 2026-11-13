from enum import Enum


class ZoneTypesEnum(str, Enum):
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class ZoneDefinitionsEnum(str, Enum):
    STARTING = "start_hub"
    ENDING = "end_hub"
    REGULAR = "hub"


class ColorsEnum(tuple[int, int, int], Enum):
    WHITE = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)


class DroneStatusEnum(str, Enum):
    MOVING = "moving"
    IN_TRANSIT = "in_transit"
    WAITING = "waiting"
    DELIVERED = "delivered"
