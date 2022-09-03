from abc import ABC, abstractmethod

class InventoryPublishController(ABC):
    @abstractmethod
    def PublishIventory(self, events) -> str:
        pass