#wersja BETA
import discord
import os

wersja = 'Release 1.5.2'
gra = "Apu Band"
client = discord.Client()

@client.event
async def on_ready():
    game = discord.Game(gra)
    await client.change_presence(status=discord.Status.online, activity=game) 
    channel = client.get_channel(813379346768986123)
    await channel.send('MeMeSzkoBot 3..0 został uruchomiony i zaaktualizowany do najnowszej dostępnej wersji pomyślnie. Aktualna Wersja: '+wersja)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#!test
    if message.content.startswith('!test'):
        await message.channel.send('Jeżeli to widzisz, to bot działa poprawnie! ' +message.author.mention)

#!granko 
    if message.content.startswith('!granko'):
        await message.channel.send('<@&705077146204504144>')
        embedVar = discord.Embed(title="Granko Time?", description= "Ktoś chce granko!", color=0x00ff00)
        embedVar.set_image(url="https://images-ext-1.discordapp.net/external/bfOVAGmGLYXgAwPk5cO1JbOUliaPshr7h4B9MDgK2KY/%3Fwidth%3D346%26height%3D229/https/media.discordapp.net/attachments/680160808403337326/732984544059326574/GRANKo.png")
        embedVar.set_author(name='MeMeszkoBot 3.0', icon_url='https://cdn.discordapp.com/avatars/819887662571847721/5262f14e44a9e8cc719feaa3bf2ff605.webp?size=256')
        embedVar.set_footer(text='Użyj !kmd aby pokazać listę komend.')
        await message.channel.send(embed=embedVar)
        
#!przerwa
    if message.content.startswith('!przerwa'):
        await message.channel.send('<@&764822752388972586>')
        embedVar = discord.Embed(title="Przerwa Time?", description= "Ktoś wywołał dzwonek!", color=0xff0000)
        embedVar.set_image(url="https://news.edubaza.pl/img/wo/2/87/Korytarz-szkolny-obrazek_sredni_4026287.jpg")
        embedVar.set_author(name='MeMeszkoBot 3.0', icon_url='https://cdn.discordapp.com/avatars/819887662571847721/5262f14e44a9e8cc719feaa3bf2ff605.webp?size=256')
        embedVar.set_footer(text='Użyj !kmd aby pokazać listę komend.')
        await message.channel.send(embed=embedVar)
        
#!help
    if message.content.startswith('!kmd'):
        embedVar = discord.Embed(title="Lista Komend", description="Wszystkie komendy MeMeSzkobota", color=0x0099ff)
        embedVar.add_field(name="Komendy:", value="!granko - granko time\n!przerwa - przerwa time\n!kmd - lista komend\n!test - testuje działalność bota\n!info - informacje o bocie", inline=False)
        embedVar.set_thumbnail(url="https://media.tenor.com/images/c78f273d8f6a182827a539302582adb6/tenor.gif")
        embedVar.set_footer(text='MeMeSzkoBot 3.0. Wersja ' +wersja)
        await message.channel.send(embed=embedVar)
    
#!info
    if message.content.startswith('!info'):
        embedVar = discord.Embed(title="Informacje", description="MeMeSzkoBot 3.0", color=0x0099ff)
        embedVar.add_field(name="Zaprogramowany przez theubusu#6401", value="Wersja " +wersja, inline=False)
        embedVar.add_field(name="Kod MeMeszkobota jest dostępny", value="[tutaj](https://github.com/theubusu/memeszkobot) ", inline=False)
        embedVar.set_thumbnail(url="https://media.tenor.com/images/c78f273d8f6a182827a539302582adb6/tenor.gif")
        embedVar.set_footer(text='(R)theubusu 2021')
        await message.channel.send(embed=embedVar)
        
#!dnd        
    if message.content.startswith('!dnd'):
      if message.author.id == 631872127934660609:
        game = discord.Game(gra)
        await client.change_presence(status=discord.Status.dnd, activity=game)
        await message.channel.send('ok ' +message.author.mention)

#!offdnd       
    if message.content.startswith('!offdnd'):
      if message.author.id == 631872127934660609:
        game = discord.Game(gra)
        await client.change_presence(status=discord.Status.online, activity=game)
        await message.channel.send('ok ' +message.author.mention)


client.run(os.getenv('Token'))
