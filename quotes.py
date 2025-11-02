"""PANDUAN
quotes.py

Sebuah file utama yang menjalankan quotes generator
user hanya perlu menjalankan main.py
"""

from random import randint
from data_quotes import (agama, percintaan, politik, salah)

def main():
    """PANDUAN UTAMA
    Fungsi main
    
    Sebuah fungsi utama dari quotes generator
    
    variable:
        jenis_quotes(str.lower())   : Sebuah inputan user untuk menentukan jenis quote
        data(func)                  : data quote dari data_quotes.py yang disesuaikan dengan jenis quote
        iterasi(int)                : Sebuah inputan user untuk menentukan berapa banyak quote yang akan ditampilkan
        random_generator(int)       : Sebuah angka integer yang ditentukan dari random generator(randint)
    """
    

    """PANDUAN 1
    
    Pada section dibawah ini berguna untuk memfilter data mana yang kita pakai
    menggunakan switch case. Kegunaan switch case mirip seperti IF-ELSE.
    data berupa sebuah fungsi yang ada di file data_quotes.py yang sudah di import di awal line
    
    Contoh penggunaan data (range 1-5):
        data(1), data(5)

    Kegunaan dari case _ adalah sebagai kasus selain dari yang sudah kita definisikan.
    Ketika user salah menginputkan jenisnya maka otomatis akan langsung keluar dari program.
    """
    jenis_quotes = input("Masukkan kategori quotes (Agama, Percintaan, Politik): ").lower()
    match jenis_quotes:
        case "agama":
            data = agama
        case "percintaan":
            data = percintaan
        case "politik":
            data = politik
        case _:
            data = salah
            print("Jenis yang anda ketikkan tidak ada [agama, percintaan, politik]")
            exit()
    
    
    """PANDUAN 2
    
    Pada section dibawah ini berguna untuk melakukan perulangan sesuai kemauan dari user
    variable iterasi merupakan jumlah perulangan yang akan dilakukan (Perlu dirubah ke int dulu)
    
    Kegunaan dari randint(1, 5) yaitu menghasilkan sebuah angka acak dari 1,2,3,4,5
    """
    iterasi = int(input("Jumlah quotes yang ingin anda tampilkan: "))
    for i in range(iterasi):
        print(f"Quotes ke {i + 1}")
        random_generator = randint(1,5)
        print(data(random_generator))
    

# Menjalankan fungsi main
print("Topik 2 - Quotes Generator")
main()