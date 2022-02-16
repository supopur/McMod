import discord
from discord.ext import commands
import logging
import colorama
from colored import fg
import threading
from time import sleep
import secrets
from getup import getup
from getup import getplayers
#set up the logger
logging.basicConfig(filename='main.log', encoding='utf-8', level=logging.DEBUG)
log = logging.info

client = commands.Bot(command_prefix="!")
logging.info('Clearing logs...')

f = open('simple.log', 'w')
f.write("")
f.close()

f = open('main.log', 'w')
f.write("")
f.close()




#the logging thingie
def log(msg : str, level : str = 'info'):

    with open('simple.log', 'a') as f:
        
        if level == "info":
            color = fg('green')
            white = fg('white')
            print(f'[INFO]', color + msg + white)
            logging.info(msg)
            f.write(f"[INFO] {msg} \n")

        elif level == 'debug':
            color = fg('white')
            white = fg('white')
            print(f'[DEBUG]', color + msg + white)
            logging.debug(msg)
            f.write(f"[DEBUG] {msg} \n")

        elif level == 'warning':
            color = fg('yellow')
            white = fg('white')
            print(f'[WARNING]', color + msg + white)
            logging.warning(msg)
            f.write(f"[WARNING] {msg} \n")

        elif level == 'error':
            color = fg('red')
            white = fg('white')
            print(f'[ERROR]', color + msg + white)
            logging.error(msg)
            f.write(f"[ERROR] {msg}\n")

        else:
            color = fg('green')
            white = fg('white')
            print(f'[INFO]', color + msg + white)
            logging.info(msg)
            f.write(f"[INFO] {msg}\n")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Violku"))
    log('Discord.py is ready')

@client.event
async def on_message(message):
    #log('on_message event called', 'debug')
    msg = message.content.lower()
    if message.author == client.user:
        return
    
    if message.channel.name == '📟-game-console' or message.channel.name == '💻-game-chat-minecraft':
        return
    if 'online' in msg:
        log('The message contains the word online, deleting the message...')
        await message.delete()
        up = getup('192.168.50.7', '25575')
        if up:
            await message.author.send("<:status:923623332291682375> Server je online prosím neptej se takto. Děkuji ;)")
        if not up:
            await message.author.send("<:statr:923882871486296074> Server je offline nejspíše pro údržbu. Podívej se na naší webovou stránku pokud není velká údržba :wrench:: https://nazev.eu  prosím neptej se takto. Děkuji ;)")
    await client.process_commands(message)

@client.command()
async def players(ctx):
    log('The command players has been called')
    players = getplayers('192.168.50.7', '25575')
    await ctx.send(players)

@client.command()
async def mc(ctx):
    log('Sending minecraftServer ip')
    await ctx.send('Ip minecraft serveru: mc.nazev.eu')

@client.command()
async def web(ctx):
    log('Sending website')
    await ctx.send('Webová stránka: https://nazev.eu')

@client.command()
async def mods(ctx):
    log('Sending website/mod-installer url')
    await ctx.send('Návod jak nainstalovat módy: https://nazev.eu/mod_installer.html')


if __name__ == "__main__":
    #x = threading.Thread(target=autoclean)
    log('Starting the autoclean thread...', 'debug')
    #x.start()
    log('Getting the token from secrets.py file...', 'debug')
    #print(secrets.token)

    client.run(secrets.token)