from PIL import Image
import os

def main():
    print("--- 📸 ČERNOBÍLÝ FILTR 📸 ---")
    
    vstup = input("Zadejte název fotky (včetně .jpg/.png): ")

    if not os.path.exists(vstup):
        print("❌ Chyba: Takový soubor tady nevidím. Zkontrolujte název.")
        return

    try:
        obrazek = Image.open(vstup)
        print(f"✅ Obrázek načten. Velikost: {obrazek.size}")

        cernobily = obrazek.convert("L")

        vystup = "bw_" + vstup
        cernobily.save(vystup)
        
        print(f"✨ Hotovo! Černobílá verze uložena jako: {vystup}")
        print("Tip: Klikněte na soubor vlevo, ať se pokocháte.")

    except Exception as e:
        print(f"❌ Něco se pokazilo: {e}")

if __name__ == "__main__":
    main()