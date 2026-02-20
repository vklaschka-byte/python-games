import qrcode
import os

def main():
    print("---📱 GENERÁTOR QR KÓDŮ 📱 ---")

    text = input("Zadej text nebo odkaz (např. https://github.com): ")

    if not text.strip():
        print("❌ Nesmíš zadat prázdný text!")
        return
    
    nazev = input("Jak se má jmenovat obrázek? (např. muj_kod): ")
    if not nazev.endswith(".png"):
        nazev += ".png"

    print("⏳ Generuji QR kód...")

    try:

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(text)
        qr.make(fit=True)

        obrazek = qr.make_image(fill_color="black", back_color="white")
        obrazek.save(nazev)

        print(f"✅ Hotovo! QR kód byl úspěšně uložen jako obrázek: {nazev}")
        print("Můžeš si ho na zkoušku naskenovat foťákem v mobilu! 📸")

    except Exception as e:
        print(f"❌ Nastala chyba při generování: {e}")

if __name__ == "__main__":
    main()