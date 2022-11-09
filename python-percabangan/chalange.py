print('Masukan nilai mata kuliah')
agama = input('Masukan nilai matkul agama (0-100)')
ld = input('Masukan nilai matkul logika diskrti (0-100)')
pdp = input('Masukan nilai matkul pemrograman dasar praktek (0-100)')
pdt = input('Masukan nilai matkul pemrograman dasar teori(0-100)')
bing = input('Masukan nilai matkul bahasa inggris (0-100)')
ttki = input('Masukan nilai matkul tata tulis karya ilmiah (0-100)')
pti = input('Masukan nilai matkul pengantar ti (0-100)')
pkn = input('Masukan nilai matkul pancasila (0-100)')
sd = input('Masukan nilai matkul sistem digital (0-100)')

total = int(agama) + int(ld) + int(pdp) + int(pdt) + int(bing) + int(
    ttki) + int(pti) + int(pkn) + int(sd)
average = total / 9
print('Nilai rata-rata =', average)
