def main():
    print("--- 📡 PŘEKLADAČ: MORSEOVA ABECEDA 📡 ---")
    print("Můžeš překládat text do Morseovky nebo naopak.")
    
    MORSE_SLOVNIK = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
        '7': '--...', '8': '---..', '9': '----.', 
        '.': '.-.-.-', ',': '--..--', '?': '..--..', ' ': '/'
    }

    OBRACENY_SLOVNIK = {hodnota: klic for klic, hodnota in MORSE_SLOVNIK.items()}

    while True:
        print("\nVyber si akci:")
        print("1. Text -> Morseovka")
        print("2. Morseovka -> Text")
        print("3. Konec")
        
        volba = input("Zadej číslo (1-3): ")
        
        if volba == "1":
            text = input("Zadej text k překladu: ").upper()
            preklad = ""
            for znak in text:

                preklad += MORSE_SLOVNIK.get(znak, znak) + " "
            print(f"\n✅ Výsledek: {preklad}")
            
        elif volba == "2":
            print("Zadávej znaky oddělené mezerou (pro mezeru mezi slovy použij lomítko /).")
            morse = input("Zadej Morseovku: ").split(" ")
            preklad = ""
            for znak in morse:
                preklad += OBRACENY_SLOVNIK.get(znak, "?")
            print(f"\n✅ Výsledek: {preklad}")
            
        elif volba == "3":
            print("Konec vysílání. Přepínám a končím! 📻")
            break
        else:
            print("❌ Neplatná volba.")

if __name__ == "__main__":
    main()