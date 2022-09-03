from abc import ABC, abstractmethod

class InventoryPublisher(ABC):
    @abstractmethod
    def publish(self, ivnentory) -> str:
        pass