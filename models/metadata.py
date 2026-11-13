from enums import ZoneTypesEnum, ColorsEnum


class ZoneMetadata:
    def __init__(self,
                 color: ColorsEnum = ColorsEnum.WHITE,
                 zone_type: ZoneTypesEnum = ZoneTypesEnum.NORMAL,
                 max_drones: int = 1):
        self.color = color
        self.zone_type = zone_type
        self.max_drones = max_drones


class ConnMetadata:

    def __init__(self, max_link_capacity: int = 1):
        self.max_link_capacity = max_link_capacity
