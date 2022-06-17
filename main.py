import feature_downloader
import psd_extractor


def print_menu():
    print("[*] Choose tool from WPs Toolkit-a:")
    print("[*] 1 - PDP feature downloader")
    print("[*] 2 - PSD image extractor")
    print("[*] 3 - Quit")

def main():

    print("""

    ░██╗░░░░░░░██╗██████╗░░██████╗  ████████╗░█████╗░░█████╗░██╗░░░░░██████╗░░█████╗░██╗░░██╗
    ░██║░░██╗░░██║██╔══██╗██╔════╝  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗╚██╗██╔╝
    ░╚██╗████╗██╔╝██████╔╝╚█████╗░  ░░░██║░░░██║░░██║██║░░██║██║░░░░░██████╦╝██║░░██║░╚███╔╝░
    ░░████╔═████║░██╔═══╝░░╚═══██╗  ░░░██║░░░██║░░██║██║░░██║██║░░░░░██╔══██╗██║░░██║░██╔██╗░
    ░░╚██╔╝░╚██╔╝░██║░░░░░██████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╦╝╚█████╔╝██╔╝╚██╗
    ░░░╚═╝░░░╚═╝░░╚═╝░░░░░╚═════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝

    """)

    print_menu()
    while True:
        user_choice = input("Enter tool id: ")

        if int(user_choice) == 1:
            feature_downloader.feature()
        elif int(user_choice) == 2:
            psd_extractor.extract()
        elif int(user_choice) == 3:
            break


if __name__ == "__main__":
    main()