import discord
import constants
import ip_address
import points

TOKEN = constants.TOKEN

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
        await client.send_message(message.channel, ':wave: Bye :wave: bye!')
        await client.close()

    if message.content.startswith('$restart'):
        await client.send_message(message.channel, 'Okay brb!')
        await client.close()
        await client.connect()

    # Guessing game for guessing the network address of an IP
    # $subnet-network
    if message.content.startswith('$subnet-network'):
        question = 'What is the Network address of **{}**?'.format(ip_address.formatted_ip_address)
        answer = ip_address.ip_network
        embed_question = discord.Embed(
            title="Subnetting: Finding Network Addresses",
            description=question,
            color=0x00FF00  # Green
        )

        embed_timeout = discord.Embed(
            title="Subnetting: Finding Network Addresses",
            description='Sorry {}, you took too long. It was **{}**'.format(author.mention, answer),
            color=0xFF0000  # Red
        )

        embed_correct = discord.Embed(
            title="Subnetting: Finding Network Addresses",
            description='Correct {}!  +10 Points!'.format(author.mention),
            color=0x00FF00  # Green
        )

        embed_wrong = discord.Embed(
            title="Subnetting: Finding Network Addresses",
            description='Sorry {}. It is actually **{}**. -5 Points'.format(author.mention, answer),
            color=0xFF0000
        )

        await client.send_message(message.channel, embed=embed_question)

        guess = await client.wait_for_message(timeout=30.0, author=author)

        # If the user enters nothing
        if guess is None:
            await client.send_message(message.channel, embed=embed_timeout)
            return
        # Correct answer given
        if guess == answer:
            await client.send_message(message.channel, embed=embed_correct)
            points.set_points(user_id, points.get_points(user_id) + 10)
        # Wrong answer given
        else:
            await client.send_message(message.channel, embed=embed_wrong)
            points.set_points(user_id, points.get_points(user_id) - 5)

    # Guessing game for guessing the broadcast address of an IP
    # $subnet-broadcast
    if message.content.startswith('$subnet-broadcast'):
        question = 'What is the Broadcast address of **{}**?'.format(ip_address.formatted_ip_address)
        answer = ip_address.ip_network.broadcast_address
        embed_question = discord.Embed(
            title="Subnetting: Finding Broadcast Addresses",
            description=question,
            color=0x00FF00  # Green
        )

        embed_timeout = discord.Embed(
            title="Subnetting: Finding Broadcast Addresses",
            description='Sorry {}, you took too long. It was **{}**'.format(author.mention, answer),
            color=0xFF0000  # Red
        )

        embed_correct = discord.Embed(
            title="Subnetting: Finding Broadcast Addresses",
            description='Correct {}!  +10 Points!'.format(author.mention),
            color=0x00FF00  # Green
        )

        embed_wrong = discord.Embed(
            title="Subnetting: Finding Broadcast Addresses",
            description='Sorry {}. It is actually **{}**. -5 Points'.format(author.mention, answer),
            color=0xFF0000  # Red
        )

        await client.send_message(message.channel, embed=embed_question)

        guess = await client.wait_for_message(timeout=30.0, author=author)

        # If the user enters nothing
        if guess is None:
            await client.send_message(message.channel, embed=embed_timeout)
            return
        # Correct answer given
        if guess == answer:
            await client.send_message(message.channel, embed=embed_correct)
            points.set_points(user_id, points.get_points(user_id) + 10)
        # Wrong answer given
        else:
            await client.send_message(message.channel, embed=embed_wrong)
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
