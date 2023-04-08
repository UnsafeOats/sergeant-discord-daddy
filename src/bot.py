import discord
from discord.ext import commands
from bot_appendages.utils import load_paywalls, load_token
from bot_appendages.librarian import Librarian
from bot_appendages.creeper import Creeper


if __name__ == "__main__":
    # local resource loads
    # load paywalled sites
    paywalled_sites = load_paywalls()
    # load bot token
    token = load_token()

    # bot instantiation
    # creates discord bot object (with member intents enabled to grab members)
    intents = discord.Intents.default()
    intents.members = True
    bot = commands.Bot(intents=intents, command_prefix="!", case_insensitive=True)

    # add command cogs to bot
    bot.add_cog(Librarian(paywalled_sites))  # archive is commands and listener
    bot.add_cog(Creeper(bot))  # listen to say weird things
    bot.run(token) # run the bot

