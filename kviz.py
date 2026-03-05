import time

def main():
    print("--- 🧠 VĚDOMOSTNÍ KVÍZ (Trivia Quiz) 🧠 ---")
    print("Otestuj své znalosti! Za každou správnou odpověď získáš bod.")
    print("---------------------------------------------------------")

    otazky = [
        {
            "otazka": "Jaký je nejvyšší vrchol světa?",
            "moznosti": ["A) K2", "B) Mount Everest", "C) Mont Blanc", "D) Kilimandžáro"],
            "spravne": "B"
        },
        {
            "otazka": "Ve kterém roce začala druhá světová válka?",
            "moznosti": ["A) 1914", "B) 1939", "C) 1945", "D) 1989"],
            "spravne": "B"
        },
        {
            "otazka": "Jaký je chemický vzorec pro vodu?",
            "moznosti": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
            "spravne": "B"
        },
        {
            "otazka": "Kdo napsal hru Romeo a Julie?",
            "moznosti": ["A) Karel Čapek", "B) Victor Hugo", "C) William Shakespeare", "D) J.K. Rowling"],
            "spravne": "C"
        },
        {
            "otazka": "Která planeta sluneční soustavy je nejblíže Slunci?",
            "moznosti": ["A) Venuše", "B) Mars", "C) Merkur", "D) Země"],
            "spravne": "C"
        }
    ]

    skore = 0

    for i, q in enumerate(otazky, 1):
        print(f"\nOtázka {i}/{len(otazky)}:")
        print(q["otazka"])
        
        for moznost in q["moznosti"]:
            print(moznost)

        odpoved = input("Tvoje odpověď (A, B, C, D): ").upper()

        if odpoved == q["spravne"]:
            print("✅ Správně!")
            skore += 1
        else:
            print(f"❌ Špatně! Správná odpověď byla {q['spravne']}.")

        time.sleep(1)

    # Vyhodnocení
    print("\n===============================")
    print("🏁 KONEC KVÍZU 🏁")
    print(f"Tvoje skóre: {skore} z {len(otazky)}")

    procenta = (skore / len(otazky)) * 100
    if procenta == 100:
        print("Hodnocení: 🏆 Naprostý expert!")
    elif procenta >= 60:
        print("Hodnocení: 👍 Velmi dobrý výsledek!")
    else:
        print("Hodnocení: 📚 Musíš ještě trochu studovat.")
    print("===============================\n")

if __name__ == "__main__":
    main()