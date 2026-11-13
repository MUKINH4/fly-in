from .models import ConnMetadata

class Connection:
    def __init__(self,
                 first_zone: Zone,
                 second_zone: Zone,
                 metadata: ConnMetadata):
        self.first_zone = first_zone
        self.second_zone = second_zone
        self.metadata = metadata

