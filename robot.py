from gtts import gTTS
import os

def main():
    print("--- 🤖 ROBOTICKÝ HLASATEL 🤖 ---")
    
    text = input("Zadejte text, který mám přečíst: ")
    
    nazev = input("Jak se má jmenovat MP3 soubor (bez koncovky)? ")
    soubor = nazev + ".mp3"

    print("⏳ Generuji hlas... chvilku strpení...")

    tts = gTTS(text=text, lang='cs')
    tts.save(soubor)

    print(f"✅ Hotovo! Soubor '{soubor}' je na světě.")
    
    try:
        os.system(f"start {soubor}")  # Pro Windows
    except:
        pass

if __name__ == "__main__":
    main()