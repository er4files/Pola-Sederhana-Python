def pola_piramida_terbalik(tinggi):
    for i in range(tinggi, 0, -1):
        print(' ' * (tinggi - i) + '*' * (2 * i - 1))

tinggi_piramida_terbalik = int(input("Masukkan tinggi piramida terbalik: "))
pola_piramida_terbalik(tinggi_piramida_terbalik)
