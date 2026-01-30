import random
import os

def vycistit():
    os.system('cls' if os.name == 'nt' else 'clear')

def rozdavat_kartu():
    """Vrátí náhodnou kartu z balíčku."""
    karty = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(karty)

def spocitat_skore(karty):
    """Spočítá součet karet a vyřeší Eso (11 nebo 1)."""
    if sum(karty) == 21 and len(karty) == 2:
        return 0 

    if 11 in karty and sum(karty) > 21:
        karty.remove(11)
        karty.append(1)
        
    return sum(karty)

def porovnat(skore_hrac, skore_pocitac):
    if skore_hrac == skore_pocitac:
        return "🤝 Je to remíza!"
    elif skore_pocitac == 0:
        return "💸 Prohrál jsi, soupeř má Blackjack!"
    elif skore_hrac == 0:
        return "💰 Vyhrál jsi s Blackjackem!"
    elif skore_hrac > 21:
        return "📈 Přetáhl jsi (přes 21). Prohrál jsi."
    elif skore_pocitac > 21:
        return "💰 Soupeř přetáhl. Vyhrál jsi!"
    elif skore_hrac > skore_pocitac:
        return "💰 Vyhrál jsi!"
    else:
        return "💸 Prohrál jsi."

def hrat_hru():
    print("--- 🃏 BLACKJACK (OKO BERE) 🃏 ---")
    
    karty_hrac = []
    karty_pocitac = []
    je_konec = False

    for _ in range(2):
        karty_hrac.append(rozdavat_kartu())
        karty_pocitac.append(rozdavat_kartu())

    while not je_konec:
        skore_hrac = spocitat_skore(karty_hrac)
        skore_pocitac = spocitat_skore(karty_pocitac)
        
        print(f"\nYour cards: {karty_hrac}, current score: {skore_hrac}")
        print(f"Dealer's first card: {karty_pocitac[0]}")

        if skore_hrac == 0 or skore_pocitac == 0 or skore_hrac > 21:
            je_konec = True
        else:
            dalsi = input("Chceš další kartu? Napiš 'y' (ano) nebo 'n' (ne): ")
            if dalsi == "y":
                karty_hrac.append(rozdavat_kartu())
            else:
                je_konec = True

    while skore_pocitac != 0 and skore_pocitac < 17:
        karty_pocitac.append(rozdavat_kartu())
        skore_pocitac = spocitat_skore(karty_pocitac)

    print(f"\n--- VÝSLEDEK ---")
    print(f"Tvoje karty: {karty_hrac}, skóre: {skore_hrac}")
    print(f"Karty dealera: {karty_pocitac}, skóre: {skore_pocitac}")
    print(porovnat(skore_hrac, skore_pocitac))
    print("----------------\n")

def main():
    while True:
        hrat = input("Chceš si zahrát Blackjack? (y/n): ")
        if hrat == "y":
            vycistit()
            hrat_hru()
        else:
            print("Díky za hru! 👋")
            break

if __name__ == "__main__":
    main()