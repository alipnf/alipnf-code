presensi = int(
    input('masukan berapa presensi dengan total 16 kali pertemuan : '))
tugas = int(input('masukan nilai (0-100) :'))
UTS = int(input('masukan nilai (0-100) :'))
UAS = int(input('masukan nilai (0-100): '))
etika = int(input('masukan nilai (0-100) :'))

nilai = (presensi / 16 * 0.1 * 100) + (tugas * 0.2) + (UTS * 0.3) + (etika *
                                                                     0.15)
print(nilai)
