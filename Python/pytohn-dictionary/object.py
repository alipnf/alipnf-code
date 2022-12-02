mahasiswa = { 1:{
    "Nim" : 202251005,
    "Nama": "Muhammad Alif Nur Firdaus" 
}
,
2: {
    "Nim" : 202251001,
    "Nama": "Jamal"
}
}

x = 1
while (x <= len(mahasiswa)):
    print(f"Nama {mahasiswa[x]['Nama']}")
    x+=1