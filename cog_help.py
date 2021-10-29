import discord
from discord.ext import commands


def setup(bot):
    bot.add_cog(CommandeHelp(bot))


class CommandeHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, command_name=None):
        if command_name is None:
            help_embed = discord.Embed(color=discord.Colour.purple(),
                                       description="[Support](https://discord.gg/ZYN5SE3vgB) • [Documentation](https://docs.break.sfertix.fr) • [Trello](https://trello.com/b/qZwMkCAd) • [Status](https://status.break.sfertix.fr)"
                                                   "\n\nChoisissez la catégorie à afficher : `b!help <catégprie>`\n\n")
            help_embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/748898016651509790/883086601176109116/Copie_de_Coconut_Beach_Summer_Vibes_CD_Cover_Art_-_Fait_avec_PosterMyWall_2.jpg")
            help_embed.add_field(name="<:breakman:881831459994882068> **`break`**",
                                 value="Affiche les commandes globales présentes sur le bot")
            help_embed.add_field(name="<:help_blague:876437812579270676> **`fun`**",
                                 value="Affiche les commandes de la catégorie Blague", inline=False)
            help_embed.add_field(name="<:HW_citrouille:902276073155334234> **`halloween`**",
                                 value="Affiche les commandes de l'évènement halloween", inline=False)
            help_embed.add_field(name="<:help_loterie:876438460146266122> **`lotterie`** - **BIENTÔT**",
                                 value="Préparation des grilles...", inline=False)
            await ctx.send(embed=help_embed)
            return

        elif command_name in ["fun"]:
            faq_joke = discord.Embed(color=discord.Colour.purple(),
                                     description="[Support](https://discord.gg/ZYN5SE3vgB) • [Documentation](https://docs.break.sfertix.fr) • [Trello](https://trello.com/b/qZwMkCAd) • [Status](https://status.break.sfertix.fr)\n\n"
                                                 "Liste : `joketype`, `blague (global/dev/dark/limit/beauf/blondes)`, `memes`, `devinette`, `disquette`")
            faq_joke.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/748898016651509790/883086601176109116/Copie_de_Coconut_Beach_Summer_Vibes_CD_Cover_Art_-_Fait_avec_PosterMyWall_2.jpg")

            await ctx.send(embed=faq_joke)

        elif command_name in ["break"]:
            faq_joke = discord.Embed(color=discord.Colour.purple(),
                                     description="s • [Status](https://status.break.sfertix.fr)\n\n"
                                                 "Liste : `links`, `ping`")
            faq_joke.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/748898016651509790/883086601176109116/Copie_de_Coconut_Beach_Summer_Vibes_CD_Cover_Art_-_Fait_avec_PosterMyWall_2.jpg")

            await ctx.send(embed=faq_joke)

        elif command_name in ["halloween"]:
            hlw_embed = discord.Embed(colour=0xFF4600,
                                      description="[Support](https://discord.gg/ZYN5SE3vgB) • [Documentation](https://docs.break.sfertix.fr) • [Trello](https://trello.com/b/qZwMkCAd) • [Status](https://status.break.sfertix.fr)\n\n"
                                                  "Liste : `bonbons`, `sachet`, `ldb`, `menica_ldb`")
            hlw_embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/748898016651509790/883086601176109116/Copie_de_Coconut_Beach_Summer_Vibes_CD_Cover_Art_-_Fait_avec_PosterMyWall_2.jpg")

            await ctx.send(embed=hlw_embed)

    @commands.command(aliases=['add', 'link', 'liens', 'lien'])
    async def links(self, ctx):
        links_embed = discord.Embed(title="Liens :", color=discord.Colour.purple(),
                                    description="Pour ajouter BreakBot et l'utiliser à fond sur ton serveur Discord "
                                                "tu dois cliquer [ICI]("
                                                "https://discord.com/api/oauth2/authorize?client_id"
                                                "=711856781311344711&permissions=8&redirect_uri=https%3A%2F%2Fdiscord"
                                                ".com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D711856781311344711"
                                                "%26permissions%3D8%26redirect_uri%3Dhttps%253A%252F%252Fdiscord.com"
                                                "%252Fapi%252Foauth2%252Fauthorize%253Fclient_id%253D711856&scope=bot"
                                                "%20applications.commands).")
        links_embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/748898016651509790/883086601176109116'
                                      '/Copie_de_Coconut_Beach_Summer_Vibes_CD_Cover_Art_-_Fait_avec_PosterMyWall_2'
                                      '.jpg')
        await ctx.send(embed=links_embed)
