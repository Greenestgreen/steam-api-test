from abc import ABC, abstractmethod

class InventoryExtractor(ABC):
    @abstractmethod
    def getInventory(self, events) -> str:
        pass