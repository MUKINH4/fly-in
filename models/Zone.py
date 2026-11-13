from enums import ZoneDefinitionEnum
from .models import ZoneMetadata


class Zone:
	def __init__(self,
                 hub: ZoneDefinitionEnum,
                 name: str,
                 loc_x,
                 loc_y,
                 metadata: Metadata):
		self.hub = hub
        self.name = name
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.metadata = metadata
		
		
