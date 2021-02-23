import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!",description = "CorBoBot pour vous servire !info " )

@bot.event
async def on_ready():
    print("Ready !")

@bot.command()
async def coucou(ctx):
    print("salut ^^ ")
    await ctx.send("Salut ^^")

@bot.command()
async def serverinfo(ctx):
    server = ctx.guild
    numberoftextechanels  = len(server.text_channels)
    numberofvoicechannels = len(server.voice_channels)
    numberofperson = server.member_count
    servername = server.name
    serverinfo = f"Le serveur {servername} , contient {numberofperson} membres , {numberoftextechanels} Salons écrits et {numberofvoicechannels} Salons vocaux"
    await ctx.send(serverinfo)

@bot.command()
async def say(ctx , *texte):
    await ctx.send(" ".join(texte))

@bot.command()
async def clear(ctx, nombre : int ):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()

@bot.command()
async def bandef(ctx , user : discord.User , reason ):
    reason = " ".join(reason)
    await ctx.guild.ban(user , reason = reason)
    await ctx.send(f"{user} a été ban avec succès")

bot.remove_command("help")

@bot.command()
async def help(ctx) :
    embed = discord.Embed (title= "**Les commandes**" , description=     f"__Toutes les commandes disponible sont:__ \n **Le kick** ; *!kick pseudo tag* \n **Le Bandef** ; *!bandef pseudo tag* \n **Le clear** ; *!clear nombre de message* \n **Le say** (sert à répeter une phrase) ; *!say phrase* \n **Le serveur info** ; *!serverinfo (sans u à server)* \n **Le clan** ; *!clan tout est expliquer une fois la commande executer* \n **Le MP **; *!MP vous permet de DM une personne depuis le Bot*")
    await ctx.send(embed=embed)

@bot.command()
async def kick(ctx , user : discord.User , *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    await ctx.send(f"{user} a été kick avec succès")

@bot.command()
async def clan(ctx):
    embed = discord.Embed(title= "**Quel est ton clan ?**", description="***Clique la haut pour le savoir***" , url = "https://grabify.link/RXJ6G8   ")
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/QBDYjHNsLpMcKZx9PfV6Y1ESh9mrPdoGokFBnM-OIOk/%3Fq%3Dtbn%253AANd9GcQ9lcA_hPjW_bjkBVYBL__LBO_K89rT29N8oA%26usqp%3DCAU/https/encrypted-tbn0.gstatic.com/images")
    embed.add_field(name = "__Les clan possible a avoir__" , value= "Clan Uchiha , Uzumaki , Hyuga ... "  )
    embed.add_field(name="Les règles : " , value= "Le droit de touner la roue que une fois (Je vois les logs donc pas de triche ;)")
    await ctx.send(embed = embed)

@bot.command()
async def gulag(ctx):
    embed = discord.Embed(title= " **Gulag** " , description= "tu va aller au GULAG " )
    embed.set_thumbnail(url="https://www.google.com/imgres?imgurl=https%3A%2F%2Femojis.slackmojis.com%2Femojis%2Fimages%2F1585999706%2F8494%2Fstalin_go_to_gulag.png%3F1585999706&imgrefurl=https%3A%2F%2Fslackmojis.com%2Femojis%2F8494-stalin_go_to_gulag&tbnid=8G3LGXIL8vu6hM&vet=10CAMQxiAoAGoXChMIgMLK_5OA7wIVAAAAAB0AAAAAEAc..i&docid=Yla7QZTEjlDCgM&w=128&h=128&itg=1&q=Gulag%20emoji&ved=0CAMQxiAoAGoXChMIgMLK_5OA7wIVAAAAAB0AAAAAEAc")
    await ctx.send("Tu va aller au Gulag" , embed=embed )

@bot.command()
async def MP(ctx , user :discord.User , *message):
    personne = user
    message = " ".join(message)
    await user.send(message)

@bot.command()
async def TS(ctx , chan : discord.TextChannel , *message):
    message = " ".join(message)
    await chan.send(message)

@bot.command()
async def NoirOuBlanc








bot.run("NzcwNjgzMzI5NzcwNDIyMzky.X5hIyA.LxsIKJxbUc5ppm4KbkbeYL0SpSY")