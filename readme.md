# **Welcome**

A simple Discord bot written in Python to help users practice their subnetting skills with games for guessing the subnet network and broadcast addresses.  Also includes a powers game to guess the answer of a random power with the base 2.

# **Installation**

1. Log in to your Discord account at 
https://discordapp.com/developers
2. Create a new application and name it whatever you want (this bot is called SubnetBot) and save your changes
3. Copy the Client ID and Client Secret and save them somewhere for the time being
4. Clone the GitHub repo onto your computer (like in your Downloads folder) ```C:\Users\username\Downloads\```
5. Enter your terminal/command prompt and ```cd``` to the *project* directory and enter the following ```pip install -r requirements.txt```
6. Copy your Client Secret into the constants.py folder between the " "
7. Follow the guide linked below for the final steps 

From this point on, you can follow the guide below to add the bot to your server.

**Note**: The bot needs Administrator privileges when being added and can only be added to a server *you* own.

https://github.com/jagrosh/MusicBot/wiki/Adding-Your-Bot-To-Your-Server

# **Commands**

1. **$points:** Shows the user's current points
2. **$leaderboard:** Displays the top 10 users and their points
3. **$subnet-network:** Starts a game for anyone in the channel to guess the network address of a given IP address and mask in the format xxx.xxx.xxx.xxx/yy
4. **$subnet-broadcast:** Starts a game for anyone in the channel to guess the broadcast address of a given IP address and mask
5. **$subnet-subnet:** Starts a game for anyone in the channel to guess the subnets of a given IP address and mask with answers delimited by a comma in the format xxx.xxx.xxx.xxx/yy (**WIP - NOT WORKING CURRENTLY**)
6. **$power:** Starts a game for anyone in the channel to guess the answer of a random power with base 2 (i.e. 2^10)
7. **$help:** DMs this help message to the user

