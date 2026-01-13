import random

def main():
    print("--- ✊ ✋ ✌️ KÁMEN, NŮŽKY, PAPÍR ✌️ ✋ ✊ ---")
    
    moznosti = ["kámen", "nůžky", "papír"]

    while True:
        print("\n--------------------------------")
        hrac = input("Vyber (kámen, nůžky, papír) nebo 'konec': ").lower().strip()

        if hrac == "konec":
            print("Díky za hru!")
            break

        if hrac not in moznosti:
            print("❌ To neznám. Zkus to znovu.")
            continue

        pocitac = random.choice(moznosti)
        print(f"🤖 Počítač vybral: {pocitac.upper()}")

        if hrac == pocitac:
            print("🤝 REMÍZA!")
        
        elif hrac == "kámen":
            if pocitac == "nůžky":
                print("✅ VYHRÁLA JSI! (Kámen tupí nůžky)")
            else:
                print("❌ PROHRÁLA JSI... (Papír balí kámen)")
        
        elif hrac == "nůžky":
            if pocitac == "papír":
                print("✅ VYHRÁLA JSI! (Nůžky stříhají papír)")
            else:
                print("❌ PROHRÁLA JSI... (Kámen tupí nůžky)")
                
        elif hrac == "papír":
            if pocitac == "kámen":
                print("✅ VYHRÁLA JSI! (Papír balí kámen)")
            else:
                print("❌ PROHRÁLA JSI... (Nůžky stříhají papír)")

if __name__ == "__main__":
    main()