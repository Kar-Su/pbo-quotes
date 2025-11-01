"""PANDUAN
quotes.py

Sebuah file utama yang menjalankan quotes generator
user hanya perlu menjalankan main.py
"""

from random import randint
from data_quotes import (agama, percintaan, politik)

def main():
    """PANDUAN
    Fungsi main
    
    Sebuah fungsi utama dari quotes generator
    
    variable:
        jenis_quotes(str.lower())   : Sebuah inputan user untuk menentukan jenis quote
        data(list[str...])          : data quote dari data_quotes.py yang disesuaikan dengan jenis quote
        iterasi(int)                : Sebuah inputan user untuk menentukan berapa banyak quote yang akan ditampilkan
        random_generator(int)       : Sebuah angka integer yang ditentukan dari random generator(randint)
    """
    
    
    """@@@
    Task 4
    
    Membuat sebuah kode untuk menentukan jenis quote menggunakan switch case,
    dan menentukan data mana yang akan dipakai,
    
    Fitur:
        Huruf besar dan kecil tidak mempengaruhi hasil inputannya.
        Contoh Agama,AGama,PERCIntaan,politik,POLITIK.
        
    Note:
        Metode boleh diubah, akan tetapi output kerjaannya harus sama.
    """
    jenis_quotes = ...
    match ...:
        case "...":
            data = ...
        case "...":
            data = ...
        case "...":
            data = ...
        case _:
            data = [None]
            print("Jenis yang anda ketikkan tidak ada [agama, percintaan, politik]")
    
    
    """@@@
    Task 5
    
    Membuat sebuah kode untuk menentukan seberapa banyak quote yang muncul.
    
    Fitur:
        Setiap iterasi berjalan, maka quotenya berbeda - beda
        menggunakan random generator(randint)
    """
    iterasi = int(input("Berapa kali iterasi (percobaan acak) ingin dijalankan? "))
    for i in range(iterasi):
        print(f"Quotes ke {i + 1}")
        random_generator = randint(1,5)
        print(data(random_generator))

if __name__ == "__main__":
    """PANDUAN
    if __name__ == "__main__":
    
    Melakukan cek apakah nama file ini di sistem python itu "__main__".
    ketika namanya itu "__main__" maka artinya quotes.py itu merupakan file utama yang sedang dijalankan.
    
    Sehingga ketika quotes.py di import di file lain(contoh.py) maka section if ini tidak akan berjalan.
    
    Magic Variable
        __name__: merupakan nama file di dalam sistem python.
        __main__: merupakan nama file yang sedang dijalankan
    """
    print("Topik 2 - Quotes Generator")
    main()