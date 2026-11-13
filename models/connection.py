from .metadata import ConnMetadata
from .zone import Zone


class Connection:
    def __init__(self,
                 zone_a: Zone,
                 zone_b: Zone,
                 metadata: ConnMetadata) -> None:
        self.zone_a = zone_a
        self.zone_b = zone_b
        self.metadata = metadata

    @property
    def name(self) -> str:
        return f"{self.zone_a.name}-{self.zone_b.name}"
