import os
import requests
from colorama import Fore, Style
import pyfiglet

def discover_directory(base_url, directories):
    discovered_directories = set()

    for directory in directories:
        url = f"{base_url}/{directory}/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                discovered_directories.add(url)
        except requests.exceptions.RequestException:
            pass

    return discovered_directories

def print_banner():
    banner_text = pyfiglet.figlet_format("Web-DIR search")
    colored_banner = Fore.MAGENTA + banner_text + Style.RESET_ALL
    print(colored_banner)

def print_signature():
    signature = f"{Fore.YELLOW}-- Web Directory Discovery by OFD5, Please use the tool for security reaserch only --{Style.RESET_ALL}\n"
    print(signature)

if __name__ == "__main__":
    print_banner()

    base_url = input("Enter the base URL (e.g., http://example.com): ")
    directories_file = input("Enter the path to the file containing directories: ")

    if not os.path.isfile(directories_file):
        print(f"{Fore.RED}Error: The specified file '{directories_file}' does not exist.{Style.RESET_ALL}")
        exit(1)

    with open(directories_file) as f:
        directories = f.read().splitlines()

    discovered_directories = discover_directory(base_url, directories)

    if discovered_directories:
        print(f"{Fore.GREEN}Discovered {len(discovered_directories)} directories:{Style.RESET_ALL}")
        for directory in discovered_directories:
            print(Fore.BLUE + directory + Style.RESET_ALL)
    else:
        print(f"{Fore.YELLOW}No directories discovered.{Style.RESET_ALL}")

    print_signature()
