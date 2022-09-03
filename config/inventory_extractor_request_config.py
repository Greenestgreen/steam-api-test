import os

class InventoryExtractorRequestConfig():

    def __init__(self,apikey):
       self.apikey = apikey

    def make_from_env():
        return InventoryExtractorRequestConfig(os.environ.get("steamapikey"))

    def validate(self):
        return True if self.apikey else False 