from .zone import Zone
from .connection import Connection
from enums import DroneStatusEnum
from typing import List, Optional


class Drone:
    def __init__(self, drone_id: str, current_zone: Zone) -> None:
        self.drone_id = drone_id
        self.current_zone = current_zone
        self.conn_history: List[str] = [current_zone.name]
        self.drone_status: DroneStatusEnum = DroneStatusEnum.WAITING
        self.turns_count: int = 0
        self.current_conn = Optional[Connection] = None
        self.target_conn = Optional[Connection] = None
