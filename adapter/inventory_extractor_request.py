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
            return json.loads(r.content)["rgDescriptions"]
        else:
            raise Exception("Could make request for inventory")