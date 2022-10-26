# Avis Mar Bot

import os
import random
import json

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content[0] != '!':
		return


	## Checks if command is a roll command and performs it if so


	roll_check = message.content.split(' ')
	if roll_check[0].lower() == '!roll':
		dice = roll_check[1].split('d')
		numDice = int(dice[0])
		typeDice = int(dice[1])
		diceRolled = []
		total = 0
		for x in range(numDice):
			roll = random.randint(1,typeDice)
			total += roll
			diceRolled.append(str(roll))
		if numDice == 0:
			return
		if numDice == 1:
			response = str(diceRolled[0])
			await message.channel.send(response)
			return
		response = '+'.join(diceRolled)
		response += '='
		response += str(total)
		await message.channel.send(response)
		return

	## Checks if command if a funny or quote command

	funny_list = ['Girthy Obelisk', 'The Gyrlz', 'Ulani joins the IRA', 'Fish tacos', 'The Tarrasque under the lake', 'Honkin Clams', 'Lake Lobster', 'Studying Russian']
	quote_list = ['Can you imagine shaving your frog?', 'It\'s been a few months since I\'ve died', 'Okay, so I have a gun', 'Your bird has been commandeered', 'Sultry as always', 'Oh god, you\'re fighting the pope']

	if message.content.lower() == '!quote':
		response = random.choice(quote_list)
		await message.channel.send(response)
		return

	if message.content.lower() == '!funny':
		response = random.choice(funny_list)
		await message.channel.send(response)
		return

	if message.content.lower() == '!johnny stop fucking with the bot':
		response = 'Ominous Placeholder while I figure out how to abuse my power'
		await message.channel.send(response)
		return

	## Checks if command is a stat block command

	stat_block_check = message.content.split()
	if stat_block_check[0].lower() == '!stat' and stat_block_check[1].lower() == 'block':
		choice = stat_block_check[2].capitalize() + '_' + stat_block_check[3].lower()
		await message.channel.send(file = discord.File('images/'+choice+'.png'))
		return

	## Checks if command is a spell command

	with open('spellDictionary.txt', errors='ignore') as file:
		data = file.read()

	spellDict = json.loads(data)

	if message.content.lower().strip('\'') in spellDict:
		response = spellDict[message.content.lower()]
		await message.channel.send(response)
		return

	## Checks if command is an item command

	with open('itemDictionary.txt', errors='ignore') as file2:
		data2 = file2.read()

	itemDict = json.loads(data2)

	if message.content.lower().strip('\'') in itemDict:
		response = itemDict[message.content.lower()]
		await message.channel.send(response)
		return

	## Checks if command is a help command

	if message.content.lower() == '!help':
		response = 'Available commands with correct syntax:\n!roll [number of dice]d[type of die]\n![name of spell or weapon] (if spell has an \' in name, please do not include it) (many weapons have hyphens such as short-sword, ensure that syntax is correct)\n!funny\n!quote'
		await message.channel.send(response)
		return

	## If it is formatted as a command but didn't register earlier send error message

	if message.content[0] == '!':
		response = 'Unknown command, enter \'!help\' for list of commands'
		await message.channel.send(response)
		return

client.run(TOKEN)