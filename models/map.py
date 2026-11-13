from .zone import Zone
from .connection import Connection
from typing import List


class Map:
    def __init__(self,
                 zones: List[Zone],
                 connections: List[Connection],
                 nb_drones: int = 1
                 ) -> None:
        self.zones = zones
        self.connections = connections
        self.nb_drones = nb_drones
