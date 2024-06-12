from requests import get
import discord
from discord.ext import commands

base_url = "https://api.warframestat.us/pc"

class WorldState(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'darvo_deal', help = ':Displays the current deal that Darvo is hosting.')
    async def darvo_deal(self, ctx):
        url = base_url + '/dailyDeals'
        deal = get(url).json()

        if isinstance(deal, list) and len(deal) > 0:
            deal_dict = deal[0]

            if 'item' in deal_dict and 'originalPrice' in deal_dict and 'salePrice' in deal_dict:
                item = deal_dict['item']
                price = deal_dict['originalPrice']
                sale = deal_dict['salePrice']

                response =f"Today Darvo is selling {item} for {sale}, original price: {price}."
            else:
                response = "Sorry operator, I am having trouble accessing this information."
        else:
            response = "Darvo is not currently available."

        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(WorldState(bot))
    return