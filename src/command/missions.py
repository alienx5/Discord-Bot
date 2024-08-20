from requests import get
import discord
from discord.ext import commands

base_url = "https://api.warframestat.us/pc"

class Missions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'archon_hunt', help = 'Displays the current Arbitration mission with the buffed warframe and weapons')
    async def archon_hunt(self, ctx):
        url = base_url + '/archonHunt'
        hunt = get(url).json

        mission_list = hunt['missions']
        archon = hunt['boss']
        time_left = hunt['eta']

        mission1 = mission_list[0]
        mission2 = mission_list[1]
        mission3 = mission_list[2]

        ##TODO add embed to display information about each mission and the boss