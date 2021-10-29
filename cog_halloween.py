import datetime
import json

import discord
import random

from discord.ext import commands
from discord.ext.commands import BucketType


def setup(bot):
    bot.add_cog(CommandeHALLOWEEN(bot))


class CommandeHALLOWEEN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # 1635616800

    @commands.command(name="bonbons")
    @commands.cooldown(1, 120, BucketType.user)
    async def bonbons(self, ctx):
        user_id = str(ctx.author.id)
        candy = random.choice(range(1, 11))
        ghost = random.choice(range(5))

        if ghost == 0:
            await ctx.send(embed=discord.Embed(title="<:HW_citrouille:902276073155334234> Évènement d'Halloween",
                                               description="<:HW_fantome:902276069804085248> Tu ne recevras aucuns bonbons",
                                               colour=0xFF4600))

            with open("halloween_candy.json") as f:
                data = json.load(f)

            data["pot"] += candy

        else:
            await ctx.send(embed=discord.Embed(title="<:HW_citrouille:902276073155334234> Évènement d'Halloween",
                                               description=f"<:HW_bonbons:902276072995971122> Tu as gagné {candy} bonbons dans cette maison !",
                                               colour=0xFF4600))

            with open("halloween_candy.json") as f:
                data = json.load(f)

            # ZONE EVENEMENT : MENICA
            if ctx.guild.id == 831294285793853440 and 1635616800 < datetime.datetime.timestamp(
                    datetime.datetime.now()) < 1635724800:
                print('ok')

                ratio = data["menica_event"]

                search = False

                for user in ratio.keys():
                    if user == user_id:
                        ratio[user_id] += candy
                        search = True

                if not search:
                    ratio[user_id] = candy
            # ZONE EVENEMENT : MENICA

            ratio = data["user_candy"]

            search = False

            for user in ratio.keys():
                if user == user_id:
                    ratio[user_id] += candy
                    search = True

            if not search:
                ratio[user_id] = candy

        with open("halloween_candy.json", "w") as fp:
            json.dump(data, fp)

    @bonbons.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=discord.Embed(title="<:HW_citrouille:902276073155334234> Impossible...",
                                               description=f"<:HW_fantome:902276069804085248> Tu dois attendre `{error.retry_after:.0f}` secondes",
                                               color=0xFF4600))

    @commands.command(name="sachet")
    async def sachet(self, ctx):
        with open("halloween_candy.json") as f:
            data = json.load(f)

        inventary = data["user_candy"]
        user = str(ctx.author.id)

        try:
            await ctx.send(
                embed=discord.Embed(title=f"<:HW_sachet:902276066142474300> Tu as {inventary[user]} bonbons !",
                                    color=0xFF4600))
        except:
            await ctx.send(embed=discord.Embed(title="<:HW_sachet:902276066142474300> Tu n'as pas encore de bonbons !",
                                               color=0xFF4600))

    @commands.command(name="ldb")
    async def leaderboard(self, ctx):
        with open("halloween_candy.json") as f:
            data = json.load(f)

        ratio = data["user_candy"]
        ordonned_ratio = sorted(ratio.items(), key=lambda t: t[1])

        if not ordonned_ratio[0]:
            ordonned_ratio.append(["N/A", 0])
        if not ordonned_ratio[1]:
            ordonned_ratio.append(["N/A", 0])
        if not ordonned_ratio[2]:
            ordonned_ratio.append(["N/A", 0])

        await ctx.send(embed=discord.Embed(title="<:HW_citrouille:902276073155334234> Le podium générale",
                                           description=f"1er : <@{ordonned_ratio[-1][0]}> ({ordonned_ratio[-1][1]} bonbons)\n"
                                                       f"2ème : <@{ordonned_ratio[-2][0]}> ({ordonned_ratio[-2][1]} bonbons)\n"
                                                       f"3ème : <@{ordonned_ratio[-3][0]}> ({ordonned_ratio[-3][1]} bonbons)\n\n",
                                           colour=0xFF4600))

    @commands.command()
    async def menica_ldb(self, ctx):
        with open("halloween_candy.json") as f:
            data = json.load(f)

        ratio = data["menica_event"]
        ordonned_ratio = sorted(ratio.items(), key=lambda t: t[1])

        menica_ldb = discord.Embed(title="<:HW_citrouille:902276073155334234> Le podium Ménica",
                                   description=f"1er : <@{ordonned_ratio[-1][0]}> ({ordonned_ratio[-1][1]} bonbons)\n"
                                               f"2ème : <@{ordonned_ratio[-2][0]}> ({ordonned_ratio[-2][1]} bonbons)\n"
                                               f"3ème : <@{ordonned_ratio[-3][0]}> ({ordonned_ratio[-3][1]} bonbons)\n\n",
                                   colour=0xFF4600)
        menica_ldb.set_footer(text="<@N/A> : Aucun joueur à affiché")
        await ctx.send(embed=menica_ldb)
