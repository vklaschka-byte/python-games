import streamlit as st
import random

# Nadpis stránky
st.title("🎮 Kámen, Nůžky, Papír")
st.write("Zahraj si proti počítači! Vyber svou zbraň 👇")

# Možnosti
moznosti = ["kámen", "nůžky", "papír"]

# Vytvoříme 3 sloupce vedle sebe pro tlačítka
col1, col2, col3 = st.columns(3)

# Proměnná pro volbu hráče (zatím prázdná)
hrac_vyber = None

# Tlačítka (každé ve svém sloupci)
with col1:
    if st.button("✊ KÁMEN"):
        hrac_vyber = "kámen"
with col2:
    if st.button("✌️ NŮŽKY"):
        hrac_vyber = "nůžky"
with col3:
    if st.button("✋ PAPÍR"):
        hrac_vyber = "papír"

# Pokud si hráč vybral (kliknul na tlačítko), hrajeme!
if hrac_vyber:
    st.divider() # Čára pro oddělení
    
    # Počítač vybírá
    pocitac_vyber = random.choice(moznosti)
    
    # Zobrazíme volby
    col_a, col_b = st.columns(2)
    with col_a:
        st.info(f"Ty: **{hrac_vyber.upper()}**")
    with col_b:
        st.warning(f"Počítač: **{pocitac_vyber.upper()}**")

    # Vyhodnocení (stejná logika jako v terminálu)
    if hrac_vyber == pocitac_vyber:
        st.header("🤝 Je to REMÍZA!")
    
    elif (hrac_vyber == "kámen" and pocitac_vyber == "nůžky") or \
         (hrac_vyber == "nůžky" and pocitac_vyber == "papír") or \
         (hrac_vyber == "papír" and pocitac_vyber == "kámen"):
        st.success("🎉 VYHRÁLA JSI! Gratuluji!")
        st.balloons() # Efekt balónků! 🎈
    else:
        st.error("💀 PROHRÁLA JSI... Zkus to znovu.")