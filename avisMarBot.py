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

	if len(message.attachments) > 0:
		return
	
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

	if message.content.lower() == '!scrying table':
		await message.channel.send(file = discord.File('images/Scrying_table.png'))
		return

	if message.content.lower() == '!control weather table':
		await message.channel.send(file = discord.File('images/Control_weather_table.png'))
		return

	if message.content.lower() == '!reincarnate table':
		await message.channel.send(file = discord.File('images/Reincarnate_table.png'))
		return

	if message.content.lower() == '!generate character':
		raceList = []
		raceListWeights = []
		backgroundList = []
		backgroundListWeights = []
		classAndSubclassList = []
		with open('raceList.txt', errors='Ignore') as file3:
			for line in file3:
				line = line.replace('\"', '')
				line = line.replace('\n', '')
				line = line.replace(',', '')
				raceList.append(line)
		with open('raceListWeights.txt', errors='Ignore') as file4:
			for line in file4:
				line = line.replace('\n', '')
				line = line.replace(',', '')
				raceListWeights.append(float(line))
		with open('backgroundList.txt', errors='Ignore') as file5:
			for line in file5:
				line = line.replace('\"', '')
				line = line.replace('\n', '')
				line = line.replace(',', '')
				backgroundList.append(line)
		with open('backgroundListWeights.txt', errors='Ignore') as file6:
			for line in file6:
				line = line.replace('\n', '')
				line = line.replace(',', '')
				backgroundListWeights.append(float(line))
		with open('classAndSubclassList.txt', errors='Ignore') as file7:
			for line in file7:
				line = line.replace('\"', '')
				line = line.replace('\n', '')
				line = line.replace(',', '')
				classAndSubclassList.append(line)
		race = random.choices(raceList, raceListWeights)
		background = random.choices(backgroundList, backgroundListWeights)
		classAndSubclass = random.choices(classAndSubclassList)
		response = 'Race: '+race[0]+', Class: '+classAndSubclass[0]+', Background: '+background[0]
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

	spellCheck = message.content.lower().replace('\'', '')

	if spellCheck in spellDict:
		response = spellDict[spellCheck]
		await message.channel.send(response)
		return

	## Checks if command is an item command

	with open('itemDictionary.txt', errors='ignore') as file2:
		data2 = file2.read()

	itemDict = json.loads(data2)

	itemCheck = message.content.lower().replace('\'', '')

	if itemCheck in itemDict:
		response = itemDict[itemCheck]
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