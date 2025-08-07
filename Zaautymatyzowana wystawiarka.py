import openpyxl

sciezka = r'E:\Prywatne\programowanie\Prywatne\Python\zaautomatyzowanie\produkty.xlsx'


workbook = openpyxl.load_workbook(sciezka)
arkusz = workbook.active


for wiersz in arkusz.iter_rows(min_row=2, values_only=True):
    tytul, opis, cena, ilosc = wiersz
    print("Tytuł:", tytul)
    print("Opis:", opis)
    print("Cena:", cena)
    print("Ilość:", ilosc)
    print("---")
