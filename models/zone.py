from enums import ZoneDefinitionsEnum
from .metadata import ZoneMetadata


class Zone:
    def __init__(self,
                 hub: ZoneDefinitionsEnum,
                 name: str,
                 loc_x: int,
                 loc_y: int,
                 metadata: ZoneMetadata):
        self.hub = hub
        self.name = name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.metadata = metadata
