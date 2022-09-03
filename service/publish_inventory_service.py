from port.inventory_extractor import InventoryExtractor
from port.inventory_publisher import InventoryPublisher
class PublishInventoryService():

    def __init__(self,inventoryExtractor: InventoryExtractor, inventoryPublisher: InventoryPublisher) -> None:
        self.inventoryExtractor = inventoryExtractor
        self.inventoryPublisher = inventoryPublisher

    def invoke(self, profile) -> bool:
        inventory = self.inventoryExtractor.getInventory(profile)
        self.inventoryPublisher.publish(inventory)
        return True

        
        