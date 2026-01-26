import random

def main():
    print("--- 💀 HRA ŠIBENICE 💀 ---")
    
    slova = ["python", "program", "pocitac", "klavesnice", "internet", "robot", "sluchatka", "obrazovka"]
    
    tajne_slovo = random.choice(slova)
    uhadnuto = []
    zivoty = 7
    
    obrazky = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]

    while zivoty > 0:
        print(obrazky[zivoty])
        
        tajenka = ""
        chybi_pismen = 0
        
        for pismeno in tajne_slovo:
            if pismeno in uhadnuto:
                tajenka += pismeno + " "
            else:
                tajenka += "_ "
                chybi_pismen += 1
        
        print(f"Tajenka: {tajenka}")
        print(f"Zbývá životů: {zivoty}")
        
        if chybi_pismen == 0:
            print("\n🎉 GRATULUJI! Vyhrál jsi! Zachránil jsi panáčka! 🎉")
            break
        
        tip = input("Hádej písmeno: ").lower()
        
        if len(tip) != 1:
            print("❌ Zadej vždy jen jedno písmeno!")
            continue
            
        if tip in uhadnuto:
            print("⚠️ Tohle písmeno už jsi zkoušel.")
            continue
            
        uhadnuto.append(tip)
        
        if tip in tajne_slovo:
            print(f"✅ Super! Písmeno '{tip}' tam je.")
        else:
            print(f"❌ Smůla! Písmeno '{tip}' tam není.")
            zivoty -= 1

    if zivoty == 0:
        print(obrazky[0])
        print(f"\n💀 PROHRÁL JSI! Tajné slovo bylo: {tajne_slovo}")

if __name__ == "__main__":
    main()