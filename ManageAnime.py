from email.policy import default
import os
import colorama
from colorama import Fore, Style
from MangaStorage import StorageLocation
import click

colorama.init(autoreset=True)

def PathsExist(local, external):
    if not os.path.exists(local): 
        print(f"Local Path: {Fore.CYAN}{local}{Fore.RESET} {Fore.RED}[Does Not Exist]{Fore.RESET}")
        return False
    if not os.path.exists(external): 
        print(f"External Path: {Fore.CYAN}{external}{Fore.RESET} {Fore.RED}[Does Not Exist]{Fore.RESET}")
        return False

    return True

@click.command()
@click.option("--local", "-L", required=False, default="C:/Users/drjjd/Documents/Manga")
@click.option("--external", "-E", required=False, default='E:/Studf')
# Main function
def ManageMain(local, external):
    print(f'{Fore.LIGHTCYAN_EX}=======================================')
    print(f"\t{Style.BRIGHT}{Fore.GREEN}Anime Management System")
    print(f'{Fore.LIGHTCYAN_EX}=======================================\n\n')

    if not PathsExist(local, external): return

    # Initialize storage objects
    localStorage: StorageLocation = None
    ExternalStorage: StorageLocation = None

    # Attempt to initialize local storage 
    try:
        localStorage = StorageLocation(local, 'local')
        print(f"Manga/Manhwa: {localStorage.getMangaCount()} ")
        print(f"Total Size: {localStorage.size}")
    except Exception as e:
        print(e)
        print(f"{Fore.RED}Error: local storage cannot be found")

    print('\n')

    # Attempt to initialize external storage 
    try:
        ExternalStorage = StorageLocation(external, 'external')
        print(f"Manga/Manhwa: {ExternalStorage.getMangaCount()} ")
        print(f"Total Size: {ExternalStorage.size}")
        print(f"Active Sources: {ExternalStorage.getNumberActiveSources()}")
    except Exception as e:
        print(e)
        print(f"{Fore.RED}Error: external storage cannot be found")
    
    print('\n\n')

    if ExternalStorage == None:
        print(f"{Fore.LIGHTRED_EX}External Storage{Fore.RESET} cannot be found please check if it is connected")
    elif localStorage == None:
        print(f"{Fore.LIGHTRED_EX}Local Storage{Fore.RESET} cannot be found please check if path is correct")


    