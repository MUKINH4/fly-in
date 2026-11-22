from models import Map, Zone
from typing import List
from exceptions.exceptions import ParserException


class Config:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.zones: List[Zone] = []
        self.nb_drones: int = 1

    def parser(self):
        new_map = Map()
        try:
            with open(self.filepath, "r") as f:
                for i, line in enumerate(f):
                    line = line.strip()
                    if line.startswith("#"):
                        continue
                    if not line:
                        continue
                    if line.startswith("nb_drones"):
                        nb_drones = int(line.split(":")[1].strip())
                        self.nb_drones = nb_drones
                    else:
                        raise ParserException("The first line must be 'nb_drones'", line=i+1)
            # new_map.add_map(zones, connections, nb_drones)
        except ParserException as e:
            print(f"ParserException: [Line {e.line}] {e.message}")
        except Exception as e:
            return e
