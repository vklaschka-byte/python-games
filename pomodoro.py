import time
import os

def vycistit():

    os.system('cls' if os.name == 'nt' else 'clear')

def odpocet(minuty, zprava):
    """Funkce, která odpočítává čas a ukazuje ho na obrazovce."""
    sekundy_celkem = minuty * 60
    
    while sekundy_celkem > 0:

        minuty_zbyva = sekundy_celkem // 60
        sekundy_zbyva = sekundy_celkem % 60
        
    
        casformat = f"{minuty_zbyva:02d}:{sekundy_zbyva:02d}"
        
        print(f"\r⏳ {zprava}: {casformat}", end="")
        
        time.sleep(1) 
        sekundy_celkem -= 1
        
    print(f"\r✅ {zprava}: HOTOVO! Čas vypršel.      ")
    print('\a') 

def main():
    vycistit()
    print("--- 🍅 POMODORO ČASOVAČ (Focus Timer) 🍅 ---")
    print("Technika pro maximální produktivitu:")
    print("Pracuj 25 minut, pak si dej 5 minut pauzu.")
    print("------------------------------------------")

    while True:
        print("\nVyber si akci:")
        print("1. 💼 Začít pracovat (25 min)")
        print("2. ☕ Dát si pauzu (5 min)")
        print("3. ⚙️ Vlastní čas (odpočet)")
        print("4. 🚪 Konec")

        volba = input("Tvoje volba (1-4): ")

        if volba == "1":
            odpocet(25, "Pracovní blok")
        elif volba == "2":
            odpocet(5, "Přestávka")
        elif volba == "3":
            try:
                vlastni_min = int(input("Zadej počet minut pro odpočet: "))
                if vlastni_min > 0:
                    odpocet(vlastni_min, "Vlastní odpočet")
                else:
                    print("❌ Čas musí být větší než 0.")
            except ValueError:
                print("❌ Musíš zadat celé číslo!")
        elif volba == "4":
            print("Díky za produktivní den! 👋")
            break
        else:
            print("❌ Neplatná volba.")

if __name__ == "__main__":
    main()