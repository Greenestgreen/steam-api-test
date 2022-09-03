from port.inventory_publisher import InventoryPublisher
from config.inventory_publisher_discord_config import InventoryExtractorDiscordConfig
from shared.discord_bot import DiscordBot

import json

class InventoryPublisherDiscord(InventoryPublisher):

    def publish(self, inventory):
        inventoryExtractorDiscordConfig  = InventoryExtractorDiscordConfig.make_from_env()
        message = self.buildMessage(inventory)
        self.sendMessageDiscord(inventoryExtractorDiscordConfig.apikey, inventoryExtractorDiscordConfig.channel_id ,message)

    def sendMessageDiscord(self,apikey, channel, message):
        DiscordBot.sendMessage(apikey,channel, message)

    def buildMessage(self,inventory):
        items = []
        ammount = len(inventory)
        for k,v in inventory.items():
            
            item_name = inventory[k].get("name")

            if "Case" not in item_name  and "Graffiti" not in item_name and "Sticker" not in item_name:
                items.append(inventory[k].get("name"))
        
        items_message = "\n".join(items)

        


        message = f"""Hey this person has  {ammount} items:
        ```{items_message[0:2000]} ```"""
        
        if len(items) < ammount/2:
            message  = message + "Apparently you only have cases and stickers"
        print(message)
        return message



