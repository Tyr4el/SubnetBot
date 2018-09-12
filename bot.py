import discord
import token
import ip_address
import points

TOKEN = token.TOKEN

client = discord.Client()


@client.event
async def on_message(message):
    author = message.author
    user_id = message.author.id
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Shutdown
    if message.content.startswith('$shutdown'):
        client.close()

    # Guessing game for guessing the network address of an IP
    if message.content.startswith('$subnet-network'):
        question = 'What is the Network address of {}'.format(ip_address.formatted_ip_address)
        answer = ip_address.ip_network
        await client.send_message(message.channel, question)

        guess = await client.wait_for_message(timeout=25.0, author=author)

        if guess is None:
            fmt = 'Sorry {}, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(author.mention, answer))
            return
        if guess == answer:
            await client.send_message(message.channel, 'Correct {}!  +10 Points!'.format(author.mention))
            points.set_points(user_id, points.get_points(user_id) + 10)
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}. -5 Points'.format(answer))
            points.set_points(user_id, points.get_points(user_id) - 5)

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
