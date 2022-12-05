"""buatlah sistem warung dengan menu pilihan 
1. Pesan makan
2. Daftar pesanan
3. Total pembayaran
4. Keluar

di menu makan ada makanan,minuman dan gorengan
makanan :
Bakso = 15k
Mie ayam = 10k
Ayam bakar = 13k
Nasi pecel = 10k
minuman :
Es teh = 3k
Es jeruk = 4k
Teh anget = 3k
Jeruk anget = 4k
gorengan ;
Tahu = 2k
Tempe = 2k
Bakwan = 2k
"""
makanan = []
minuman = []
gorengan = []
pcs = []
harga = []
status = ("on")

while status=="on":
    print("")
    print('=========================')
    print('Pilih menu \n1. Pesan Makan \n2. Pesan minum \n3. Daftar pesanan \n4. Total Pembayaran \n5. Keluar')
    print('=========================')
    print("")
    menu = input('Pilih menu : ')
    if (menu == "1"):
        print("")
        print('=========================')
        print('Pilih makanan\n1. Bakso \n2. Mie ayam \n3. Ayam bakar \n4. Nasi pecel')
        print('=========================')
        print("")
        makan = input('Pilih makanan : ')
        if (makan == "1"):
            pcs_b = int(input('pesan berapa : '))
            harga_b = pcs_b * 150000
            makanan.append("Bakso")
            pcs.append(pcs_b)
            harga.append(harga_b)
        elif (makan == "2"):
            pcs_m = int(input('pesan berapa : '))
            harga_m = pcs_m * 150000
            makanan.append("Mie ayam")
            pcs.append(pcs_m)
            harga.append(harga_m)
        elif (makan == "3"):
            makanan.append("Ayam bakar")
        elif (makan == "4"):
            makanan.append("Nasi pecel")
        else :
            print("")
            print('=========================')
            print('input salah')
            print('=========================')
            print("")
    elif (menu == "2"):
        print("")
        print('=========================')
        print('Pilih makanan\n1. Bakso \n2. Mie ayam \n3. Ayam bakar \n4. Nasi pecel')
        print('=========================')
        print("")
        makan = input('Pilih makanan : ')
        if (makan == "1"):
            minuman.append("Es teh")
        elif (makan == "2"):
            minuman.append("Es jeruk")
        elif (makan == "3"):
            minuman.append("Teh anget")
        elif (makan == "4"):
            minuman.append("Jeruk anget")
        else :
            print("")
            print('=========================')
            print('input salah')
            print('=========================')
            print("")
    elif (menu == "3"):
        print("")
        print("Pesanan", '|', "Makan/minum")
        print('=========================')
        m = 0
        while (m < len(makanan)):
            print("")
            print(pcs[m], "Pesanan", '', '', '', '' , makanan[m])
            m+=1
    elif (menu == "4"):
        print("")
        print("Pesanan", '|', "Pcs", '|' , "Harga")
        print('=========================')
        h = 0
        while (h < len(harga)):
            print("")
            print()
            print(pcs[h], '', '', '', '', makanan[h], '', '', '', '', harga[h])
            h+=1

        
    else:
        status = ("off")