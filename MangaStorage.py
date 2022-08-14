import os
import sys
import colorama
from colorama import Fore, Back, Style
from typing_extensions import Self
if sys.version_info < (3, 8):
    from typing_extensions import Literal
else:
    from typing import Literal

colorama.init(autoreset=True)

class ItemDirectory:
    __path: str
    __location: Literal['local', 'external']
    __items: list[Self] = []

    def __init__(self, path: str, location: Literal['local', 'external']):
        self.__path = path
        self.__location = location

        with os.scandir(path) as items:
            self.__items = [ItemDirectory(item.path, location) for item in items if item.is_dir()]
    
    def isLocal(self) -> bool:
        if self.__location == 'local': return True
        return False
    
    def isExternal(self) -> bool:
        if self.__location == 'external': return True
        return False
    
    @property
    def path(self) -> str:
        return self.__path

    @property
    def count(self) -> int:
        return len(self.__items)
    
    @property
    def items(self) -> list[Self]:
        return self.__items

    @property
    def size(self) -> str:
        sizeValue = self.__getDirSize(self.__path)
        unit = 'B'
        color = Fore.LIGHTGREEN_EX
        while sizeValue > 1024:
            sizeValue = sizeValue / 1024
            if unit == 'B': 
                unit = 'KB'
                color = Fore.GREEN
            elif unit == 'KB': 
                unit = 'MB'
                color = Fore.YELLOW
            elif unit == 'MB': 
                unit = 'GB'
                color = Fore.LIGHTRED_EX
            else: 
                unit = 'TB'
                color = Fore.RED
        return "{}{:.2f} {}{}".format(color, sizeValue, unit, Fore.RESET)

    def __getDirSize(self, dirPath) -> int:
        totalSize: int = 0
        with os.scandir(dirPath) as itemDir:
            for item in itemDir:
                if item.is_dir():
                    totalSize += self.__getDirSize(item.path)
                elif item.is_file():
                    totalSize += item.stat().st_size
        return totalSize

        

class StorageLocation(ItemDirectory):
    def __init__(self, path: str, location: Literal['local', 'external']):
        print(f"Initializing {Fore.CYAN}{location}{Fore.RESET} storage at path {Fore.CYAN}{path}")
        super().__init__(path, location)

    def getMangaCount(self) -> str:
        mangaCount = sum([itemDir.count for itemDir in self.items])
        color = Fore.LIGHTGREEN_EX if mangaCount < 10 else Fore.GREEN if mangaCount < 25 else Fore.YELLOW if mangaCount < 50 else Fore.RED
        return f"{color}{mangaCount}{Fore.RESET}"

    def getNumberActiveSources(self) -> str:
        activeSources = len([sources.path for sources in self.items if sources.count > 0])
        color = Fore.LIGHTGREEN_EX if activeSources < 5 else Fore.GREEN if activeSources < 10 else Fore.YELLOW if activeSources < 15 else Fore.RED
        return f"{color}{activeSources}{Fore.RESET}"