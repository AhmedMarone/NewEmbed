# Bot d'Embed Discord

Ce bot Discord permet d'envoyer des messages embed personnalisés dans un salon spécifique.

## Commande

Le bot dispose d'une commande `embed` qui peut être utilisée pour envoyer un message embed personnalisé dans un salon désigné. Voici les détails de la commande :

- **Nom**: `embed`
- **Description**: 📰 Envoyer un embed personnalisé avec image, couleur... dans un salon
- **Paramètres**:
  - `content` (str): Le contenu principal de l'embed.
  - `channel` (discord.TextChannel): Le salon où envoyer l'embed.
  - `title` (str, optionnel): Le titre de l'embed.
  - `color` (str, optionnel): La couleur de l'embed au format hexadécimal (par exemple, "#ff0000").
  - `image_url` (str, optionnel): L'URL de l'image à inclure dans l'embed.
  - `mention` (discord.Role, optionnel): Le rôle à mentionner dans le message. 
  - `footer_text` (str, optionnel): Le texte du footer de l'embed.

## Exemple

```python
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
    # Code de la commande embed...

Avant de lancer le bot, assurez-vous de remplacer "YourToken" par votre propre token d'authentification Discord.



SUIVEZ-MOI:

X (Twitter) : https://twitter.com/AmedMarone

Youtube : https://www.youtube.com/@MaroneOpenSource

