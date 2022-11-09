print(
    'pilih rumus \n1. Persegi \n2. Persegi panjang \n3. Segitiga \n4. Jajar genjang \n5. Lingkaran'
)
rumus = input('pilih rumus di atas :')
if (rumus == '1'):
    sisi = int(input('masukan sisi :'))
    Luas = sisi * sisi
    print('luasnya =', Luas)
elif (rumus == '2'):
    panjang = int(input('masukan panjang :'))
    lebar = int(input('masukan lebar :'))
    Luas = panjang * lebar
    print(Luas)
elif (rumus == '3'):
    alas = int(input('masukan alas :'))
    tinggi = int(input('masukan tinggi :'))
    Luas = 1 / 2 * alas * tinggi
    print('luasnya =', Luas)
elif (rumus == '4'):
    alas = int(input('masukan alas :'))
    tinggi = int(input('masukan tinggi :'))
    Luas = alas * tinggi
    print(Luas)
elif (rumus == '5'):
    r = int(input('masukan jari jari :'))
    if (r % 7 == 1):
        Luas = 22 / 7 * r
        print(Luas)
    else:
        Luas = 3.14 * r
        print(Luas)
