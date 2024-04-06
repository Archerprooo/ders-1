import re,json,ast

def menu():
    print("╔═══════════════════════════╗")
    print("║  REHBER UYGULAMASI        ║")
    print("║                           ║")
    print("║  1-Kişi ekle              ║")
    print("║  2-Listele                ║")
    print("║  3-Ara                    ║")
    print("║  4-Kişi Düzelt            ║")
    print("║  5-Sil                    ║")
    print("╚═══════════════════════════╝")

    secim = input("seciminizi giriniz : ")
    if secim=="1":
        listele()
        kisiEkle()
        listele()
        menu()
    if secim=="2":
        listele()
        menu()
    if secim=="3":
        ara()
        menu()
    if secim=="4":
        duzelt()
        listele()
        menu()
    if secim=="5":
        sil()
        listele()
        menu()
def kisiEkle():
    dosya = open("rehber.txt","a")
    print("╔═════════════╗")
    print("║ Kişi Ekleme ║")
    print("╚═════════════╝")
    ad = input("Kaydedilecek ad ve soyad :")
    numara = input("Kaydedilecek numara      :")
    dosya.write(f'{str({"ad":ad,"numara":numara})},')
    dosya.close()

def listele():
    try:
        with open("rehber.txt", "r") as dosya:
            okunan = dosya.read()
        print("╔════════════════╗")
        print("║ Kişi Listeleme ║")
        print("╚════════════════╝")

        cevirilen = ast.literal_eval(okunan)
        for a in cevirilen:
            print (a)
    except :
        print("Bir hata oluştu")          
def ara():
    with open("rehber.txt", "r") as dosya:
        okunan = dosya.read()
    print("╔══════════╗")
    print("║ Kişi Ara ║")
    print("╚══════════╝")


    cevirilen = ast.literal_eval(okunan)
    aranan = input("Aranan isim nedir?")
    for a in cevirilen:
        if a["ad"]==aranan: print(a)

def duzelt():
    with open("rehber.txt", "r") as dosya:
        okunan = dosya.read()
    print("╔═══════════════════════╗")
    print("║ Kişi Bilgisi Düzeltme ║")
    print("╚═══════════════════════╝")

    cevirilen = ast.literal_eval(okunan)
    aranan = input("Düzeltilecek isim nedir? ")
    dosya.close()
    with open("rehber.txt","w") as dosya:
        for a in cevirilen:
            if a["ad"]==aranan:
                print(a)
                yeniAd = input("Yeni ad nedir? ")
                yeniNumara = input("Yeni numara nedir? ")
                a["ad"]=yeniAd
                a["num"]=yeniNumara
            dosya.write(f"{str(a)},")        

def sil():
    with open("rehber.txt", "r") as dosya:
        okunan = dosya.read()
    print("╔════════════╗")
    print("║ Kişi Silme ║")
    print("╚════════════╝")

    cevirilen = ast.literal_eval(okunan)
    aranan = input("Silinecek isim nedir? ")
    dosya.close()
    with open("rehber.txt","w") as dosya:
        for a in cevirilen:
            if a["ad"]!=aranan:
                dosya.write(f"{str(a)},")

menu()