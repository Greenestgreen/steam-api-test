import os

class InventoryExtractorDiscordConfig():

    def __init__(self,apikey,channel_id):
       self.apikey = apikey
       self.channel_id = channel_id

    def make_from_env():
        return InventoryExtractorDiscordConfig(os.environ.get("discordkey"),os.environ.get("channel"))

    def validate(self):
        return True if self.apikey else False 