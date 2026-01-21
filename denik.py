import datetime
def main():
    print("--- 📝 MŮJ DIGITÁLNÍ DENÍK 📝 ---")
    poznamka = input("Co máš dnes na srdci?")
    aktualni_cas = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    zapis = f"[{aktualni_cas}] {poznamka}\n"
    try:

        with open("denik.txt", "a", encoding="utf-8") as soubor:
            soubor.write(zapis)
            print("✅ Úspěšně zapsáno do denik.txt")

    except Exception as e:
        print(f"❌ Chyba při zápisu: {e}")

if __name__ == "__main__":
    main()