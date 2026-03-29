import random
import time
import os
from collections import deque

def vycistit():
    os.system('cls' if os.name == 'nt' else 'clear')

def vytvor_bludiste(sirka, vyska):
    
    maze = [["#" for _ in range(sirka)] for _ in range(vyska)]
    return maze

def vykresli(maze, cesta=[]):
    vycistit()
    print("--- 🗺️ GENERÁTOR A ŘEŠITEL BLUDIŠTĚ 🗺️ ---")
    for r in range(len(maze)):
        radek = ""
        for c in range(len(maze[0])):
            if (r, c) in cesta:
                radek += ". " 
            else:
                radek += maze[r][c] + " "
        print(radek)
    print("------------------------------------------")

def najdi_cestu(maze, start, cil):
    vyska = len(maze)
    sirka = len(maze[0])
    fronta = deque([(start, [start])])
    navstiveno = {start}

    while fronta:
        (r, c), cesta = fronta.popleft()

        if (r, c) == cil:
            return cesta

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < vyska and 0 <= nc < sirka and \
               maze[nr][nc] == " " and (nr, nc) not in navstiveno:
                navstiveno.add((nr, nc))
                fronta.append(((nr, nc), cesta + [(nr, nc)]))
    return None

def main():

    maze = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["S", " ", " ", "#", " ", " ", " ", " ", " ", "#"],
        ["#", "#", " ", "#", " ", "#", "#", "#", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", "#", "#", "#", " ", "#", " ", "#"],
        ["#", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", " ", " ", "C"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    ]
    
    start = (1, 0)
    cil = (7, 9)
    
    vykresli(maze)
    print("\nStiskni Enter a já najdu cestu...")
    input()
    
    print("🔍 Hledám cestu...")
    cesta = najdi_cestu(maze, start, cil)
    
    if cesta:
        for i in range(len(cesta) + 1):
            vykresli(maze, cesta[:i])
            time.sleep(0.1)
        print(f"\n✨ Cesta nalezena! Délka: {len(cesta)} kroků.")
    else:
        print("\n❌ Cesta neexistuje.")

if __name__ == "__main__":
    main()