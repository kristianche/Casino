from abc import ABC, abstractmethod


class SlotMachine(ABC):

    @staticmethod
    @abstractmethod
    def rules(self):
        ...

    @abstractmethod
    def play(self):
        ...