from controller.inventory_publish_controller import InventoryPublishController
from service.publish_inventory_service import PublishInventoryService
from adapter import inventory_extractor_request,inventory_publisher_discord

class InventoryPublishDiscord(InventoryPublishController):

    def PublishIventory(self,profile):

        
        publishInventoryService = PublishInventoryService(inventory_extractor_request.InventoryExtractorRequest(), inventory_publisher_discord.InventoryPublisherDiscord())
        publishInventoryService.invoke(profile)
