import random
import time

def vygeneruj_cislo():
    """Vytvoří tajné 4místné číslo s unikátními číslicemi."""

    prvni = random.randint(1, 9)
    zbytek_moznosti = list(range(10))
    zbytek_moznosti.remove(prvni)

    dalsi = random.sample(zbytek_moznosti, 3)

    tajne = [prvni] + dalsi
    return tajne

def main():
    print("--- 🐮 BÝCI A KRÁVY (Logic Game) 🐮 ---")
    print("Počítač si myslí 4místné číslo (číslice se neopakují).")
    print("Tvým úkolem je ho uhodnout.")
    print("🐮 Býk = Správné číslo na správném místě.")
    print("🐄 Kráva = Správné číslo, ale jinde.")
    print("---------------------------------------")

    tajne_cislo = vygeneruj_cislo()

    pokusy = 0
    zacatek_casu = time.time()

    while True:
        tip_str = input("\nZadej 4místné číslo: ")

        if not tip_str.isdigit() or len(tip_str) != 4:
            print("⚠️ Musíš zadat přesně 4 číslice!")
            continue

        if len(set(tip_str)) != 4:
            print("⚠️ Číslice se nesmí opakovat!")
            continue
        tip = [int(c) for c in tip_str] 
        pokusy += 1

        byci = 0
        kravy = 0

        for i in range(4):

            if tip[i] == tajne_cislo[i]:
                byci += 1

            elif tip[i] in tajne_cislo:
                kravy += 1

        print(f"Výsledek: {byci} 🐮 (Býků), {kravy} 🐄 (Krav)")

        if byci == 4:
            konec_casu = time.time()
            trvani = round(konec_casu - zacatek_casu, 2)
            print("\n🎉 GRATULUJI! Uhodla jsi to! 🎉")
            print(f"Počet pokusů: {pokusy}")
            print(f"Čas: {trvani} sekund")
            break

if __name__ == "__main__":
    main()
                