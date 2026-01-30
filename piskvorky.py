def vytvorit_plochu():
    return [" " for _ in range(9)]

def vypis_plochu(plocha):
    print("\n")
    print(f" {plocha[0]} | {plocha[1]} | {plocha[2]} ")
    print("---|---|---")
    print(f" {plocha[3]} | {plocha[4]} | {plocha[5]} ")
    print("---|---|---")
    print(f" {plocha[6]} | {plocha[7]} | {plocha[8]} ")
    print("\n")

def zkontroluj_vyhru(plocha, hrac):
    vyherni_kombinace = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)             
    ]
    
    for a, b, c in vyherni_kombinace:
        if plocha[a] == hrac and plocha[b] == hrac and plocha[c] == hrac:
            return True
    return False

def main():
    print("--- ⭕ PIŠKVORKY (Tic-Tac-Toe) ❌ ---")
    print("Ovládání: Zadávej čísla 1-9 podle pozice na klávesnici.")
    
    plocha = vytvorit_plochu()
    aktualni_hrac = "X"
    kolo = 1
    
    while True:
        vypis_plochu(plocha)
        print(f"Na tahu je hráč: {aktualni_hrac}")
        
        try:
            pozice = int(input("Kam chceš hrát (1-9): ")) - 1
            
            if pozice < 0 or pozice > 8:
                print("⚠️ Číslo musí být od 1 do 9!")
                continue
                
            if plocha[pozice] != " ":
                print("⚠️ Tohle políčko už je obsazené!")
                continue
                
            plocha[pozice] = aktualni_hrac
            
            if zkontroluj_vyhru(plocha, aktualni_hrac):
                vypis_plochu(plocha)
                print(f"🎉 GRATULUJI! Hráč {aktualni_hrac} vyhrál! 🎉")
                break
            
            if " " not in plocha:
                vypis_plochu(plocha)
                print("🤝 Je to REMÍZA!")
                break
            
            aktualni_hrac = "O" if aktualni_hrac == "X" else "X"
            
        except ValueError:
            print("❌ Musíš zadat číslo!")

if __name__ == "__main__":
    main()