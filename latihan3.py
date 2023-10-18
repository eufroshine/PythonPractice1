#input nilai
a = input("Masukan Nilai a : ")
b = input("Masukan Nilai b : ")

#cetak nilai
print("Variable a = ", a)
print("Variable b = ", b)

#cetak hasil operasi
print("Hasil Penggabungan {0} & {1} = ".format(a,b)+(a+b))

#konversi nilai variable
a=int(a)
b=int(b)
print("Hasil Penjumlahan {1} + {0} = %d".format(a,b) %(a+b))
print("Hasil Pembagian {1}/{0} = %d".format(a,b) %(a/b))
