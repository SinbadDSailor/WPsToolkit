import feature_downloader
import psd_extractor


def print_menu():
    print("[*] Izaberi alat iz WPs Toolkit-a:")
    print("[*] 1 - Skini slike ficera")
    print("[*] 2 - Izvlacenje slika is PSD fajla")
    print("[*] 3 - Izlaz")

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
        user_choice = input("Unesi broj zeljenog menija: ")

        if int(user_choice) == 1:
            feature_downloader.feature()
        elif int(user_choice) == 2:
            psd_extractor.extract()
        elif int(user_choice) == 3:
            break


if __name__ == "__main__":
    main()