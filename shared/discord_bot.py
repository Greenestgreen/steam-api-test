import discord

class DiscordBot():

    def sendMessage(apikey,channel_id, message):
        intents = discord.Intents.default()
        intents.message_content = True
        client = discord.Client(intents=intents)
    
        @client.event
        async def on_ready():
            for channel  in client.get_all_channels():
                if  channel.name == "general":
                    await channel.send(message) 
                
            await client.close()     
        
        client.run(apikey)