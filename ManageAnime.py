from email.policy import default
import os
import colorama
from colorama import Fore, Style
from MangaStorage import StorageLocation
import click

colorama.init(autoreset=True)

@click.group(invoke_without_command=True)
@click.option("--local", "-L", type=click.Path(exists=True, file_okay=False), required=False, default="C:/Users/drjjd/Documents/Manga")
@click.option("--external", "-E", type=click.Path(exists=True, file_okay=False), required=False, default='E:/Studf')
@click.pass_context
def ManageMain(ctx, local, external):
    ctx.ensure_object(dict)
    ctx.obj['localPath'] = local
    ctx.obj['externalPath'] = external

    if ctx.invoked_subcommand is None: initial(local, external)

# Main function
def initial(local, external):
    print(f'{Fore.LIGHTCYAN_EX}=======================================')
    print(f"\t{Style.BRIGHT}{Fore.GREEN}Anime Management System")
    print(f'{Fore.LIGHTCYAN_EX}=======================================\n\n')

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
        mangaCount = int(ExternalStorage.getMangaCount()[5:-5])
        print(f"Manga/Manhwa: {ExternalStorage.getMangaCount()} ")
        print(f"Total Size: {ExternalStorage.size}")
        print(f"Active Sources: {ExternalStorage.getNumberActiveSources()}")

        if mangaCount > 0: print(f'\n{Fore.LIGHTBLACK_EX}You can transfer the {mangaCount} manga/manhwa to the local storage by using the command "tachi transfer"')
    except Exception as e:
        print(e)
        print(f"{Fore.RED}Error: external storage cannot be found")
    
    print('\n\n')


    