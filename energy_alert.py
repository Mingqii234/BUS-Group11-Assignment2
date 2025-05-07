from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for obs in self._observers:
            obs.update(self)

class RoomStatus(Subject):
    def __init__(self, room_name, is_occupied, light_on, ac_on):
        super().__init__()
        self.room_name   = room_name
        self.is_occupied = is_occupied
        self.light_on    = light_on
        self.ac_on       = ac_on

    def set_status(self, is_occupied: bool, light_on: bool, ac_on: bool):
        self.is_occupied = is_occupied
        self.light_on    = light_on
        self.ac_on       = ac_on
        self.notify()

class EnergyAlertSystem(Observer):
    def update(self, subject):
        if not isinstance(subject, RoomStatus):
            return
        if not subject.is_occupied and (subject.light_on or subject.ac_on):
            reason = []
            if subject.light_on:
                reason.append("light is ON")
            if subject.ac_on:
                reason.append("AC is ON")
            detail = " and ".join(reason)
            print(f" Alert: {subject.room_name} is empty but {detail}!")




