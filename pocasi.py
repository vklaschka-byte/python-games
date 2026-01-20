import requests
import sys

def main():
    print("--- 🌦️ ROSNIČKA (Předpověď počasí) 🌦️ ---")
    
    mesto = input("Zadejte město (např. Brno, Prague, Ostrava): ").strip()
    
    if not mesto:
        print("❌ Musíte zadat město!")
        return

    print(f"\n⏳ Stahuji data pro: {mesto}...\n")

    try:
 
        url = f"https://wttr.in/{mesto}?format=3&lang=cs"
        
        odpoved = requests.get(url)
        if odpoved.status_code == 200:
            print("-" * 40)
            print(odpoved.text.strip())
            print("-" * 40)
            
            detail = input("Chcete detailní předpověď? (ano/ne): ")
            if detail.lower() == "ano":
                url_detail = f"https://wttr.in/{mesto}?lang=cs"
                print(requests.get(url_detail).text)
                
        else:
            print("❌ Nepodařilo se zjistit počasí. Možná překlep v názvu?")

    except Exception as e:
        print(f"❌ Chyba připojení: {e}")

if __name__ == "__main__":
    main()