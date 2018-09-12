import discord
import token

TOKEN = token.TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Shutdown
    if message.content.startswith('$shutdown'):
        client.close()

    # Hello (Test)
    if message.content.startswith('$hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
