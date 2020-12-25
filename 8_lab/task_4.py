#!/usr/bin/env python3
""" Laboratory work 8. Task 4 """
from abc import ABC, abstractmethod


class Edication():
    """
    This class defines the interface of edication to client
    """

    def __init__(self, edication_system):
        self._edication_system = edication_system

    @property
    def edication_system(self):
        return self._edication_system

    @edication_system.setter
    def set_edication_system(self, edication_system):
        self._edication_system = edication_system

    def get_edication_information(self):
        """ Return information about edication system """
        result = self._edication_system.system_interface()

        return result


class EdicationSystem(ABC):
    """
    This class declares an interface common to all suppoted systems
    """
    @abstractmethod
    def system_interface(self):
        pass


class Schoolchild(EdicationSystem):
    def system_interface(self):
        print("Школьник учится 11 лет")


class StudentBachelor(EdicationSystem):
    def system_interface(self):
        print("Бакалавр длится 4 года")


class StudentMaster(EdicationSystem):
    def system_interface(self):
        print("Магистратура длится 5 лет")


if __name__ == "__main__":
    edication = Edication(Schoolchild())
    print("Сначала ребенок учится в школе:")
    edication.get_edication_information()
    print()

    print("Далее поступает в университет:")
    edication.set_edication_system = StudentBachelor()
    edication.get_edication_information()
    print()

    print("Студент может получить магистерскую степень:")
    edication.set_edication_system = StudentMaster()
    edication.get_edication_information()
