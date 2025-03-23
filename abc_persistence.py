### abstract interface for persisting data
from abc import ABC, abstractmethod


class ABCPersistence(ABC):
    @abstractmethod
    def save(self, data) -> None:
        pass

    @abstractmethod
    def load(self):
        pass
