import os
from shared.validator import Validator

class InventoryExtractorRequestConfig(Validator):

    def __init__(self,apikey):
       self.apikey = apikey

    def make_from_env():
        return InventoryExtractorRequestConfig(os.environ.get("steamapikey"))

    
    def validate(self) -> str:
        
        if not self.validateField(self.apikey):
            self.addError("steamapikey", "either null or emtpy")

        