import wikipedia

def main():
    print("--- 🧠 VŠEZNÁLEK (Wikipedie do kapsy) 🧠 ---")
    
    wikipedia.set_lang("cs")

    while True:
        print("\n" + "="*40)
        dotaz = input("O čem chceš vědět? (nebo 'konec'): ").strip()

        if dotaz.lower() == "konec":
            break
            
        if not dotaz:
            continue

        print("🔍 Hledám...")

        try:
            stranka = wikipedia.page(dotaz)
            
            print(f"\n📖 Téma: {stranka.title}")
            print(f"🔗 Odkaz: {stranka.url}")
            print("-" * 20)
            
            shrunti = wikipedia.summary(dotaz, sentences=5)
            print(shrunti)

        except wikipedia.exceptions.DisambiguationError as e:
            print("⚠️ To je moc obecné! Myslel jsi třeba tohle?")
            print(e.options[:5])
            
        except wikipedia.exceptions.PageError:
            print("❌ Smůla, o tomhle Wikipedie nic neví.")
            
        except Exception as e:
            print(f"Chyba: {e}")

if __name__ == "__main__":
    main()