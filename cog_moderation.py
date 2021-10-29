import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(ModerationExt(bot))


class ModerationExt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=None):
        await ctx.message.delete()

        bad_args_em = discord.Embed(title="<:erreur:875475117566734399> Il y a un souci !",
                                    color=discord.Colour.red(),
                                    description="Tu dois saisir une valeur numérique, située entre 1 et "
                                                "100 (compris).\n"
                                                "`b!clear [nombre]`")

        if amount is None or not amount.isdigit():
            await ctx.send(embed=bad_args_em, delete_after=10)
            return

        amount = int(amount)

        if 0 < amount < 101:
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=discord.Embed(title=f"💩 {amount} messages supprimés.", color=0xBF9055),
                           delete_after=5)

        else:
            await ctx.send(embed=bad_args_em, delete_after=10)

    @clear.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(title="<:erreur:875475117566734399> Permissions !", color=discord.Colour.red(),
                                               description="Il te manque la permission de ***`GÉRER LES MESSAGES`***"),
                           delete_after=10)

        else:
            print(f"Commande Clear : {error}")
            await ctx.send("<:erreur:875475117566734399> Je sais pas ce qu'il se passe !!!", delete_after=10)