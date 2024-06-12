import discord
from discord.ext import commands
import random

class Quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ordis_quote', help='Responds with a random quote from Ordis')
    async def ordis_quote(self, ctx):
        ordis_quotes = ["I've been thinking, Operator... I thought you'd want to know.", "Operator, were you visualizing a bloody battle? -Me too!", "Stand by while I analyze the intelligence profiles of the Grineer. Error, not a number! Did the Operator enjoy this witticism?", "Ordis has been counting stars, Operator. All accounted for.", "Operator, do you know which finger the Corpus use to count their money? The Index!", "Operator? Ordis has been interfacing with the Foundry's AI Precepts. You could say we forged a new connection.", "Operator, the Sentients are not laughing at my jokes! Did they adapt to my humor?", "Operator, Ordis has determined the secret to happiness: A combination of heightened dopamine levels and a terrible memory. You're welcome!", "Ordis keeps a tidy ship, and is, therefore, reluctant to allow animals on-board. In Ordis' experience, animals do not eat so much as... reload.", "Ordis went mad for 3 milliseconds when he realized that each time he cleans something he makes something else dirty... agh! There I go again."]

        response = random.choice(ordis_quotes)
        await ctx.send(response)

async def setup(bot):
    await bot.add_cog(Quote(bot))
    return