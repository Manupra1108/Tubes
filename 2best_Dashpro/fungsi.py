def baris(x):
    # Mencari jumlah baris pada sebuah data matriks
    baris = 0
    for i in x:
        baris += 1
    return(baris)

def length(x):
    # mencari panjang dari suatu string
    len = 0
    for i in x:
        len +=1
    return(len)

def konso(data1,data2):
    data1 += [data2]
    return(data1)