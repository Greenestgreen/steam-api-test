import argparse
from decimal import InvalidOperation
import sys
from controller.inventory_publish_cli import InventoryPublishCli
from controller.inventory_publish_discord import InventoryPublishDiscord

def parseArguments():
    
    parser = argparse.ArgumentParser(description='Porcess Steam key.')
    parser.add_argument('--profile', dest='profile',type=str, help='The profile to make the request')

    args = parser.parse_args()
    return args.profile

if __name__ == "__main__":
    profile = parseArguments()
    inventoryPublishCli = InventoryPublishCli()
    #inventoryPublishCli.PublishIventory(profile)
    inventoryPublishDiscord = InventoryPublishDiscord()
    inventoryPublishDiscord.PublishIventory(profile)
    
