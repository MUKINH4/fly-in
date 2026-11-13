from models import Map, Zone
from typing import List


class Config:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.zones: List[Zone] = []
        self.nb_drones: int = 1
    def parser(self):
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
                        print(nb_drones)

        except Exception as e:
            return e
