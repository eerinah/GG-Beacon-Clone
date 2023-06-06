import discord
import responses

async def send_message(message, user_message, username, nchannel):
    try:
        response = responses.handle_response(user_message)

        #here we evaluate the prefix given by the model in responses.py
        #if its 0 we can just do nothing
        #if 1 we send a message that it was hateful
        #if 2 we send a message that it was depressive
        if response[0] == '0':
            response = username + ' said normal message: ' + response[1:]
        elif response[0] == '1':
<<<<<<< Updated upstream
            response = username + ' said hateful message: ' + response#response[1:]
=======
            response = username + ' said message that indicates harm towards others: ' + response[1:]
        elif response[0] == '2':
            response = username + ' said message that indicates harm towards self: ' + response[1:]
>>>>>>> Stashed changes


        await nchannel.send(response)
        #await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)



def run_discord_bot():
    TOKEN = 'MTExNTA1NDg5NDE5MDE3ODQ2NQ.GW7Z0g.Ku8r1oZdFhr82a8fD8YREzph4H0ThYA_4PTEkk'
    intents = discord.Intents.default()
    intents.message_content = True #so the bot can read messages
    client = discord.Client(intents=intents)
    
    #client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        #dont want the bot to react to its own messages
        if message.author == client.user:
            return

        #extract information from the message
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #debugging purposes
        print(f"{username} said: '{user_message}' ({channel})")
        #print(f"{message} {message.content}")

        #output to the output channel
        nchannel = client.get_channel(1115086982444482640) #send it to the output channel

        #if it starts with a question, then we send it to the user who sent the message
        #depending on use case we could try to figure out how to make it send to a particular person ?
        await send_message(message, user_message, username, nchannel)


        #if it starts with a question, then we send it to the user who sent the message
        #depending on use case we could try to figure out how to make it send to a particular person ?
        # if user_message[0] == '?':
        #     user_message = user_message[1:]
        #     await send_message(message, user_message, is_private=True)
        # else:
        #     await send_message(message, user_message, is_private=False)
    
    client.run(TOKEN)