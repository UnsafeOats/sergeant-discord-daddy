from discord.ext import commands
from utils import and_includes, or_includes
import random


class Creeper(commands.Cog):
    """
    Creeper just peeps messages and responds with group in-jokes
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if and_includes(message.content, "thanks", "sar'nt"):
            # Responds to "thanks" and "sar'nt" in the same message
            await message.channel.send(
                "No problemo buckaroo."
            )

        if or_includes(message.content, "army", "west point") and (
            random.random() < 0.33
        ):
            # You know what this does
            await message.channel.send("Hooah.")

        if or_includes(message.content, "navy", "naval academy") and (
            random.random() < 0.33
        ):
            # You know what this does
            await message.channel.send("Hoooyah.")

        if or_includes(message.content, "airforce", "air force", "air force academy") and (
            random.random() < 0.33
        ):
            # You know what this does
            await message.channel.send("Hmmph.")

        if or_includes(message.content, "usmc", "marines", "naval academy") and (
            random.random() < 0.33
        ):
            # You know what this does
            await message.channel.send("Oorah.")
