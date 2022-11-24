print ('r = jari-jari \nd = diameter')
sisi = input('masukan tipe (r/d) :')
if (sisi == "r"):
    r = int(input('masukan jari-jari :'))
    if (r%7==0):
        Luas = 22/7*r*r
        print ("kelipatan")
    else :
        Luas = 3.14*r*r
        print (Luas)
elif (sisi == "d"):
    d = int(input('masukan diameter :'))
    Luas = 3.14*d
    print (Luas)
else:
    ('Pilih tipe')