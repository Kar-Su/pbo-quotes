"""PANDUAN
data_quotes.py

Tempat penyimpanan data quotes
dimana setiap jenis quote ada 10 quote (Jangan lebih dan kurang).


Variable:
    agama (list[str...])        : Tempat penyimpanan quote agama
    percintaan (list[str...])   : Tempat penyimpanan quote percintaan
    politik (list[str...])      : Tempat penyimpanan quote politik
"""


"""@@@
Task 1

Mencari 10 quote agama dan memasukkannya kedalam list
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

"""@@@
Task 2

Mencari 10 quote percintaan dan memasukkannya kedalam list
"""
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

"""@@@
Task 3

Mencari 10 quote politik dan memasukkannya kedalam list
"""
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
            
def salah(angka_random):
    pass