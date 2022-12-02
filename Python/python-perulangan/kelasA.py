list1 = []
list2 = []
status = "Y"
while (status == "Y"):
    print ('Menu \n1. Tampil Data \n2. Tambah Data \n3. Keluar aplikasi')
    menu = input('pilih menu :')
    if (menu == '1'):
        print ("")
        print ("DATA")
        x=0
        while (x < len(list1)):
            print (list1[x], list2[x])
            x+=1
        print ('')
    elif (menu == '2'):
        list1.append(input("masukan nama : "))
        list2.append(input("masukan Nim : "))
    elif (menu == '3'):
        print ('berhasil kelluar')
        status = "N"
