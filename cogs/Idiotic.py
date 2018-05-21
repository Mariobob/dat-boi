import discord 
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import io
import sys, traceback
import random
import datetime
import time
import idioticapi


class Idiotic:
    def __init__(self, bot):
        self.bot = bot
        self.token = os.environ.get("IDIOTICAPI")
        self.client = idioticapi.Client(self.token, dev=True)


    @commands.command()
    async def blame(self, ctx, *, text=None):
        """Blame someone"""
        try:
            await ctx.send(file=discord.File(await self.client.blame(str(text)), "blame.png"))
        except Exception as e:
            await ctx.send(f"An error occured with the API. \nMore details: \n{e}")
            
            
    @commands.command()
    async def gay(self, ctx, user: discord.Member = None):
        """Someone is gay"""
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(file=discord.File(await self.client.rainbow(user.avatar_url), "gay.png"))
        except Exception as e:
            await ctx.send(f"An error occured with the API. \nMore details: \n{e}")
           
        
    @commands.command()
    async def triggered(self, ctx, user: discord.Member = None):
        """Someone is triggered."""
        await ctx.trigger_typing()
        user = user if user is not None else ctx.author
        try:
            await ctx.send(file=discord.File(await self.client.triggered(av), "triggered.gif"))
        except Exception as e:
            await ctx.send(f"An error occured with the API. \nMore details: \n{e}")
        
            
def setup(bot):
    bot.add_cog(Idiotic(bot))
