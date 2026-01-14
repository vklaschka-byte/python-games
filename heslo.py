import random
import string

def main():
    print("--- 🔐 GENERÁTOR SUPER-HESEL 🔐 ---")

    try:
        delka = int(input("Jak dlouhé heslo chcete? (doporučuji aspoň 12): "))
    except ValueError:
        print("❌ Musíte zadat číslo!")
        return

    if delka < 4:
        print("⚠️ To je moc krátké! Bezpečné heslo má aspoň 8 znaků.")
        return

    pismena = string.ascii_letters  
    cisla = string.digits          
    znaky = string.punctuation      

    vsechno = pismena + cisla + znaky

    heslo = "".join(random.choices(vsechno, k=delka))

    print("-" * 30)
    print(f"✨ Vaše nové bezpečné heslo: {heslo}")
    print("-" * 30)
    print("Tip: Heslo si hned uložte do správce hesel, tohle si nezapamatujete! 😄")

if __name__ == "__main__":
    main()