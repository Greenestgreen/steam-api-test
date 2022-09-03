from port.inventory_publisher import InventoryPublisher


class InventoryPublisherConsole(InventoryPublisher):

    def publish(self, inventory) -> str:
        print(inventory)