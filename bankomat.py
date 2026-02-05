import json
import os
import time

SOUBOR_DATA = "banka_data.json"
SPRAVNY_PIN = "1234"

def nacist_zustatek():
    """Načte peníze ze souboru. Pokud soubor neexistuje, dá nám 1000 Kč do začátku."""
    if os.path.exists(SOUBOR_DATA):
        with open(SOUBOR_DATA, "r") as f:
            data = json.load(f)
            return data.get("zustatek", 0)
    else:
        return 1000
def ulozit_zustatek(castka):
    """Uloží aktuální peníze do souboru."""
    data = {"zustatek": castka}
    with open(SOUBOR_DATA, "w") as f:
        json.dump(data, f)

def main():
    print("--- 🏦 PYTHON BANKA & ATM 🏦 ---")

    pokusy = 3
    prihlasen = False

    while pokusy > 0:
        pin = input("Zadajte PIN (nápověda: 1234): ")
        if pin == SPRAVNY_PIN:
            prihlasen = True
            break
        else:
            pokusy -= 1
            print(f"❌ Chybný PIN! Zbývá pokusů: {pokusy}")

    if not prihlasen:
        print("🚨 Karta zablokována. Policie je na cestě.")
        return
    
    zustatek = nacist_zustatek()
    print("\n✅ PIN přijat. Vítejte v systému.")

    while True:
        print("\n------------------------------")
        print(f"💰 AKTUÁLNÍ ZŮSTATEK: {zustatek} Kč")
        print("------------------------------")
        print("1. 📥 Vložit peníze")
        print("2. 📤 Vybrat peníze")
        print("3. 🚪 Konec / Vrátit kartu")

        volba = input("Vaše volba: ")

        if volba == "1":
            try:
                vklad = int(input("Kolik chcete vložit?"))
                if vklad > 0:
                    zustatek += vklad
                    ulozit_zustatek(zustatek)
                    print("✅ Peníze vloženy.")
                else:
                    print("⚠️ Částka musí být kladná.")
            except ValueError:
                print("❌ Musíte zadat číslo.")

        elif volba == "2":
            try:
                vyber = int(input("Kolik chcete vybrat?"))
                if vyber > zustatek:
                    print("❌ Nedostatek prostředků na účtu!")
                elif vyber <= 0:
                    print("⚠️ Částka musí být kladná.")
                else:
                    zustatek -= vyber
                    ulozit_zustatek(zustatek)
                    print("✅ Peníze vybrány. Nezapomeňte si je vzít.")
            except ValueError:
                print("❌ Musíte zadat číslo.")

        elif volba == "3":
            print("Děkujeme, že používáte Python Banku. Na shledanou! 👋")
            break
        else:
            print("Neplatná volba.")

        time.sleep(1)

if __name__ == "__main__":
    main()