# ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃

import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('Mensagem | Message')
      print(f"> Mensagem enviada para | Message sent to : {user.name} <")
    except:
       print(f"> Mensagem recusada para | Message declined for : {user.name} <")
       
client.run('TOKEN', bot=False)


#  ▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃▃
