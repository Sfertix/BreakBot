import asyncio
import os.path
import discord
import datetime

import youtube_dl
from colorama import init, Fore
from discord.ext import commands, tasks

bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or("b!"), intents=discord.Intents.all(),
                              case_insensitive=True)

bot.remove_command("help")

cog_list = ["cog_fun", "cog_help", "cog_moderation", "cog_halloween"]

# Colorama automatisation
init(autoreset=True)


def manage_cog(manage=None):
    message_status = ""

    for cog in cog_list:

        try:
            if manage == "load":
                bot.load_extension(cog)
                print(f"\t{Fore.GREEN}[BreakBot Cogs] {cog} chargée")
                message_status += f"<:yes:732621196889161758> : `{cog}` chargée\n"

            elif manage == "reload":
                bot.reload_extension(cog)
                print(f"\t{Fore.GREEN}[BreakBot Cogs] {cog} rechargée")
                message_status += f"<:yes:732621196889161758> : `{cog}` rechargée\n"

            elif manage == "unload":
                bot.unload_extension(cog)
                print(f"\t{Fore.GREEN}[BreakBot Cogs] {cog} déchargée")
                message_status += f"<:yes:732621196889161758> : `{cog}` déchargée\n"

        except commands.ExtensionNotFound:
            print(f"\t{Fore.RED}[BreakBot Cogs] {cog} introuvable")
            message_status += f"<:nop:732621196838830170> : `{cog}` introuvable\n"

        except commands.ExtensionAlreadyLoaded:
            print(f"\t{Fore.YELLOW}[BreakBot Cogs] {cog} déjà chargée")
            message_status += f"⚠ : `{cog}` déjà chargée\n"

        except commands.ExtensionNotLoaded:
            print(f"\t{Fore.YELLOW}[BreakBot Cogs] {cog} n'est pas chargée")
            message_status += f"⚠ : `{cog}` n'est pas chargée\n"

        except commands.ExtensionError as e:
            print(f"\t{Fore.RED}[BreakBot Cogs] Un problème est survenue : {cog} ({e})")
            message_status += f"<:nop:732621196838830170> : `{cog}` erreur (voir console)\n"

    return message_status


async def statistics_counter():
    guilds_count = 0
    members_count = 0

    async for server in bot.fetch_guilds(limit=100):
        guilds_count += 1

        guild = bot.get_guild(server.id)
        members_count += guild.member_count

    guild_count_channel = bot.get_channel(884906488433352704)
    await guild_count_channel.edit(name=f"『🧮』Serveurs : {guilds_count}",
                                   reason="Mise à jour du salon statistique : Serveur")

    member_count_channel = bot.get_channel(884908774425493514)
    await member_count_channel.edit(name=f"『👥』Utilisateurs : {members_count}",
                                    reason="Mise à jour du salon statistique : Membres")


# Quand le bot est prêt
@bot.event
async def on_ready():
    # Chargement des cogs
    manage_cog(manage="load")

    # Status + Shard
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("b!help / v1.2.2"))
    print(f"\nNombre de Shard : {bot.shard_count}")

    # Lancement de la tâche AutoUpdateStatistics
    AutoUpdateStatistics.start()

    # Supprime les fichiers .mp3
    for file in os.listdir("./"):
        if file.endswith('.mp3'):
            os.remove(file)

    # Chargement du bot complet
    print("[BreakBot] est prêt à être utilisé.")
    print("\n\n#---------------#\n\n")

    # Stats
    await statistics_counter()


@bot.event
async def on_guild_join(guild):
    server_join_embed = discord.Embed(title="<:nv:881640186046476318> **Nouveau serveur !**",
                                      color=discord.Colour.green(),
                                      timestamp=datetime.datetime.utcnow())
    server_join_embed.set_thumbnail(url=guild.icon_url)
    server_join_embed.add_field(name="Nom", value=f"{guild.name} (Id : {guild.id})")
    server_join_embed.add_field(name="Propriétaire", value=f"{guild.owner}", inline=False)
    server_join_embed.add_field(name="Membres", value=f"{guild.member_count}", inline=True)

    channel = bot.get_channel(859545865831841803)
    await channel.send(embed=server_join_embed)

    for general in guild.text_channels:
        if general and general.permissions_for(guild.me).send_messages:
            introduction_embed = discord.Embed(title="Break :wave:", color=0x33F8EF,
                                               description="Bonjour à toi, je suis <@711856781311344711>.\n"
                                                           "Je ne suis disponible qu'en français :flag_fr: (pour le moment :wink:).\n\n"
                                                           "Je pense être assez simple à utiliser et toutes mes commandes sont visibles avec `b!help` ou sur ["
                                                           "cette page](https://docs.sfertix.fr). Mon préfix est `b!` et je suis mentionnable.\n"
                                                           "Toutes __suggestions d'améliorations__ sont acceptés en rejoignant le serveur [support](https://discord.gg/ZYN5SE3vgB)\n\n"
                                                           "**Les commandes `b!faq` sont à votre service pour vous orienté et vous aider sur mon utilisation.**")

            await general.send(embed=introduction_embed)
        return

    await statistics_counter()


@bot.event
async def on_guild_remove(guild):
    leave_server_embed = discord.Embed(title="<:del:881640185878708285> **Serveur supprimé**",
                                       color=discord.Colour.red(),
                                       timestamp=datetime.datetime.utcnow(),
                                       description=f"On m'a éjecté de : `{guild}`\n\n"
                                                   f"**__Id :__** {guild.id}\n"
                                                   f"**__Membres :__** {guild.member_count}")

    channel = bot.get_channel(859545865831841803)
    await channel.send(embed=leave_server_embed)
    await statistics_counter()


@tasks.loop(hours=1)
async def AutoUpdateStatistics():
    await statistics_counter()


@bot.command()
@commands.is_owner()
async def maj(ctx, action=None):
    await ctx.message.delete()

    if action == "load":
        print("\n\n#---------------#\n\n")
        print("[BreakBot] Démarrage des cogs...")

        status_cogs = manage_cog(manage="load")

        print("\n[BreakBot] Démarrage effectué !")
        print("\n\n#---------------#\n\n")

        status_embed = discord.Embed(title="<:reload:881833874223669249> Chargement des cogs",
                                     description=status_cogs, colour=discord.Colour.gold(),
                                     timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=status_embed, delete_after=10)

    elif action == "reload":
        print("\n\n#---------------#\n\n")
        print("[BreakBot] Redémarrage des cogs...")

        status_cogs = manage_cog(manage="reload")

        print("\n[BreakBot] Redémarrage effectué !")
        print("\n\n#---------------#\n\n")

        status_embed = discord.Embed(title="<:reload:881833874223669249> Rechargement des cogs",
                                     description=status_cogs, colour=discord.Colour.gold(),
                                     timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=status_embed, delete_after=10)

    elif action == "unload":
        print("\n\n#---------------#\n\n")
        print("[BreakBot] Arrêt des cogs...")

        status_cogs = manage_cog(manage="unload")

        print("\n[BreakBot] Arrêt effectué !")
        print("\n\n#---------------#\n\n")

        status_embed = discord.Embed(title="<:reload:881833874223669249> Déchargement des cogs",
                                     description=status_cogs, colour=discord.Colour.gold(),
                                     timestamp=datetime.datetime.utcnow())
        await ctx.send(embed=status_embed, delete_after=10)


@maj.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        await ctx.send(embed=discord.Embed(title="👑 Mon codeur uniquement peut utiliser cette commande",
                                           colour=discord.Colour.gold()))


server_music_start = []
musics = {}


def running_music(ctx, queue, url):
    song_there = os.path.isfile(f"./music_cache/{ctx.guild.id}_song.mp3")

    if song_there:
        os.remove(f"./music_cache/{ctx.guild.id}_song.mp3")

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir("./"):
        try:
            if file.endswith('.mp3'):
                if file.title not in server_music_start:
                    os.rename(file, f'./music_cache/{ctx.guild.id}_song.mp3')
                    server_music_start.append(f"{ctx.guild.id}_song.mp3")

        except PermissionError:
            continue

    def next_song(_):
        if len(queue) > 0:
            new_song = queue[0]
            del queue[0]

            running_music(ctx, queue, new_song)

        # Si il n'y en a pas alors le bot est déconnecté
        else:
            asyncio.run_coroutine_threadsafe(voice.disconnect(), bot.loop)
            os.remove(f"./music_cache/{ctx.guild.id}_song.mp3")
            del server_music_start[server_music_start.index(f"{ctx.guild.id}_song.mp3")]
            return

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio(f'./music_cache/{ctx.guild.id}_song.mp3'), after=next_song)


@bot.command()
async def play(ctx, url=None):
    client = ctx.guild.voice_client

    # Si le membre n'est pas connecté dans un salon vocal
    if not ctx.message.author.voice:
        await ctx.send("<:signal:799952661192376330> **Vous n'êtes pas connecté dans un salon vocal**")
        return

    # si pas de lien
    if url is None:
        await ctx.send("<:signal:799952661192376330> **Il faut insérer un lien YouTube")
        return

    # Bot déjà connecté
    if client and client.channel:
        musics[ctx.guild].append(url)
        print(f'{url} : added to the queue')

    # Bot non connecté
    else:
        channel = ctx.author.voice.channel
        musics[ctx.guild] = []
        await channel.connect()

        running_music(ctx, musics[ctx.guild], url)


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("bot isn't connected")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing:
        voice.pause()
    else:
        await ctx.send("Déjà en pause")


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Déjà en cours")


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


# ping - Affiche les latences du bot
@bot.command()
async def ping(ctx):
    pings = round(bot.latency * 1000)
    print(f"[BreakBot LogPing] Mon ping est de {pings}ms")

    embed_title = "<:wifi:878406210955640842> Temps de réponse :"

    if pings <= 150:
        embed = discord.Embed(title=embed_title, description=f"**{pings}ms** (latences faibles)", color=0x1CE300)

    elif 150 < pings <= 175:
        embed = discord.Embed(title=embed_title, description=f"**{pings}ms** (latences modérées)", color=0xFF9B00)

    elif 175 < pings <= 200:
        embed = discord.Embed(title=embed_title, description=f"**{pings}ms** (latences élevées)", color=0xFF0000)

    else:
        embed = discord.Embed(title=embed_title, color=0x000000, description=f"**{pings}ms** (latences critiques)\n"
                                                                             f"[Contactez le support](https://discord.gg/ZYN5SE3vgB)")

    await ctx.send(embed=embed)


# Token + Start
print("\n\n#---------------#\n\n")
print("[BreakBot] Starting...")
bot.run("NzExODU2NzgxMzExMzQ0NzEx.XsJGSg.UBvcs4lbS8LEf6LfOg1Dz5M3PdE")
