import openpyxl
import time
import os
import sys

sciezka = r'C:\Users\mikol\Downloads\produkty.xlsx'


workbook = openpyxl.load_workbook(sciezka)
arkusz = workbook.active


# KONFIGURACJA
CLIENT_ID = input("Podaj Client_ID: ")
CLIENT_SECRET = input("Podaj Client_secret: ")
os.system('cls')
time.sleep(1)

# Potwierdzenia
if CLIENT_ID == "" or CLIENT_SECRET == "":
    print("Client_id i Client_secret: Jest puste, skrypt nie zadziała")
    sys.exit()
else:
    print("Client_id:", CLIENT_ID)
    print("Client_Secret:", CLIENT_SECRET)
    print("---")


for wiersz in arkusz.iter_rows(min_row=2, values_only=True):
    tytul, opis, cena, ilosc = wiersz
    print("Tytuł:", tytul)
    print("Opis:", opis)
    print("Cena:", cena)
    print("Ilość:", ilosc)
    print("---")


#FUNKCJE




#KOD
