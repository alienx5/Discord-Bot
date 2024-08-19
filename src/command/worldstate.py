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

                response =f"Today Darvo is selling {item} for {sale}p, original price: {price}p."
            else:
                response = "Sorry operator, I am having trouble accessing this information."
        else:
            response = "Darvo is not currently available."

        await ctx.send(response)

    @commands.command(name = 'cetus', help = 'Displays the current state in Cetus and the time remaining.')
    async def cetus_state(self, ctx):
        url = base_url + '/cetusCycle'
        cetus = get(url).json()

        if 'error' in cetus:
            response = "I am having trouble contacting Konzu operator."
        else:
            state = cetus['state']
            time_left = cetus['timeLeft']

            if state == 'night':
                response = f"It is currently {state} in Cetus for {time_left}. Happy Eidolon hunting operator!"
            else:
                reponse = f"It is currently {state} in Cetus for {time_left}."
        
        await ctx.send(response)

    @commands.command(name = 'fortuna', help = 'Displays the current state in the Orb Vallis and the time remaining.')
    async def fortuna_state(self, ctx):
        url = base_url + '/vallisCycle'
        fortuna = get(url).json()

        if 'error' in fortuna:
            response = "I am having trouble contacting Eudico operator."
        else:
            state = fortuna['isWarm']
            time_left = fortuna['timeLeft']

            if state == True:
                response = f"It is currently warm in the Orb Vallis for {time_left}."
            else:
                response = f"It is currently cold in the Orb Vallis for {time_left}."
        
        await ctx.send(response)

    @commands.command(name = 'deimos', help = 'Displays the current state in the Cambion Drift and the time remaining.')
    async def deimos_state(self, ctx):
        url = base_url + '/cambionCycle'
        deimos = get(url).json()

        if 'error' in deimos:
            response = "I am having trouble contacting Mother operator."
        else:
            state = deimos['state']
            time_left = deimos['timeLeft']

            response = f"It is currently {state} in the Cambion Drift for {time_left}"

        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(WorldState(bot))
    return