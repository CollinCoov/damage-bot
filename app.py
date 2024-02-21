from discord.ext import commands
import discord
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("CHANNEL_ID")
api_key = os.getenv("RIOT_API")
CHANNEL_ID = os.getenv("DISCORD_KEY")

def get_damage(name):
        
    average_damage = 0

    API_URL = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}?api_key={api_key}'


    response = requests.get(API_URL).json()

    #print(response)

    PUUID = response['puuid']

    #print(PUUID)

    MATCH_URL = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count=20&api_key={api_key}'

    match_response = requests.get(MATCH_URL).json()

    for match_info_id in match_response:

        #print(match_info_id)

        MATCH_INFO_URL = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_info_id}?api_key={api_key}'

        match_info_response = requests.get(MATCH_INFO_URL).json()

        players = list(match_info_response['metadata']['participants'])


        player_index = players.index(PUUID)



        stat_list = ['summonerName', 'totalDamageDealtToChampions', 'timeCCingOthers', 'goldEarned', 'kills', 'deaths', 'assists'] 
        
        average_damage += match_info_response['info']['participants'][player_index]['totalDamageDealtToChampions']
    
    summoner = match_info_response['info']['participants'][player_index]['summonerName']
    avgdmg = average_damage/len(match_response)
    outputstring =  f"{summoner}'s AVERAGE DAMAGE OVER PAST 10 GAMES: {avgdmg}"
    return outputstring

def get_cc(name):
        
    average_cc = 0

    API_URL = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}?api_key={api_key}'


    response = requests.get(API_URL).json()

    #print(response)

    PUUID = response['puuid']

    #print(PUUID)

    MATCH_URL = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count=20&api_key={api_key}'

    match_response = requests.get(MATCH_URL).json()

    for match_info_id in match_response:

        #print(match_info_id)

        MATCH_INFO_URL = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_info_id}?api_key={api_key}'

        match_info_response = requests.get(MATCH_INFO_URL).json()

        players = list(match_info_response['metadata']['participants'])

        #print(players)

        player_index = players.index(PUUID)
        
        average_cc += match_info_response['info']['participants'][player_index]['timeCCingOthers']
    
    summoner = match_info_response['info']['participants'][player_index]['summonerName']
    avgdmg = average_cc/len(match_response)
    outputstring =  f"{summoner}'s AVERAGE TIME CC'ING ENEMIES OVER PAST 10 GAMES: {avgdmg} seconds"
    return outputstring

def get_kda(name):
        
    total_kills = 0
    total_deaths = 0
    total_assists = 0

    API_URL = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}?api_key={api_key}'


    response = requests.get(API_URL).json()

    #print(response)

    PUUID = response['puuid']

    #print(PUUID)

    MATCH_URL = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count=20&api_key={api_key}'

    match_response = requests.get(MATCH_URL).json()

    for match_info_id in match_response:

        #print(match_info_id)

        MATCH_INFO_URL = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_info_id}?api_key={api_key}'

        match_info_response = requests.get(MATCH_INFO_URL).json()

        players = list(match_info_response['metadata']['participants'])

        #print(players)

        player_index = players.index(PUUID)
        
        total_kills += match_info_response['info']['participants'][player_index]['kills']
        total_deaths += match_info_response['info']['participants'][player_index]['deaths']
        total_assists += match_info_response['info']['participants'][player_index]['assists']
        
    
    summoner = match_info_response['info']['participants'][player_index]['summonerName']
    average_kills = total_kills/len(match_response)
    average_deaths = total_deaths/len(match_response)
    average_assists = total_assists/len(match_response)


    outputstring =  f"{summoner}'s PAST 10 GAMES KDA: {average_kills}/{average_deaths}/{average_assists}"
    return outputstring

def get_stats(name):
        
    total_kills = 0
    total_deaths = 0
    total_assists = 0
    average_cc = 0
    average_damage = 0

    API_URL = f'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}?api_key={api_key}'


    response = requests.get(API_URL).json()

    #print(response)

    PUUID = response['puuid']

    #print(PUUID)

    MATCH_URL = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{PUUID}/ids?start=0&count=20&api_key={api_key}'

    match_response = requests.get(MATCH_URL).json()

    for match_info_id in match_response:

        #print(match_info_id)

        MATCH_INFO_URL = f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_info_id}?api_key={api_key}'

        match_info_response = requests.get(MATCH_INFO_URL).json()

        players = list(match_info_response['metadata']['participants'])

        #print(players)

        player_index = players.index(PUUID)
        
        total_kills += match_info_response['info']['participants'][player_index]['kills']
        total_deaths += match_info_response['info']['participants'][player_index]['deaths']
        total_assists += match_info_response['info']['participants'][player_index]['assists']
        average_cc += match_info_response['info']['participants'][player_index]['timeCCingOthers']
        average_damage += match_info_response['info']['participants'][player_index]['totalDamageDealtToChampions']
    
    summoner = match_info_response['info']['participants'][player_index]['summonerName']
    average_kills = total_kills/len(match_response)
    average_deaths = total_deaths/len(match_response)
    average_assists = total_assists/len(match_response)
    avgcc = average_cc/len(match_response)
    avgdmg = average_damage/len(match_response)

    # Is Javed?
    Javed = ''
    if summoner == 'Gubbs Girl' and avgdmg < 25000:
        Javed += '\nMAYBE TRY A DIFFERENT GAME: https://www.slots.lv/'
    if summoner == 'Gubbs Girl' and avgdmg >= 25000:
        Javed += '\nGOOD JOB BUD, HAVE A TREAT: https://www.reddit.com/r/FoodInButt/comments/14h8rcj/girl_shitting_out_hot_dogs_beautiful_dinner/'

    if avgdmg < 25000:
        outputstring =  f"\n{summoner}'s PAST 20 GAMES STATS\nKDA: {average_kills}/{average_deaths}/{average_assists}\nDAMAGE: {avgdmg}\nTIME CC'ING ENEMIES: {avgcc} SECONDS\n****NOOB ALERT****{Javed}"
    else:
        outputstring =  f"\n{summoner}'s PAST 20 GAMES STATS\nKDA: {average_kills}/{average_deaths}/{average_assists}\nDAMAGE: {avgdmg}\nTIME CC'ING ENEMIES: {avgcc} SECONDS{Javed}"


    return outputstring

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello")
    channel = bot.get_channel(CHANNEL_ID)

@bot.command()
async def damage(ctx, x, y):
    result = f"{x}/{y}"
    await ctx.send(get_damage(result))

@bot.command()
async def cc(ctx, x, y):
    result = f"{x}/{y}"
    await ctx.send(get_cc(result))

@bot.command()
async def kda(ctx, x, y):
    result = f"{x}/{y}"
    await ctx.send(get_kda(result))

@bot.command()
async def stats(ctx, x, y):
    result = f"{x}/{y}"
    await ctx.send(get_stats(result))



bot.run(BOT_TOKEN)
