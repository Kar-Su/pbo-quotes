"""PANDUAN UTAMA
data_quotes.py

Tempat penyimpanan data quotes
dimana setiap jenis quote ada 10 quote (Jangan lebih dan kurang).


Variable:
    agama (func)        : Tempat penyimpanan quote agama
    percintaan (func)   : Tempat penyimpanan quote percintaan
    politik (func)      : Tempat penyimpanan quote politik
"""

"""PANDUAN 1

fungsi agama, percintaan, politik memiliki logic yang sama
yang membedakannya hanyalah isi quotesnya.

Fungsi yang disebutkan tadi nantinya akan digunakan di quotes.py/PANDUAN1
yang namanya akan berubah (di assign) kedalam variable yang bernama data
Setelah itu nantinya pada quotes.py/PANDUAN2 variable data akan dipanggil.

Logicnya menggunakan match case untuk membuat kondisi khusus sesuai dengan angka_random yang sudah digenerate

"""

def agama(angka_random):
    match angka_random:
        case 1:
            print("Kadang Allah nggak langsung kasih yang kita mau, karena Dia tahu yang kita mau belum tentu kita butuh. Tapi yang pasti, setiap penundaan dari Allah itu selalu ada kebaikan di baliknya.")
        case 2:
            print("Tenang aja, nggak semua orang harus ngerti perjuanganmu. Cukup Allah yang tahu seberapa keras kamu berusaha dan seberapa sering kamu berdoa diam-diam.")
        case 3:
            print("Tenang aja, nggak semua orang harus ngerti perjuanganmu. Cukup Allah yang tahu seberapa keras kamu berusaha dan seberapa sering kamu berdoa diam-diam.")
        case 4:
            print("Jangan pernah merasa sendirian, karena Allah selalu ada di sampingmu, bahkan saat kamu merasa paling jauh dari-Nya.")
        case 5:
            print("Hidup ini penuh ujian, tapi ingatlah bahwa setiap ujian dari Allah itu ada maksud baiknya. Mungkin Dia ingin menguatkanmu atau mengajarkanmu sesuatu yang berharga.")


def percintaan(angka_random):
    match angka_random:
        case 1:
            print("Orang yang benar-benar mencintaimu tidak akan membuatmu merasa harus berjuang sendirian")
        case 2:
            print("Cinta sejati tidak mencari kesempurnaan, tapi menerima kekurangan dengan tulus")
        case 3:
            print("Jatuh cinta itu mudah, tapi menjaga cinta itu seni")
        case 4:
            print("Cinta bukan buta, tapi membuat kita melihat dengan cara yang berbeda")
        case 5:
            print("Ketika kamu mencintai seseorang, kamu mencintai versinya yang sebenarnya, bukan yang kamu harapkan")


def politik(angka_random):
    match angka_random:
        case 1:
            print("Kekuasaan cenderung merusak, dan kekuasaan absolut merusak secara absolut")
        case 2:
            print("Demokrasi adalah dua serigala dan seekor domba yang memilih menu makan malam")
        case 3:
            print("Politik adalah seni mencegah orang ikut campur dalam urusan mereka sendiri")
        case 4:
            print("Seorang politisi memikirkan pemilu berikutnya; seorang negarawan memikirkan generasi berikutnya")
        case 5:
            print("Ketidakpedulian rakyat adalah tiket emas bagi tiran")


"""PANDUAN 2

Fungsi ini tidak menghasilkan apapun karena ada kata pass
Yang dimana kegunaan pass adalah untuk mengisi sebuah fungsi yang kosong

Hal ini berguna ketika di quotes.py/PANDUAN 1 user salah memasukkan jenis quotes
maka data akan di assign dengan fungsi salah yang berarti fungsi kosong.
"""            
def salah():
    pass