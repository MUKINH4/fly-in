from .zone import Zone
from .connection import Connection
from typing import List


class Map:
    def __init__(self) -> None:
        self.nb_drones = 1
        self.connections: List[Connection] = []
        self.zones: List[Zone] = []

    def add_map(self,
                zones: List[Zone],
                connections: List[Connection],
                nb_drones: int
                ) -> None:
        self.zones = zones
        self.connections = connections
        self.nb_drones = nb_drones

