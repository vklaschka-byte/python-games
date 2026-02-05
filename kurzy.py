import requests

def main():
    print("--- 💱 MĚNOVÁ KALKULAČKA (CZK Converter) 💱 ---")
    print("Stahuji aktuální kurzy z internetu...")

    try:

        url = "https://api.exchangerate-api.com/v4/latest/CZK"
        odpoved = requests.get(url)
        data = odpoved.json()

        kurzy = data['rates']

        print("✅ Data stažena.")
        print("---------------------------------------")

        castka = float(input("Kolik korun (CZK) chceš převést?"))
        cilova_mena = input("Na jakou měnu? (EUR, USD, GBP, PLN, JPY...):").upper()

        if cilova_mena in kurzy:
            kurz = kurzy[cilova_mena]
            vysledek = castka * kurz

            print(f"\n💰 {castka} CZK = {round(vysledek, 2)} {cilova_mena}")
            print(f"(Aktuální kurz: 1 CZK = {kurz} {cilova_mena})")

            print(f"(Pro info: 1 {cilova_mena} = {round(1/kurz, 2)} CZK)")

        else:
            print("❌ Tuto měnu neznám nebo není v kurzovním lístku.")

    except ValueError:
        print("❌ Musíš zadat číslo (např. 100 nebo 150.5).")
    except Exception as e:
        print(f"❌ Chyba připojení: {e}")

if __name__ == "__main__":
    main()