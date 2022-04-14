def read_csv(x):
    data_csv = []
    # Membaca data csv
    try:
        filename = x
        f = open(filename,'r')
        count = 0
        i = 0
        if filename == 'game.csv':    
            kolom = 6
        elif filename == 'riwayat.csv':
            kolom = 5
        elif filename == 'kepemilikan.csv':
            kolom = 2
        elif filename == 'user.csv':
            kolom = 6    
        for line in f:
            Tarr = ['' for i in range(kolom)]
            arr = line
            Terminated = False
            while not(Terminated):
                # Parsing
                    if arr[i] != ";":
                        Tarr[count] += arr[i]
                        i +=1
                    else:
                        count +=1
                        i+=1
                        if count == kolom - 1:
                            while (not(Terminated)):
                                # Parsing
                                if arr[i] != "\n":
                                    Tarr[count] += arr[i]
                                    i +=1
                                else:
                                    data_csv += [Tarr]
                                    Terminated = True
                                    count = 0
                                    i = 0
        f.close()
        return(data_csv)
    except IOError:
        pesan = (f'Maaf file {x} tidak ada')
        return(pesan)


# Program buat nyobain fungsinya jalan apa enggak
x = input() #Masukkan nama file
print(f"Berikut merupakan data dari file {x}")
print()
print(read_csv(x))