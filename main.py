import os
import sys

import hra
import wiki_bot
import robot
import filtr
import heslo
import pocasi
import detektiv

def vycistit_obrazovku():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        vycistit_obrazovku()
        print("==========================================")
        print("      🐍 PYTHON HERNÍ KONZOLE 🐍")
        print("==========================================")
        print("1. ✊ Hra: Kámen, Nůžky, Papír (Terminál)")
        print("2. 🎈 Hra: Kámen, Nůžky, Papír (Web)")
        print("3. 🧠 Všeználek (Wiki Bot)")
        print("4. 🤖 Mluvící Robot (Text-to-Speech)")
        print("5. 📸 Černobílý Filtr na fotky")
        print("6. 🔐 Generátor hesel")
        print("7.🌦️ Předpověď počasí")
        print("8.🕵️‍♀️ Detekce obličejů na fotce")
        print("0. 🚪 Konec")
        print("==========================================")
        
        volba = input("Vyberte možnost (0-6): ")

        print("\nSpouštím...\n")

        if volba == "1":
            hra.main()
        elif volba == "2":
            print("Spouštím webový server...")
            os.system("streamlit run web_hra.py")
        elif volba == "3":
            wiki_bot.main()
        elif volba == "4":
            robot.main()
        elif volba == "5":
            filtr.main()
        elif volba == "6":
            heslo.main()
        elif volba == "7":
            pocasi.main ()
        elif volba == "8":
            detektiv.main()
        elif volba == "0":
            print("Díky, že používáš Python! Ahoj. 👋")
            break
        else:
            print("❌ Neplatná volba!")
        
        input("\nStiskněte ENTER pro návrat do menu...")

if __name__ == "__main__":
    main()