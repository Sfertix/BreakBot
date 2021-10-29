# Embed for Welcome
import datetime
import discord

"""Message du règlement RPG"""
embed_one_welcome = discord.Embed(title="Bienvenue !", color=0x25FF98,
                                  description="__Coffee RPG__ est disponible et mis en place par les équipes de BreakBot.\n"
                                              "Dans celui-ci vous pourrez miner des ressources afin de vous enrichir et de "
                                              "commercer avec les autres joueurs. Ce RPG est multiserveur donc vous pouvez "
                                              "y jouer de n'importe où.")

embed_two_rules = discord.Embed(title="Règles de base", color=0x25FF98,
                                description="- Vous êtes tenue de respecter ce règlement sous peine de bannissement de "
                                            "l'animation.\n"
                                            "- Vous avez le droit d'organiser des animations sur vos serveurs à partir "
                                            "de ce RPG mais vous ne pouvez pas en copier le contenue.\n"
                                            "- Respectez les nouveaux joueurs et formez les, les bons comportement "
                                            "peuvent être favorisé par des récompenses.\n"
                                            "- Les arnaques sont sévèrement puni, ne vous y amusez pas.")

embed_three_farm = discord.Embed(title="Farm", color=0x25FF98,
                                 description="Il existe 5 types de farming : la cueillette de champignons, la coupe de "
                                             "bois, le minage de charbon, la pêche de poissons et la chasse.")

embed_four_utils = discord.Embed(title="Nourriture / Outils", color=0x25FF98,
                                 description="Grâce à la nourriture et aux outils, vos rendements peuvent augmenter ce "
                                             "qui vous permet d’accélérer dans votre aventure. Vous disposez d'origine "
                                             "de 500 <:flash:841414591011487774> (rechargeable avec la nourriture). "
                                             "C'est votre énergie, vous en avez besoin pour farm.")

embed_five_shop = discord.Embed(title="Boutique", color=0x25FF98,
                                description="Dans la boutique, vous pourrez trouver tout plein d'objets, d'outils et de"
                                            "consommable vous permettant d'évoluer dans l'aventure. Celle-ci peut même"
                                            "contenir quelques produits en stock limité pour les évènements.")

embed_six_event = discord.Embed(title="Évènements", color=0x25FF98,
                                description="Nous mettrons en place des évènements réguiliers afin de permettre aux "
                                            "joueurs d'avancer rapidement dans le départ. Les invitations sur le serveur"
                                            "support vous seront désormais utiles, les rôles évolutifs rapporteront de"
                                            "l'argent.")

"""Possibilité de réponses Alea"""
reponse = ["Oui", "Mouais", "Bien sûr", "Yup", "Vaut mieux que je rép pas", "La réponse est dans la question",
           "Sans blague : OUI", "Sans blague : NON",
           "Euh", "Disons que... Bah...", "...", "As-tu besoin d'une robote pour te rep ?",
           "Je suis un robot, je ne peut pas te blesser",
           "Je m'en tape le code par terre", "La vérité blesse, le mensonge préserve",
           "Tu me prends pour qui ? Tu crois que je sais tout ?",
           "Non", "Je préfère pas rép, sinon Sfertix va encore me débrancher", "T'as trop cru",
           "Pour une réponse : appelle Sidoréla ||C'est con elle est plus là||"
           "Je pense que tu devrais continuer ton chemin"]

"""Embed d'erreur inattendu"""

