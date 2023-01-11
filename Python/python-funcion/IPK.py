# matkul = ["pti", 'ld', 'pd', 'pdd', 'sd', 'ttki', 'agm', 'pcn', 'ing']
# def ipk():
#     if (nilai == 'A'):
#         poin = 4
#     elif (nilai == 'AB'):
#         poin = 3,6
#     elif (nilai == "B"):
#         poin = 3

# # ipk(matkul, nilai, sks)
# print(matkul)
# sks = input(matkul;)
seluruh_nilai = {"Agama": 0, "Pancasila": 0, "TTKI": 0, "Pemrograman Dasar Praktikum": 0, "Pemrograman Dasar Teori": 0,
               "Bahasa Inggris": 0, "Sistem Digital": 0, "Logika Diskrit": 0, "Pengantar Teknik Informatika": 0}
nilai = 0
# input
for a,b in seluruh_nilai.items():
    b = str(input(f"Masukkan nilai {a} : "))
    seluruh_nilai.update({a:b})
if (nilai == 'A'):
    poin = 4
elif (nilai == 'AB'):
    poin = 3,6
elif (nilai == "B"):
    poin = 3

    total+=b
print("\n")
for a,b in seluruh_nilai.items():
    print (f"Nilai mata kuliah {a} adalah {b} ")
print("Total nilai anda adalah : ", total)
print("Rata-rata nilai anda adalah : ", total/len(seluruh_nilai))