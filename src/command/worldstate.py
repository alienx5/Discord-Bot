from requests import get
import discord
from discord.ext import commands

base_url = "https://api.warframestat.us/pc"

class WorldState(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'Darvo Deals', help = 'Displays the current deal that Darvo is hosting.')
    async def darvo_deal(self, ctx):
        url = base_url + '/dailyDeals'
        deal = get(url).json()

        item = deal['item']
        price = deal['originalPrice']
        sale = deal['salePrice']

        response = "Today Darvo is selling " + item + " for " + sale + ", original price: " + price
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(WorldState(bot))
    return