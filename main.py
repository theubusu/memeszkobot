import discord
import os
import nacl

wersja = 'Release 1.8.5'
gra = "floppa"
client = discord.Client()

@client.event
async def on_ready():
    game = discord.Game(gra)
    await client.change_presence(status=discord.Status.online, activity=game) 
    channel = client.get_channel(813379346768986123)
    embedVar = discord.Embed(title="MeMeSzkoBot 3.0", description="MeMeSzkoBot 3..0 został uruchomiony i zaaktualizowany do najnowszej dostępnej wersji pomyślnie. Aktualna Wersja: ", color=404040)
    embedVar.add_field(name=wersja, value="Lista wersji dostępna [tutaj](https://pastebin.com/raw/CMbKpM4g)", inline=False)
    await channel.send(embed=embedVar)
    print ("MeMeSzkoBot Uruchomiony :)")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#star
    if message.channel.id == 814122754504392735:
      if message.attachments or "http"  in message.content.lower():
        emoji = '⭐'
        await message.add_reaction(emoji)
              
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
        
#!kmd
    if message.content.startswith('!kmd'):
        embedVar = discord.Embed(title="Lista Komend", description="Wszystkie komendy MeMeSzkobota", color=0x0099ff)
        embedVar.add_field(name="Komendy:", value="!granko - granko time\n!przerwa - przerwa time\n!gpu - pokazuje ci RTX 3090 na pocieszenie\n!kmd - lista komend\n!test - testuje działalność bota\n!info - informacje o bocie\n!vc - dołącz do kanału głosowego (beta)", inline=False)
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
        emoji = '👍'
        await message.add_reaction(emoji)
      else:
        emoji = '⛔'
        await message.add_reaction(emoji)        

#!offdnd       
    if message.content.startswith('!offdnd'):
      if message.author.id == 631872127934660609:
        game = discord.Game(gra)
        await client.change_presence(status=discord.Status.online, activity=game)
        emoji = '👍'
        await message.add_reaction(emoji)
      else:
        emoji = '⛔'
        await message.add_reaction(emoji)
        
#!rtx
    if message.content.startswith('!gpu'):
        embedVar = discord.Embed(title="RTX 3090", description= "Masz na pocieszenie", color=0x444444)
        embedVar.set_image(url="https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/ampere/rtx-3090/geforce-rtx-3090-shop-600-p@2x.png")
        embedVar.set_author(name='MeMeszkoBot 3.0', icon_url='https://cdn.discordapp.com/avatars/819887662571847721/5262f14e44a9e8cc719feaa3bf2ff605.webp?size=256')
        embedVar.set_footer(text='Użyj !kmd aby pokazać listę komend.')
        await message.channel.send(embed=embedVar)
        
#!vc
    if message.content.startswith('!vc'):
      if message.author.voice:
        await message.author.voice.channel.connect()
        emoji = '👍'
        await message.add_reaction(emoji)
        
#!dm
    if message.content.startswith('!dm'):
      await message.author.send('elo')
      await message.delete()


client.run(os.getenv('Token'))
