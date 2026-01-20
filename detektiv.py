import cv2
import os
def main():
    print("--- 🕵️‍♀️ DETEKTIV (Rozpoznání tváří) 🕵️‍♀️ ---")
    img_path = input ("Zadejte název fotky (nař.lidi.jpg): ")
    if not os.path.exists(img_path):
        print("❌ Soubor neexistuje! Nahrajte fotku do složky.")
        return
    img = cv2.imread (img_path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cesta_k_modelu = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cesta_k_modelu)
    print ("🔍 Hledám obličeje...")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    print (f"✅ Nalezeno obličejů: {len(faces)}")
    
    for (x, y, w, h) in faces:
        
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    vystup = "face_" + img_path
    cv2.imwrite(vystup, img)
    print(f"✨ Hotovo! Výsledek uložen jako: {vystup}")

if __name__ == "__main__":
    main()