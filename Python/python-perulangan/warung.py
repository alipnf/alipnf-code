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
Es jeru1k = 4k
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
pcs_ma = []
pcs_mi = []
harga_ma = []
harga_mi = []
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
            harga_b = pcs_b * 15000
            makanan.append("Bakso")
            pcs_ma.append(pcs_b)
            harga_ma.append(harga_b)
        elif (makan == "2"):
            pcs_m = int(input('pesan berapa : '))
            harga_m = pcs_m * 10000
            makanan.append("Mie ayam")
            pcs_ma.append(pcs_m)
            harga_ma.append(harga_m)
        elif (makan == "3"):
            pcs_a = int(input('pesan berapa : '))
            harga_a = pcs_a * 13000
            makanan.append("Ayam bakar")
            pcs_ma.append(pcs_a)
            harga_ma.append(harga_a)
        elif (makan == "4"):
            pcs_n = int(input('pesan berapa : '))
            harga_n = pcs_n * 10000
            makanan.append("Nasi pecel")
            pcs_ma.append(pcs_n)
            harga_ma.append(harga_n)
        else :
            print("")
            print('=========================')
            print('input salah')
            print('=========================')
            print("")
    elif (menu == "2"):
        print("")
        print('=========================')
        print('Pilih minuman\n1. Es teh \n2. Es jeruk \n3. Teh anget \n4. Jeruk anget')
        print('=========================')
        print("")
        minum = input('Pilih minuman : ')
        if (minum == "1"):
            pcs_et = int(input('pesan berapa : '))
            harga_et = pcs_et * 3000
            minuman.append("Es teh")
            pcs_mi.append(pcs_et)
            harga_mi.append(harga_et)
        elif (minum == "2"):
            pcs_ej = int(input('pesan berapa : '))
            harga_ej = pcs_ej * 4000
            minuman.append("Es jeruk")
            pcs_mi.append(pcs_ej)
            harga_mi.append(harga_ej)
        elif (minum == "3"):
            pcs_ta = int(input('pesan berapa : '))
            harga_ta = pcs_ta * 3000
            minuman.append("Teh anget")
            pcs_mi.append(pcs_ta)
            harga_mi.append(harga_ta)
        elif (minum == "4"):
            pcs_ja = int(input('pesan berapa : '))
            harga_ja = pcs_ja * 4000
            minuman.append("Jeruk anget")
            pcs_mi.append(pcs_ja)
            harga_mi.append(harga_ja)

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
        ma = 0
        mi = 0
        while (ma < len(makanan)):
            print("")
            print(pcs_ma[ma], "Pesanan", '', '', '', '' , makanan[ma])
            ma+=1
        while (mi < len(minuman)):
            print(pcs_mi[mi], "Pesanan", '', '', '', '' , minuman[mi])                        
            mi+=1
    elif (menu == "4"):
        print("")
        print("Pcs | Pesanan", '|' , "Harga")
        print('=========================')
        hma = 0
        hmi = 0
        while (hma < len(makanan)):
            print(pcs_ma[hma], '', '', '', '', makanan[hma], '', '', '', '', harga_ma[hma])
            hma+=1
        while (hmi < len(minuman)):
            print(pcs_mi[hmi], '', '', '', '', minuman[hmi], '', '', '', '', harga_mi[hmi])
            hmi+=1            
        print('=========================')
        print("")
        total_ma = sum(harga_ma)
        total_mi = sum(harga_mi)
        print("Total biaya", total_ma+total_mi)
        
    else:
        status = ("off")