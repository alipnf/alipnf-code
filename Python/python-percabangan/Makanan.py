pesanan = "y"
totalHarga = 0
print("1.\tbakso\t10k\n2.\mi ayam\t9k\n3.\es teh\t3k\n")
while (pesanan == "y"):
    pilihMenu = int(input("masukkan pilihan menu"))
    if (pilihMenu == 1):
        totalHarga += 10000
        print("ent")
    elif (pilihMenu == 2):
        totalHarga += 9000
    elif (pilihMenu == 3):
        totalHarga += 3000
    else:
        print("error")
    pesanan = input("apakah anda ingin menambah pesanan? (y/n)")
    if (pesanan != "y"):
        pesanan = "no"
print("yang harus dibayar : ", totalHarga)
