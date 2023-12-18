import emoji
import requests
from bs4 import BeautifulSoup
import re
import webbrowser
from colorama import init, Fore, Style
import shutil
import os
import time
import getpass

if os.name == 'nt':
    import ctypes

__version__ = '1.0.0'

init(autoreset=True)

if os.name == "nt":
    ctypes.windll.kernel32.SetConsoleTitleW(f" Programmed and owned by lelaxltcl#0000 | https://discord.gg/ltclservices | SMM Botting Sites ")
else:
    pass

password = ""
max_password_attempts = 3

categories1 = {
    "Chargeable": {
        "SMB Panel": "https://smbpanel.net/",
        "TSMG Reseller": "https://tsmgreseller.com/",
        "joy SMM": "https://www.joysmm.net",
        "SmmStone": "https://smmstone.com",
        "SMM Raja": "https://www.smmraja.com",
        "SmmFollows": "https://smmfollows.com",
        "SMM Pak Panel": "https://smmpakpanel.com",
        "Smm World Panel": "https://smmworldpanel.com",
        "Secsers": "https://secsers.com",
        "PrimeSMM": "https://primesmm.com/",
    },
    "Free Options": {
        "Zefoy": "https://zefoy.com/",
        "Fire Liker": "https://fireliker.com/",
        "Instafollows": "https://www.instafollowers.co/",
    },
    "Credits/Socials": {
        "Discord Server (Custom Link)": "https://discord.gg/ltclservices",
        "Discord Server (Always working Link)": "https://discord.gg/NsMUAQPvG5",
        "Instagram Account": "https://instagram.com/lelaxltcl/",
        "GitHub Account": "https://github.com/LelaxLTCL",
        "GitHub Tool Link": "https://github.com/LelaxLTCL/SMM-Botting",
    },
    "Support me :)": {
        "PayPal Link": "https://paypal.me/myltcl",
    }
}

def open_link1(link):
    webbrowser.open(link)

def display_categories1():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        terminal_width = shutil.get_terminal_size().columns
        header1 = " ######  ##     ## ##     ##        ########   #######  ######## ######## #### ##    ##  ######  "
        header2 = "##    ## ###   ### ###   ###        ##     ## ##     ##    ##       ##     ##  ###   ## ##    ## "
        header3 = "##       #### #### #### ####        ##     ## ##     ##    ##       ##     ##  ####  ## ##       "
        header4 = " ######  ## ### ## ## ### ##        ########  ##     ##    ##       ##     ##  ## ## ## ##   ####"
        header5 = "      ## ##     ## ##     ##        ##     ## ##     ##    ##       ##     ##  ##  #### ##    ## "
        header6 = "##    ## ##     ## ##     ##        ##     ## ##     ##    ##       ##     ##  ##   ### ##    ## "
        header7 = " ######  ##     ## ##     ##        ########   #######     ##       ##    #### ##    ##  ######  "
        credit1 = "================================================================================================="
        credit2 = "================================================================================================="
        os.system('cls' if os.name == 'nt' else 'clear')

        print(Fore.RED + header1.center(terminal_width))
        print(Fore.RED + header2.center(terminal_width))
        print(Fore.RED + header3.center(terminal_width))
        print(Fore.RED + header4.center(terminal_width))
        print(Fore.RED + header5.center(terminal_width))
        print(Fore.RED + header6.center(terminal_width))
        print(Fore.RED + header7.center(terminal_width))
        print(Fore.LIGHTBLUE_EX + credit1.center(terminal_width))
        print(Fore.LIGHTBLUE_EX + credit2.center(terminal_width))
        print()
        for i, category in enumerate(categories1.keys(), start=1):
            print(Fore.LIGHTGREEN_EX + f"[{i}]" + Fore.RESET +  f" {category}")
        print()
        print(Fore.LIGHTRED_EX + "[0]" + Fore.RESET + " Close/Exit")
        print()

        choice = input(Fore.LIGHTGREEN_EX + "[>]" + Fore.RESET + " Please choose a category: ")

        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(categories1):
            selected_category = list(categories1.keys())[int(choice) - 1]
            display_links1(selected_category)
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")
            time.sleep(2)

def display_links1(category):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        terminal_width = shutil.get_terminal_size().columns
        underline = f"Category: {category}"
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.LIGHTBLUE_EX + underline.center(terminal_width))
        print()
        category_links = categories1[category]
        for i, (link_name, link_url) in enumerate(category_links.items(), start=1):
            print(Fore.LIGHTGREEN_EX + f"[{i}]" + Fore.RESET + f" {link_name}")
        print()
        print(Fore.LIGHTRED_EX + "[0]" + Fore.RESET + " Back")
        print()

        choice = input(Fore.LIGHTGREEN_EX + "[>]" + Fore.RESET + " Please choose a link or" + Fore.LIGHTRED_EX + " [0]" + Fore.RESET + " to go back: ")

        if choice == '0':
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(category_links):
            selected_link = list(category_links.values())[int(choice) - 1]
            open_link1(selected_link)
            time.sleep(1)
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")
            time.sleep(2)

def check_latest_version():
    
    # GitHub Repository URL
    github_url = 'https://github.com/LelaxLTCL/SMM-Botting/releases/latest'

    # Adding User-Agent to mimic a browser
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # Sending a request to the GitHub page
        response = requests.get(github_url, headers=headers)
        if response.status_code == 200:
            # Get the HTML content of the page
            html_content = response.text

            # Using BeautifulSoup to find the release tag
            soup = BeautifulSoup(html_content, 'html.parser')
            release_tag = soup.find('span', class_='css-truncate-target')

            # Searching for the release tag to extract version number (assumed format: vX.X.X)
            if release_tag:
                latest_version = release_tag.text.strip()
                # Enter your current local version of the tool here
                current_version = __version__  # Now referring to the local version defined earlier

                # Comparing version numbers
                if latest_version != current_version:
                    print(Fore.LIGHTGREEN_EX + "[!]" + Fore.RESET + " A new version " + Fore.LIGHTGREEN_EX + f"({latest_version})" + Fore.RESET + " is available!")
                    print()
                    decision = input(Fore.LIGHTGREEN_EX + "[?]" + Fore.RESET + " Do you want to visit the new version page now or later (now/later): ")
                    print(Fore.LIGHTGREEN_EX + "[i]" + Fore.RESET + " You still need to install the .zip folder manually")
                    if decision == "now":
                        webbrowser.open(github_url)
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(Fore.LIGHTGREEN_EX + "[>]" + Fore.RESET + " No Problem, I ask you again when you start this tool again :)")
                        print() 
                        input(Fore.LIGHTGREEN_EX + "[>]" + Fore.RESET + " Press any key to continue...")
                else:
                    print(Fore.LIGHTGREEN_EX + "[!]" + Fore.RESET + " The installed version is up to date.")
                    print()
                    input(Fore.LIGHTGREEN_EX + "[>]" + Fore.RESET + " Press any key to continue...")
            else:
                print(Fore.LIGHTRED_EX + "[!]" + Fore.RESET + " Error: Version number not found.")
                print()
                input(Fore.LIGHTGREEN_EX + "[>]" + Fore.RESET + " Press any key to continue...")
        else:
            print(Fore.LIGHTRED_EX + "[!]" + Fore.RESET + " Error while fetching the webpage. Status code:", response.status_code)
    except requests.RequestException as e:
        print(Fore.LIGHTRED_EX + "[!]" + Fore.RESET + " Request error:", e)
        print()
        input(Fore.LIGHTGREEN_EX + "[>]" + Fore.RESET + " Press any key to continue...")

if __name__ == "__main__":
    check_latest_version()
    display_categories1()
