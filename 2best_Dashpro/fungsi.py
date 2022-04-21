def length(x):
    # mencari panjang dari suatu string
    len = 0
    for i in x:
        len +=1
    return(len)

def konso(data1,data2):
    data1 += [data2]
    return(data1)

def read_csv(x,folder_name):
    data_csv = []
    # Membaca data csv
    try:
        filename = x
        count = 0
        i = 0
        if filename == 'game.csv':
            f = open(f"{folder_name}"+"/game.csv",'r')
            kolom = 6 
        elif filename == 'riwayat.csv':
            f = open(f"{folder_name}"+"/riwayat.csv",'r')
            kolom = 5
        elif filename == 'kepemilikan.csv':
            f = open(f"{folder_name}"+"/kepemilikan.csv",'r')
            kolom = 2
        elif filename == 'user.csv':
            f = open(f"{folder_name}"+"/user.csv",'r')
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
                                    konso(data_csv,Tarr)
                                    #data_csv += [Tarr]
                                    Terminated = True
                                    count = 0
                                    i = 0
        f.close()
        return(data_csv)
    except IOError:
        if filename == 'game.csv':
            f1 = open(f"{folder_name}"+"/game.csv",'r')
            f1.writelines("id;nama;kategori;tahun_rilis;harga;stok")
            f1.writelines("\n")
            f1.close()
            data_csv = [["id","nama;kategori","tahun_rilis","harga","stok"]]
            return(data_csv)
        elif filename == 'riwayat.csv':
            f1 = open(f"{folder_name}"+"/riwayat.csv",'r')
            f1.writelines("game_id;nama;harga;user_id;tahun_beli")
            f1.writelines("\n")
            f1.close()
            data_csv = [["game_id","nama","harga","user_id","tahun_beli"]]
            return(data_csv)
        elif filename == 'user.csv':
            f1 = open(f"{folder_name}"+"/user.csv",'r')
            f1.writelines("id;username;nama;password;role;saldo")
            f1.writelines("\n")
            f1.close()
            data_csv = [["id","username","nama","password","role","saldo"]]
            return(data_csv)
        elif filename == 'kepemilikan.csv':
            f1 = open(f"{folder_name}"+"/kepemilikan.csv",'r')
            f1.writelines("game_id;user_id")
            f1.writelines("\n")
            f1.close()
            data_csv = [["game_id","user_id"]]
            return(data_csv)
        else:    
            pesan = (f'Maaf file {x} tidak ada')
            print(pesan)
            return
