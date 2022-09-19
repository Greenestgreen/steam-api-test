from port.inventory_publisher import InventoryPublisher
from config.inventory_publisher_discord_config import InventoryExtractorDiscordConfig
from shared.discord_bot import DiscordBot

import json

class InventoryPublisherDiscord(InventoryPublisher):

    def publish(self, message):
        inventoryExtractorDiscordConfig  = InventoryExtractorDiscordConfig.make_from_env()
        if inventoryExtractorDiscordConfig.validate():            
            self.sendMessageDiscord(inventoryExtractorDiscordConfig.apikey, inventoryExtractorDiscordConfig.channel_id ,message)
        else:
            raise Exception("No all variables are set")

    def sendMessageDiscord(self,apikey, channel, message):
        DiscordBot.sendMessage(apikey,channel, message)




