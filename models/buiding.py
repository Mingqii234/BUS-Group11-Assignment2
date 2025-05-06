#
class Building:
    def __init__(self, building_id):
        self.id = building_id
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def get_total_energy(self):
        return sum(d.get_total_energy() for d in self.devices)

    def get_devices(self):
        return self.devices

    def device_energy_breakdown(self):
        return {d.name: d.get_total_energy() for d in self.devices}




#
class Dormitory(Building):
    pass

class Laboratory(Building):
    pass

class Classroom(Building):
    pass

class BuildingFactory:
    @staticmethod
    def create_building(building_type):
        if building_type == "Dormitory":
            return Dormitory("Dormitory")
        elif building_type == "Laboratory":
            return Laboratory("Laboratory")
        elif building_type == "Classroom":
            return Classroom("Classroom")
        else:
            raise ValueError(f"Unknown building type: {building_type}")