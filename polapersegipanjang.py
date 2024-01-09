def pola_persegi_panjang(panjang, lebar):
    for i in range(lebar):
        print('*' * panjang)

panjang_persegi_panjang = int(input("Masukkan panjang persegi panjang: "))
lebar_persegi_panjang = int(input("Masukkan lebar persegi panjang: "))
pola_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang)
