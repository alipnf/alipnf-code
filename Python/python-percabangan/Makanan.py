pesanan = "y"
totalHarga = 0
print("1.bakso \t10k\n2.mi ayam \t9k\n3.es teh \t3k\n")
while (pesanan == "y"):
    pilih_Menu = int(input("masukkan pilihan menu :"))
    if (pilih_Menu == 1):
        totalHarga += 10000
    elif (pilih_Menu == 2):
        totalHarga += 9000
    elif (pilih_Menu == 3):
        totalHarga += 3000
    else:
        print("error")
    pesanan = input("apakah anda ingin menambah pesanan? (y/n)")
    if (pesanan != "y"):
        pesanan = "no"
print("yang harus dibayar : ", totalHarga)
