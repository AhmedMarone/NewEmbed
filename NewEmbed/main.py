import discord
from discord.ext import commands
from discord import app_commands
# from discord.ext.commands import has_permissions, check


intents = discord.Intents().all()
bot = commands.Bot(command_prefix="/", intents=intents)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@bot.event
async def on_ready():
    print("Bot running with")
    print("Username: ", bot.user.name)
    print("User ID: ", bot.user.id)
    await bot.change_presence(activity=discord.Game(name="/about"))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(e)


@bot.tree.command(name='embed', description="📰 Envoyer un embed personnalisé avec image, couleur... dans un salon")
async def embed_command(
    interaction, 
    content: str, 
    channel: discord.TextChannel,
    title: str = None,
    color: str = None, 
    image_url: str = None,  
    mention: discord.Role = None,
    footer_text: str = None
):
    guild = channel.guild

    if guild is None:
        embed = discord.Embed(description="*❌  Erreur: Impossible de récupérer le serveur à partir du canal.*", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    member = guild.get_member(interaction.user.id)

    if member and (member.guild_permissions.administrator or member.guild_permissions.manage_messages):
        try:
            tweet_embed = discord.Embed(description=content)

            if title:
                tweet_embed.title = title
            
            if image_url:
                if image_url.startswith(('http://', 'https://')):
                    tweet_embed.set_image(url=image_url)
                else:
                    raise ValueError("L'image n'est pas un lien valide. Exemple : https://example.com/image.png")
            
            # Vérifier si la couleur est valide
            try:
                if color:
                    if color.startswith('#'):
                        tweet_embed.color = discord.Color(int(color[1:], 16))
                    elif color.startswith('0x'):
                        tweet_embed.color = discord.Color(int(color[2:], 16))
                    else:
                        raise ValueError("Format de couleur invalide. Utilisez le format hexadécimal.")
            except ValueError as color_error:
                embed = discord.Embed(description=f"❌ *Erreur de couleur : {color_error}*", color=discord.Color.red())
                await interaction.response.send_message(embed=embed, ephemeral=True)
                return

            mention_content = mention.mention if mention else None  # Utiliser la mention du rôle, ou None si aucun rôle spécifié

            if footer_text:
                tweet_embed.set_footer(text=footer_text)

            if not channel.permissions_for(guild.me).send_messages:
                no_access_embed = discord.Embed(description="*❌  Le bot n'a pas accès à ce salon.*", color=discord.Color.red())
                await interaction.response.send_message(embed=no_access_embed, ephemeral=True)
            else:
                if mention_content:
                    await channel.send(content=mention_content, embed=tweet_embed)
                else:
                    await channel.send(embed=tweet_embed)
                success_embed = discord.Embed(description="*✅  L'embed a été envoyé avec succès!*", color=discord.Color.green())
                await interaction.response.send_message(embed=success_embed, ephemeral=True)
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'embed : {e}")
            embed = discord.Embed(description="*❌  Erreur lors de l'envoi de l'embed.*", color=discord.Color.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(description="*⛔  Désolé, vous n'avez pas la permission d'exécuter cette commande.*", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)



# Lancer le bot
bot.run("YourToken")
