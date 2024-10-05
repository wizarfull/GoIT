import os
import sys
from colorama import Fore, Style, init

def print_directory_structure(path, indent_level=0):
    try:
        if not os.path.exists(path):
            print(Fore.RED + "Шлях не існує!" + Style.RESET_ALL)
            return
        
        if not os.path.isdir(path):
            print(Fore.RED + "Це не директорія!" + Style.RESET_ALL)
            return
        
        # Виводимо вміст директорії
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            indent = "    " * indent_level
            
            if os.path.isdir(item_path):
                print(Fore.BLUE + indent + f"📂 {item}" + Style.RESET_ALL)
                print_directory_structure(item_path, indent_level + 1)
            else:
                print(Fore.GREEN + indent + f"📜 {item}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    init(autoreset=True)
    if len(sys.argv) > 1:
        path = sys.argv[1]
        print_directory_structure(path)
    else:
        print(Fore.RED + "Будь ласка, вкажіть шлях до директорії." + Style.RESET_ALL)
