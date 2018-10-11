import discord
import constants
import ip_address
import ipaddress
import points
import random

TOKEN = constants.TOKEN

client = discord.Client()
points.load_points()


@client.event
async def on_message(message):
    author = message.author
    user_id = message.author.id
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Shutdown
    if message.content.startswith('$shutdown'):
        if author.server_permissions.administrator:
            await client.send_message(message.channel, ':wave: Bye :wave: bye!')
            points.save()
            await client.close()
        else:
            await client.send_message(message.channel, 'You do not have permissions to do that.')
    # Guessing game for guessing the network address of an IP
    # $subnet-network
    if message.content.startswith('$subnet-network'):
        ip = ip_address.IPAddress()
        question = "What is the Network address of **{}**?\n\n Format your answer as " \
                   "xxx.xxx.xxx.xxx/xx".format(ip.formatted_ip_address)
        answer = ip.ip_network
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
        current_channel = message.channel

        def check(msg):
            if msg.channel != current_channel:
                return False
            try:
                ipaddress.IPv4Network(msg.content, strict=False)
                return True
            except ipaddress.AddressValueError:
                return False

        guess = await client.wait_for_message(channel=message.channel, timeout=60.0, check=check)

        # If the user enters nothing
        if guess is None:
            await client.send_message(message.channel, embed=embed_timeout)
            return
        # Correct answer given
        if ipaddress.IPv4Network(guess.content, strict=False) == answer:
            await client.send_message(message.channel, embed=embed_correct)
            points.set_points(user_id, points.get_points(user_id) + 10)
            points.save()
        # Wrong answer given
        else:
            await client.send_message(message.channel, embed=embed_wrong)
            points.set_points(user_id, points.get_points(user_id) - 5)
            points.save()

    # Guessing game for guessing the broadcast address of an IP
    # $subnet-broadcast
    if message.content.startswith('$subnet-broadcast'):
        ip = ip_address.IPAddress()
        question = 'What is the Broadcast address of **{}**?'.format(ip.formatted_ip_address)
        answer = ip.ip_network.broadcast_address
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
        current_channel = message.channel

        def check(msg):
            if msg.channel != current_channel:
                return False
            try:
                ipaddress.IPv4Network(msg.content, strict=False)
                return True
            except ipaddress.AddressValueError:
                return False

        guess = await client.wait_for_message(timeout=30.0, check=check)

        # If the user enters nothing
        if guess is None:
            await client.send_message(message.channel, embed=embed_timeout)
            return
        # Correct answer given
        if guess.content == answer:
            await client.send_message(message.channel, embed=embed_correct)
            points.set_points(user_id, points.get_points(user_id) + 10)
            points.save()
        # Wrong answer given
        else:
            await client.send_message(message.channel, embed=embed_wrong)
            points.set_points(user_id, points.get_points(user_id) - 5)
            points.save()

    # Guessing game for guessing the subnets of an IP
    # $subnet-subnet
    # if message.content.startswith('$subnet-subnet'):
    #     ip = ip_address.IPAddress()
    #     question = 'What are the subnets of **{}**?\n\n Format your answer as \
    #                xxx.xxx.xxx.xxx/xx and separate subnets with a space'.format(ip.formatted_ip_address)
    #     answer = []
    #     for subnet in ip.subnets:
    #         answer.append(subnet)
    #         print(subnet)
    #
    #     print(answer)
    #
    #     embed_question = discord.Embed(
    #         title="Subnetting: Finding Subnets",
    #         description=question,
    #         color=0x00FF00  # Green
    #     )
    #
    #     embed_timeout = discord.Embed(
    #         title="Subnetting: Finding Subnets",
    #         description='Sorry {}, you took too long. It was **{}**'.format(author.mention, answer[0:]),
    #         color=0xFF0000  # Red
    #     )
    #
    #     embed_correct = discord.Embed(
    #         title="Subnetting: Finding Subnets",
    #         description='Correct {}!  +10 Points!'.format(author.mention),
    #         color=0x00FF00  # Green
    #     )
    #
    #     embed_wrong = discord.Embed(
    #         title="Subnetting: Finding Subnets",
    #         description='Sorry {}. It is actually **{}**. -5 Points'.format(author.mention, answer),
    #         color=0xFF0000  # Red
    #     )
    #
    #     await client.send_message(message.channel, embed=embed_question)
    #
    #     guess = await client.wait_for_message(channel=message.channel, timeout=60.0)
    #     # Split the guess into an array separated by a comma
    #     guess_split = set(guess.content.split(','))
    #     print(guess_split)  # Debugging
    #
    #     # If the user enters nothing
    #     if guess is None:
    #         await client.send_message(message.channel, embed=embed_timeout)
    #         return
    #     # Correct answer given
    #     if guess_split.issubset(answer):
    #         await client.send_message(message.channel, embed=embed_correct)
    #         points.set_points(user_id, points.get_points(user_id) + 10)
    #         points.save()
    #     # Wrong answer given
    #     else:
    #         await client.send_message(message.channel, embed=embed_wrong)
    #         points.set_points(user_id, points.get_points(user_id) - 5)
    #         points.save()

    if message.content.startswith("$power"):
        power = random.randint(1, 16)
        question = "What is the answer: **2^{}**".format(power)
        answer = 2 ** power

        embed_question = discord.Embed(
            title="Powers: Base 2",
            description=question,
            color=0x00FF00  # Green
        )

        embed_timeout = discord.Embed(
            title="Powers: Base 2",
            description='Sorry {}, you took too long. It was **{}**'.format(author.mention, answer),
            color=0xFF0000  # Red
        )

        embed_correct = discord.Embed(
            title="Powers: Base 2",
            description='Correct {}!  +10 Points!'.format(author.mention),
            color=0x00FF00  # Green
        )

        embed_wrong = discord.Embed(
            title="Powers: Base 2",
            description='Sorry {}. It is actually **{}**. -5 Points'.format(author.mention, answer),
            color=0xFF0000  # Red
        )

        await client.send_message(message.channel, embed=embed_question)

        current_channel = message.channel

        def is_int(msg):
            try:
                int(msg)
                return True
            except ValueError:
                return False

        def check(msg):
            return msg.channel == current_channel and is_int(msg.content)

        guess = await client.wait_for_message(channel=message.channel, timeout=10.0, check=check)

        # If the user enters nothing
        if guess is None:
            await client.send_message(message.channel, embed=embed_timeout)
            return
        # Correct answer given
        if guess.content == str(answer):
            await client.send_message(message.channel, embed=embed_correct)
            points.set_points(user_id, points.get_points(user_id) + 10)
            points.save()
        # Wrong answer given
        else:
            await client.send_message(message.channel, embed=embed_wrong)
            points.set_points(user_id, points.get_points(user_id) - 5)
            points.save()

    # Get user's points from the json file
    # $points
    if message.content.startswith('$points'):
        points_embed = discord.Embed(
            title='{}\'s Points'.format(author),
            description='You have **{}** points'.format(points.get_points(user_id)),
            color=0xFFFF00  # Yellow
        )
        await client.send_message(message.channel, embed=points_embed)

    # Display the leaderboard
    if message.content.startswith('$leaderboard'):
        leaderboard_embed = discord.Embed(
            title="Subnetting Leaderboard",
            description='The Top 10 Subnetting Masters!',
            color=0xFFFF00,  # Yellow
        )

        # Enumerate through get_leaderboard()
        # Set position to 1 + index
        # Set name to be a mention when it formats in Discord
        # points = value (couldn't use the same name)
        for index, item in enumerate(points.get_leaderboard()):
            position = index + 1
            name = '<@' + str(item[0]) + '>'
            value = item[1]
            leaderboard_embed.add_field(name='Position', value='**{0}.**'.format(position), inline=True)
            leaderboard_embed.add_field(name='Name', value='{0}'.format(name), inline=True)
            leaderboard_embed.add_field(name='Points', value='{0}'.format(value), inline=True)

        await client.send_message(message.channel, embed=leaderboard_embed)

    # Hello (Test)
    if message.content.startswith('$hello'):
        await client.send_message(message.channel, 'Hello {}'.format(author.mention))

    if message.content.startswith('$help'):
        await client.send_message(author,
                                  "**Developed By:** Tyr4el#9451\n\n"
                                  "**$points:** Shows the user's current points\n"
                                  "**$leaderboard:** Displays the top 10 user's and their points\n"
                                  "**$subnet-network:** Starts a game for anyone in the channel to guess the network "
                                  "address of a given IP address and mask in the format xxx.xxx.xxx.xxx/yy\n"
                                  "**$subnet-broadcast:** Starts a game for anyone in the channel to guess the "
                                  "broadcast address of a given IP address and mask\n"
                                  "**$subnet-subnet:** Starts a game for anyone in the channel to guess the subnets "
                                  "of a given IP address and mask with answers delimited by a comma in the format "
                                  "xxx.xxx.xxx.xxx/yy (**WIP - NOT WORKING CURRENTLY**)\n"
                                  "**$power:** Starts a game for anyone in the channel to guess the answer of a "
                                  "random power with base 2 (i.e. 2^10)\n"
                                  "**$help:** DMs this help message to the user")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Use $help'))


client.run(TOKEN)
