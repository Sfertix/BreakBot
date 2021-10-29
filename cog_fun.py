import urllib.request
import json
import random
import discord

from colorama import init, Fore
from discord.ext import commands
from blagues_api import BlaguesAPI, BlagueType
from discord.ext.commands import BucketType

# Colorama automatisation
init(autoreset=True)


def setup(bot):
    bot.add_cog(CommandeFUN(bot))


def searchJoke(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, 'TOKEN': "8G4CcEJd0rtLLjd8AMLCUDQOverb8EDKLt2vcSFxdZAyFmcdxy5KNQdFW6aa", }
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    return json.load(response)


async def ErrorGestionnaryJoke(ctx, data):
    await ctx.send(
        embed=discord.Embed(
            title=f"<:erreur:875475117566734399> Erreur J0KE#{data['status']} ({data['message']})",
            description="Merci de contacter le support en indiquant le code ci-dessus",
            color=discord.Colour.red()))


"""Possibilité de réponses Alea"""
possibility_reponse = ["Oui", "Mouais", "Bien sûr", "Yup", "Vaut mieux que je rép pas",
                       "La réponse est dans la question",
                       "Sans blague : OUI", "Sans blague : NON",
                       "Euh", "Disons que... Bah...", "...", "As-tu besoin d'une robote pour te rep ?",
                       "Je suis un robot, je ne peut pas te blesser",
                       "Je m'en tape le code par terre", "La vérité blesse, le mensonge préserve",
                       "Tu me prends pour qui ? Tu crois que je sais tout ?",
                       "Non", "Je préfère pas rép, sinon Sfertix va encore me débrancher", "T'as trop cru",
                       "Pour une réponse : appelle Sidoréla ||C'est con elle est plus là||"
                       "Je pense que tu devrais continuer ton chemin"]

blagues_api_token = BlaguesAPI(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNDMwNzY0MTUyNTQyNDYxOTUyIiwibGltaXQiOjEwMCwia2V5IjoiU1BDeEVpdEJXczlhQ2RacmFGSlh6azBnclFGUVRhcGxRaG5ZY3ViV3FZNXdYdmZHRk8iLCJjcmVhdGVkX2F0IjoiMjAyMS0wOC0xNFQyMTo0NzowNCswMDowMCIsImlhdCI6MTYyODk3NzYyNH0.puaUiMfnSuGoYLrHoz-jjNo-9VA0XrLE7Lxfwn9k53k")


class CommandeFUN(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(alliases=["8ball"])
    @commands.cooldown(1, 5, BucketType.user)
    async def alea(self, ctx, *, question=None):

        if question is None:

            miss_args_embed = discord.Embed(
                description='<:missing_args:876022317963153418> **Il faut préciser une question**',
                color=discord.Colour.green(),
            )


            await ctx.send(embed=miss_args_embed)

        elif len(question) > 200:

            so_long_ask_embed = discord.Embed(
                description=f"<:missing_args:876022317963153418> **Ta question doit faire moins de 200 caractères __({len(question)}/200)__**",
                color=discord.Colour.green())

            await ctx.send(embed=so_long_ask_embed)

        else:
            embed = discord.Embed(title="<:shuffle:791714947137536024> **Réponse aléatoire**",
                                  description="Poses moi tes questions et je te réponderai", color=0x1BD2AE)
            embed.add_field(name="__Question :__", value=question)
            embed.add_field(name="__Ma réponse :__", value=random.choice(possibility_reponse), inline=False)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/791259869339713556/792780534476570684/searching.png")
            embed.set_footer(text=f"Pour {ctx.author}")

            await ctx.send(embed=embed)

    @commands.command(aliases=["joketype"])
    async def joketypes(self, ctx):
        type_joke_embed = discord.Embed(title="Voici les différents commandes disponibles :", colour=0xFFF300)
        type_joke_embed.add_field(name="Types :",
                                  value="- `blague (global/dev/dark/limit/beauf/blondes)` : Blague basique aléatoire (ou catégorisé)\n"
                                        "- `memes` : Mème Tweeter/GarsVsFilles\n"
                                        "- `devinette` : Devinette\n"
                                        "- `disquette` : Phrase de dragueur")
        type_joke_embed.set_footer(text="API : ©J0KE • ©BlaguesAPI")
        await ctx.send(embed=type_joke_embed)

    @commands.command(aliases=["joke", "blagues"])
    async def blague(self, ctx, asked=None):
        if asked in ["global", "globale", "globales"]:
            blague = await blagues_api_token.random_categorized(BlagueType.GLOBAL)

        elif asked == "dev":
            blague = await blagues_api_token.random_categorized(BlagueType.DEV)

        elif asked in ["dark", "noire", "noires"]:
            blague = await blagues_api_token.random_categorized(BlagueType.DARK)

        elif asked in ["limit", "limite", "limites"]:
            blague = await blagues_api_token.random_categorized(BlagueType.LIMIT)

        elif asked in ["beauf", "beaufs"]:
            blague = await blagues_api_token.random_categorized(BlagueType.BEAUF)

        elif asked in ["blondes", "blonde"]:
            blague = await blagues_api_token.random_categorized(BlagueType.BLONDES)

        else:
            blague = await blagues_api_token.random()
            asked = "aléatoire"

        blague_embed = discord.Embed(title=f":joy: Blague {blague.type} #{blague.id}",
                                     description=f"{blague.joke}\n||{blague.answer}||", colour=discord.Colour.purple())
        blague_embed.set_footer(text=f"Type demandé : {asked}")

        await ctx.send(embed=blague_embed)

    @blague.error
    async def on_command_error(self, ctx, error):
        print(f"{Fore.RED}[BlaguesError] (user : {ctx.author}) {error}")

        await ctx.send(
            embed=discord.Embed(
                title="<:bugs:881640794858078318> Incident !",
                color=discord.Colour.red(),
                description="Merci de contacter le support car cette erreur n'est pas habituelle",
            )
        )

    @commands.command()
    async def memes(self, ctx):
        url = random.choice(["https://j0ke.xyz/api/garsvsfilles", "https://j0ke.xyz/api/tweet"])
        data = searchJoke(url)

        if data["status"] == 200:
            gvf_embed = discord.Embed(title=f"Memes #{data['id']}", color=0x7400FF)
            gvf_embed.set_image(url=data['url'])
            await ctx.send(embed=gvf_embed)

        else:
            await ErrorGestionnaryJoke(ctx, data)

    @commands.command()
    async def devinette(self, ctx):
        url = "https://j0ke.xyz/api/riddle"
        data = searchJoke(url)

        if data['status'] == 200:
            riddle_embed = discord.Embed(title=f"Devinette #{data['id']}", color=0xFF0051,
                                         description=f"{data['riddle']}\n||{data['answer']}||")
            await ctx.send(embed=riddle_embed)

        else:
            await ErrorGestionnaryJoke(ctx, data)

    @commands.command()
    async def disquette(self, ctx):
        url = "https://j0ke.xyz/api/disquette"
        data = searchJoke(url)

        if data['status'] == 200:
            disquette_embed = discord.Embed(title=f"Disquette #{data['id']}", color=0xFF7400,
                                            description=f"**{data['disquette']}**")
            await ctx.send(embed=disquette_embed)

        else:
            await ErrorGestionnaryJoke(ctx, data)
