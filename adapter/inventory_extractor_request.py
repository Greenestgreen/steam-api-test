from time import sleep
from port.inventory_extractor import InventoryExtractor
from config.inventory_extractor_request_config import InventoryExtractorRequestConfig
import json

import requests

class InventoryExtractorRequest(InventoryExtractor):
    
    def getInventory(self, profile):
        inventoryExtractorRequestConfig = InventoryExtractorRequestConfig.make_from_env()
        inventoryExtractorRequestConfig.validate()
        if inventoryExtractorRequestConfig.isValid():
            key = inventoryExtractorRequestConfig.apikey            
            r = requests.get(f"https://steamcommunity.com/id/{profile}/inventory/json/730/2")

            return  self.buildMessage(json.loads(r.content)["rgDescriptions"],profile)
        else:
            raise Exception("Could make request for inventory")

    
    def buildMessage(self, inventory,profile):

        items = []
        value = 0
        for k,v in inventory.items():

            hash_name = inventory[k].get("market_hash_name")
            exclude = ["Case", "Graffiti", "Sticker", "Medal", "Coin", "Badge", "Bonus Rank XP", "Music Kit","Trophy"]
            if  not any(x in hash_name for x in exclude) and "|" in hash_name:
                sleep(2)
                items.append(hash_name)                    
                print(f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={hash_name}")
                market_request = requests.get(f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name={hash_name}")
                market_item = json.loads(market_request.content)
                if market_item is None or market_item.get("median_price") is None:
                    print(hash_name)
                    continue
                value = value + float(market_item.get("median_price")[1:])

        message = f"The total value of `{profile}'s` inventory is :{value} USD"
        items_message = "\n".join(items)
        return message + f"``` {items_message[0:1900]}```"
