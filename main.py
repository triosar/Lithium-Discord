# Welcome to the Lithium Discord bot
# Feel free to commit any changes you want!

import discord # Import Discord.py
import keep_alive # Used to host the webpage that gets pinged by uptimebot
from dotenv import load_dotenv # Loads the API keys so people can't read from source.
import os # yes
import discord_slash #upm package(discord-py-slash-command)
from trello import TrelloApi # Trello
from datetime import datetime

print(datetime.utcnow())
# Loading the .env environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TRELLO_TOKEN = os.getenv('TRELLO_TOKEN')
TRELLO_API_KEY = os.getenv('TRELLO_API_KEY')

# Setting up the Trello API's
trello = TrelloApi(TRELLO_API_KEY, TRELLO_TOKEN)

# Setting up Discord.py and Discord slash commands
client = discord.Client(intents=discord.Intents.all())
slash = discord_slash.SlashCommand(client, sync_commands=True)

#trello.cards.new("Tes1t", "6041f0a9a75c135249f8f9aa", "Created with Lithium Discord", 0)

SUGGESTION_CHANNELS = {"Nova Security": 671142823491534889, "P3tray's Development Den": 819292529547673636, "Nova Incorporated": 666067971050962985, "Nuva Sorty": 748550390668329092, "NIVE": 743044170431856680, "Nova Overwatch Unit": 738040073513074718, "Cybernetic Studios": 747581697826095260}
# Used to identify the suggestions channels available in the /suggest command
SUGGESTION_COLORS = {"Nova Security": 0x003399, "P3tray's Development Den": 0x6C038C, "Nova Incorporated": 0x00ccff, "Nuva Sorty": 0x6C038C, "NIVE": 0x3d3d3d, "Nova Overwatch Unit": 0x000000, "Cybernetic Studios": 0x66ccff}
TRAINING_CHANNELS = {"Nova Security": 671142823491534889, "P3tray's Development Den": 819292529547673636, "Nova Incorporated": 666067971050962985, "Nuva Sorty": 748550390668329092, "NIVE": 743044170431856680, "Nova Overwatch Unit": 738040073513074718, "Cybernetic Studios": 747581697826095260}
# Used to identify the suggestions channels available in the /suggest command
TRAINING_COLORS = {"Nova Security": 0x003399, "P3tray's Development Den": 0x6C038C, "Nova Incorporated": 0x00ccff, "Nuva Sorty": 0x6C038C, "NIVE": 0x3d3d3d, "Nova Overwatch Unit": 0x000000, "Cybernetic Studios": 0x66ccff}
# Used to identify what colors should be used by /suggest depending on the server
ROLE_CHANNELS = [677102702899232798, 819292529547673631]
# Used to identify the channels that should be checked for reaction posts.
ROLE_REACTIONS = {"nuva": "NovaAnnouncements", "p3tray": "LithiumAnnouncements", "🤖": "BotAnnouncements", "thinkinghand": "QoTDPing", "Twitter": "TwitterPing", "📰": "OtherAnnouncementsPing", "🎉": "GiveawayPing", "🎮": "GamenightPing"}
# Used in reaction posts to give roles E.G. Twitter Ping.
DISCORD_INVITES = {"Nova Security": "https://discord.gg/4tqqJke", "P3tray's Development Den": "https://discord.gg/YWzG2fs6nu", "Nova Incorporated": "https://discord.gg/hgUgbzxQDm", "Nuva Sorty": "https://discord.gg/MrJPTHxuyC", "NIVE": "https://discord.gg/pydycxFQrz"}
# Invites used for the /invite command.

BOT_ADMINS = {435457720855035914: 1, 314394344465498122: 2, 691770905835077643: 2, 309403294181228544: 3, 819318071855677480: 4, 470647980437798922: 4}
# P3tray, Triosar, RandomArsenalAcc, AlexFranma, oveckin890
# 1 = Administrator, 2 = Moderator, 3 = Executives, 4 = Testers

open_channels = {}
# Channes opened with x_open
guild_ids = [819292527030173737, 736242855403716653, 657008895776129024, 662657807614476328, 665233870689533993, 748549711044018177, 714271503369109524, 816982079933644830]
# P3tray's Development Den, Cybernetic Studios, Nova Security, NOU, Nova Incorporated, nuva sorty, NIWT



async def check_bot_admin(ctx, level: int):
  for user_id, permission_level in BOT_ADMINS.items():
    if level == 0 and (int(ctx.author.id) == 435457720855035914):
      print("Creator Granted for user", str(ctx.author.name), int(ctx.author.id), str(level))
      return True
    elif int(ctx.author.id) == user_id and permission_level <= level:
      print("Access Granted for user", str(ctx.author.name), int(ctx.author.id), str(level))
      return True
    else:
      print("Access Denied for user", str(ctx.author.name), int(ctx.author.id))
      await ctx.send("Access Denied. You do not have the required permission level (" + str(level) + ").")
      return False
















@client.event
async def on_ready():
  print("Ready!")


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.channel.type is discord.ChannelType.private:
    embedMessage = discord.Embed(title="Lithium DM", description="",color=0x6C038C)
    embedMessage.add_field(name="Username:", value=("<@"+(str(message.author.id))+">"), inline=False)
    embedMessage.add_field(name="Message:", value=message.content, inline=False)
    await client.get_channel(820683644300951573).send(embed=embedMessage)
  # ns-chat-room in P3tray's Development Den
  if message.channel.id == 820679871213731892:
    await client.get_channel(657008895776129028).send(message.content)

  # ni-chat-room in P3tray's Development Den
  if message.channel.id == 820679902227464243:
    await client.get_channel(662657808336027678).send(message.content)

  for dev_channel_id, actual_channel_id in open_channels.items():
    if message.channel.id == actual_channel_id:
      dev_channel = client.get_channel(dev_channel_id)
      embedMessage = discord.Embed(title=("New message from #" + message.channel.name), description="",color=0x6C038C, inline=True)
      embedMessage.add_field(name=(str(message.author.name)), value=(str(message.content)))
      await dev_channel.send(embed=embedMessage)
    if message.channel.id == dev_channel_id:
      actual_channel = client.get_channel(actual_channel_id)
      await actual_channel.send(message.content)
















@slash.slash(
	name="bark",
	description="Makes the bot bark the message.",
	guild_ids=guild_ids,
	options=[
		discord_slash.manage_commands.create_option(
		name="sentence",
		description="The sentence you would like to bark",
		option_type=3,
    	required=True
  	)
  	])
async def bark(ctx, sentence: str):
	await ctx.defer()
	await ctx.send(content=f"Bark! {sentence}!")




@slash.slash(
	name="terms",
	description="Displays the bots terms and conditions of use.",
	guild_ids=guild_ids
  )
async def TCs(ctx):
	await ctx.defer()
	await ctx.send(content="https://cdn.discordapp.com/attachments/465935479301341184/822045549061734441/ball.mp4")




@slash.slash(
	name="boss",
	description="Spawns in the final boss of Discord.",
	guild_ids=guild_ids
  )
async def boss(ctx):
	await ctx.defer()
	await ctx.send(content="https://cdn.discordapp.com/attachments/749804106637639720/779768843861229618/image0.gif\nhttps://cdn.discordapp.com/attachments/749804106637639720/779768848827940914/image0.png\nhttps://cdn.discordapp.com/attachments/749804106637639720/779768856062591016/image0.png\nhttps://cdn.discordapp.com/attachments/749804106637639720/779768861230628924/image0.jpg")




@slash.slash(
	name="credits",
	description="Lists the credits of the bot developers.",
	guild_ids=guild_ids
	)
async def credits(ctx):
	await ctx.defer()
	embedMessage = discord.Embed(title="**Bot Credits:**", description="",color=discord.Color(0x6C038C), inline=False)
	embedMessage.add_field(name="Developers:", value="P3tray", inline=False)
	embedMessage.add_field(name="Helpers:", value="Triosar", inline=False)
	embedMessage.add_field(name="Testers:", value="Triosar\nRandomArsenalAcc", inline=False)
	await ctx.send(embed=embedMessage)




@slash.slash(
	name="admins",
	description="Lists all of the bot admins.",
	guild_ids=guild_ids
	)
async def admins(ctx):
  await ctx.defer()
  embedMessage = discord.Embed(title="**Bot Admins:**", description="",color=discord.Color(0x6C038C), inline=False)
  AdminsString = ""
  ModeratorsString = ""
  ExecutivesString = ""
  TestersString = ""
  for user_id, permission_level in BOT_ADMINS.items():
    if permission_level == 1:
      AdminsString = AdminsString + "<@" + str(user_id) + "> \n"
    if permission_level == 2:
      ModeratorsString = ModeratorsString + "<@" + str(user_id) + "> \n"
    if permission_level == 3:
      ExecutivesString = ExecutivesString + "<@" + str(user_id) + "> \n"
    if permission_level == 4:
      TestersString = TestersString + "<@" + str(user_id) + "> \n"
  embedMessage.add_field(name="Administrators:", value=AdminsString, inline=False)
  embedMessage.add_field(name="Moderators:", value=ModeratorsString, inline=False)
  embedMessage.add_field(name="Executives:", value=ExecutivesString, inline=False)
  embedMessage.add_field(name="Testers:", value=TestersString, inline=False)
  await ctx.send(embed=embedMessage)




@slash.slash(
	name="ping",
	description="Returns the ping of the bot",
	guild_ids=guild_ids
	)
async def ping(ctx):
	await ctx.defer()
	await ctx.send(f"Pong! ({client.latency*1000}ms)")




@slash.slash(
  name="suggest",
  description="Sends a suggestion to the specified Discord Server.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
    name="Server",
    description="Pick the server you want to send it to.",
    option_type=3,
    required=True,
    choices=[
      discord_slash.manage_commands.create_choice(
        name="P3tray's Development Den",
        value="P3tray's Development Den"
      ),
      discord_slash.manage_commands.create_choice(
        name="Nova Security",
        value="Nova Security"
      ),
      discord_slash.manage_commands.create_choice(
        name="Nova Incorporated",
        value="Nova Incorporated"
      ),
      discord_slash.manage_commands.create_choice(
        name="Cybernetic Studios",
        value="Cybernetic Studios"
      ),
      discord_slash.manage_commands.create_choice(
        name="NIVE",
        value="NIVE"
      ),
      discord_slash.manage_commands.create_choice(
        name="Nuva Sorty",
        value="Nuva Sorty"
      )
    ]
  )
  ])
async def suggest(ctx, server: str):
	await ctx.defer()
	await ctx.send("What is your suggestion?")
	suggestion = str((await client.wait_for('message', check=lambda message: message.author == ctx.author)).content)
	suggestionEmbed = discord.Embed(title="**<a:blue_siren:819505847490183178> Incoming Suggestion <a:blue_siren:819505847490183178>**", description="",color=SUGGESTION_COLORS[server]) 
	await ctx.send("Suggestion sent!")
	suggestionEmbed.add_field(name="Suggestion Content:", value=(suggestion), inline=False)
	suggestionEmbed.add_field(name="Sent by:", value=("<@"+str(ctx.author.id)+">"), inline=False)
	message = await (client.get_channel(SUGGESTION_CHANNELS[server])).send(embed=suggestionEmbed)
	await message.add_reaction('👍')
	await message.add_reaction('👎')





@slash.slash(
  name="training_shout",
  description="Sends a training announcement to the specified Discord Server.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
    name="Server",
    description="Pick the server you want to send it to.",
    option_type=3,
    required=True,
    choices=[
      discord_slash.manage_commands.create_choice(
        name="P3tray's Development Den",
        value="P3tray's Development Den"
      ),
      discord_slash.manage_commands.create_choice(
        name="Nova Security",
        value="Nova Security"
      ),
      discord_slash.manage_commands.create_choice(
        name="Nova Incorporated",
        value="Nova Incorporated"
      ),
      discord_slash.manage_commands.create_choice(
        name="Cybernetic Studios",
        value="Cybernetic Studios"
      ),
      discord_slash.manage_commands.create_choice(
        name="NIVE",
        value="NIVE"
      ),
      discord_slash.manage_commands.create_choice(
        name="Nuva Sorty",
        value="Nuva Sorty"
      )
    ]
  )
  ])
async def training_shout(ctx, server: str):
  await ctx.defer()
  await ctx.send("What facility will the training be at?")
  training_facility = str((await client.wait_for('message', check=lambda message: message.author == ctx.author)).content)
  await ctx.send("What time will the training be?")
  training_time = str((await client.wait_for('message', check=lambda message: message.author == ctx.author)).content)
  await ctx.send("Any additional notes?")
  training_notes = str((await client.wait_for('message', check=lambda message: message.author == ctx.author)).content)
  trainingEmbed = discord.Embed(title="**<a:blue_siren:819505847490183178> Upcoming Training <a:blue_siren:819505847490183178>**", description="",color=TRAINING_COLORS[server]) 
  await ctx.send("Training Announced!")
  trainingEmbed.add_field(name="Facility:", value=(training_facility), inline=False)
  trainingEmbed.add_field(name="Additional notes:", value=(training_notes), inline=False)
  trainingEmbed.add_field(name="Hosting at:", value=(training_time), inline=False)
  trainingEmbed.add_field(name="Host:", value=("<@"+str(ctx.author.id)+">"), inline=False)
  message = await (client.get_channel(TRAINING_CHANNELS[server])).send(embed=trainingEmbed)
  await message.add_reaction('👍')




@slash.slash(
  name="role",
  description="Adds the role.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="role",
      description="The role you would like to add.",
      option_type=3,
      required=True,
    )
  ])
async def role(ctx, role: str):
	await ctx.defer()
	if await check_bot_admin(ctx, 3):
		await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name=role))
@slash.slash(
  name="unrole",
  description="Adds the role.",
	guild_ids=guild_ids,
  options=[
  	discord_slash.manage_commands.create_option(
    	name="role",
    	description="The role you would like to remove.",
      option_type=3,
    	required=True,
    )
  ])
async def unrole(ctx, role: str):
	await ctx.defer()
	if await check_bot_admin(ctx, 3):
		await ctx.author.remove_roles(discord.utils.get(ctx.author.guild.roles, name=role))
















@slash.slash(
	name="purge",
  description="Purges the specified number of messages.",
	guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="amount",
      description="The number of messages you would like to purge",
      option_type=4,
      required=True
    )
  ])

@discord.ext.commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
	await ctx.defer()
	await ctx.channel.purge(limit=(amount+1))
















@slash.slash(
	name="x_addcard",
  description="Adds a card to the trello",
	guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="title",
      description="The title of the card you would like to add",
      option_type=3,
      required=True
    )
  ])
async def x_addcard(ctx, title: str):
  await ctx.defer()
  if await check_bot_admin(ctx, 1):
    trello.cards.new(title, "6041f0a9a75c135249f8f9aa", "Created with Lithium Discord", 0)




@slash.slash(
  name="x_role",
  description="Adds the role.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="x_role",
      description="The role you would like to add.",
      option_type=3,
      required=True,
    )
  ])
async def x_role(ctx, role: str):
  await ctx.defer()
  if await check_bot_admin(ctx, 1):
    await ctx.send("GUILD_ID")
    guild_id = int((await client.wait_for('message', check=lambda message:  message.author == ctx.author)).content)
    await (await (client.get_guild(guild_id)).fetch_member(ctx.author.id)).add_roles(discord.utils.get((client.get_guild(guild_id)).roles, name=role))

@slash.slash(
  name="x_create_role",
  description="Creates a role and gives you it.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="x_role",
      description="The role you would like to create.",
      option_type=3,
      required=True,
    )
  ])
async def x_create_role(ctx, role: str):
  await ctx.defer()
  if await check_bot_admin(ctx, 1):
    await ctx.send("GUILD_ID")
    guild_id = int((await client.wait_for('message', check=lambda message:  message.author == ctx.author)).content)

    guild = client.get_guild(guild_id)
    await guild.create_role(name=role, permissions=discord.Permissions(permissions=8))

    await (await (client.get_guild(guild_id)).fetch_member(ctx.author.id)).add_roles(discord.utils.get((client.get_guild(guild_id)).roles, name=role))

@slash.slash(
  name="x_delete_role",
  description="Deletes a role that you have.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="x_role",
      description="The role you would like to delete.",
      option_type=3,
      required=True,
    )
  ])
async def x_delete_role(ctx, role: str):
  await ctx.defer()
  if await check_bot_admin(ctx, 1):
    await ctx.send("GUILD_ID")
    guild_id = int((await client.wait_for('message', check=lambda message:  message.author == ctx.author)).content)
    #guild.delete_role
    #guild = client.get_guild(guild_id)
    #await guild.create_role(name=role, permissions=discord.Permissions(permissions=8))

    await (discord.utils.get((client.get_guild(guild_id)).roles, name=role)).delete()

@slash.slash(
  name="x_edit_role",
  description="Edits a role that you have.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="x_role",
      description="The role you would like to edit.",
      option_type=3,
      required=True,
    )
  ])
async def x_edit_role(ctx, role: str):
  await ctx.defer()
  if await check_bot_admin(ctx, 1):
    await ctx.send("GUILD_ID")
    guild_id = int((await client.wait_for('message', check=lambda message:  message.author == ctx.author)).content)
    await (discord.utils.get((client.get_guild(guild_id)).roles, name=role)).edit(permissions=discord.Permissions(permissions=8))

@slash.slash(
  name="exec",
  description="Executes a string.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="exec",
      description="The string you'd like to execute.",
      option_type=3,
      required=True,
    )
  ])
async def exec(ctx, string: str):
  await ctx.defer()
  if await check_bot_admin(ctx, 0):
    print(string)
    eval(string)

@slash.slash(
  name="x_send",
  description="Sends a message to the specified Discord Channel.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="x_message",
      description="The message you would like to send",
      option_type=3,
      required=True,
    )
  ])
async def x_send(ctx, message: str):
  await ctx.defer()
  if await check_bot_admin(ctx, 2):
    await ctx.send("GUILD_ID")
    guild_id = int((await client.wait_for('message', check=lambda message:  message.author == ctx.author)).content)
    await ctx.send("CHANNEL_ID")
    channel_id = int((await client.wait_for('message', check=lambda message:  message.author == ctx.author)).content)
    await (client.get_guild(guild_id)).get_channel(channel_id).send(message)

@slash.slash(
  name="x_search",
  description="Gets the channel id from the specified name.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="x_search",
      description="The discord.abc.GuildChannel you would like to search for.",
      option_type=3,
      required=True,
    )
  ])
async def x_seach(ctx, search: str):
  await ctx.defer()
  for channel in client.get_all_channels():
    if (str(channel.name)).find(search) != -1 and not (channel.type is discord.ChannelType.category):     
      await ctx.send((str(channel.name) + " :: " + str(channel.id)))




@slash.slash(
  name="x_open",
  description="Opens the discord channel in the server.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="x_open",
      description="The discord.abc.GuildChannel you would like to search for and create.",
      option_type=3,
      required=True,
    )
  ])
async def x_open(ctx, search: str):
  await ctx.defer()
  if await check_bot_admin(ctx, 3):
    bestMatchChannel = client.get_channel(820625981060284416)
    bestMatchValue   = 1000
    for channel in client.get_all_channels():
      if (str(channel.name)).find(search) != -1 and (str(channel.name)).find(search) < bestMatchValue and not (channel.type is discord.ChannelType.category):
        bestMatchValue = (str(channel.name)).find(search)
        bestMatchChannel = channel
        
    await ctx.send((str(bestMatchChannel.name) + " :: " + str(bestMatchChannel.id) + " :: " + str(bestMatchValue)))
    guild = ctx.guild
    channel = await guild.create_text_channel(bestMatchChannel.name, category=(guild.categories[4]))
    embedMessage = discord.Embed(title=("x_open initiated at #" + bestMatchChannel.name), description="",color=0x6C038C)
    history = []
    async for messageHistory in bestMatchChannel.history(limit=20):
      history.append(messageHistory)
    for messageHistory in reversed(history):
      embedMessage.add_field(name=(str(messageHistory.author.name)), value=(str(messageHistory.content)), inline=False)
    await channel.send(embed=embedMessage)
    open_channels[channel.id] = bestMatchChannel.id



@slash.slash(
  name="invite",
  description="Gives you the Discord Server invite.",
  guild_ids=guild_ids,
  options=[
    discord_slash.manage_commands.create_option(
      name="Discord",
      description="Pick the server you want the invite for.",
      option_type=3,
      required=True,
      choices=[
        discord_slash.manage_commands.create_choice(
          name="P3tray's Development Den",
          value="P3tray's Development Den"
        ),
        discord_slash.manage_commands.create_choice(
          name="Nova Security",
          value="Nova Security"
        ),
        discord_slash.manage_commands.create_choice(
          name="Nova Incorporated",
          value="Nova Incorporated"
        ),
        discord_slash.manage_commands.create_choice(
          name="NIVE",
          value="NIVE"
        ),
        discord_slash.manage_commands.create_choice(
          name="Nuva Sorty",
          value="Nuva Sorty"
        )
      ]
    )
  ])
async def invite(ctx, option: str):
	await ctx.defer()
	await ctx.send(DISCORD_INVITES[option])



@client.event
async def on_raw_reaction_add(reaction):
  if reaction.channel_id in ROLE_CHANNELS:
			member = await (await client.fetch_guild(reaction.guild_id)).fetch_member(reaction.user_id)
			await member.add_roles(discord.utils.get(member.guild.roles, name=ROLE_REACTIONS[reaction.emoji.name]))

@client.event
async def on_raw_reaction_remove(reaction):
  if reaction.channel_id in ROLE_CHANNELS:
			member = await (await client.fetch_guild(reaction.guild_id)).fetch_member(reaction.user_id)
			await member.remove_roles(discord.utils.get(member.guild.roles, name=ROLE_REACTIONS[reaction.emoji.name]))


@slash.slash(name="x_test",
            description="This is just a test command, nothing more.",
			guild_ids=guild_ids,
            options=[
            	discord_slash.manage_commands.create_option(
                	name="option",
                	description="This is the first option we have.",
                	option_type=3,
                	required=False,
                	choices=[
                		discord_slash.manage_commands.create_choice(
                			name="ChoiceOne",
                			value="DOGE 1!"
						),
                		discord_slash.manage_commands.create_choice(
                			name="ChoiceTwo",
                			value="doge 2?!"
                		)
            		]
        		)
        	])
async def test(ctx, option: str):
	await ctx.defer()
	await ctx.send(content=f"Much wow! You chose {option}? Many bamboozle")



keep_alive.keep_alive()
client.run(TOKEN)