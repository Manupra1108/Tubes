from read_csv import read_csv
from fungsi import baris,length,konso

def IsValid(nama,kategori,tahun,harga,stok_awal):
    # Melakukan validasi terhadap masukan nama,kategori,tahun,harga,stok_awal    
    if nama == '':
        kondisi = False
    else:
        if kategori == '':
            kondisi = False
        else:
            kondisi_tahun = True
            if tahun == '':
                kondisi_tahun = False
            else:
                for i in tahun:
                    if not(i >= '0' and i<='9') or i=='':
                        kondisi_tahun = False
                        break
            if kondisi_tahun == False:
                kondisi = False
            else:
                kondisi_harga = True
                if harga == '':
                    kondisi_harga = False
                else:
                    for i in harga:
                        if not(i >= '0' and i<='9') or i=='':
                            kondisi_harga = False
                            break
                if kondisi_harga == False:
                    kondisi = False
                else:
                    kondisi_stok = True
                    if stok_awal == '':
                        kondisi_stok = False
                    else:
                        for i in stok_awal:
                            if not(i>='0' and i<='9') or i=='':
                                kondisi_stok = False
                                break
                    if kondisi_stok == False:
                        kondisi = False
                    else:
                        kondisi = True
    return(kondisi)

def id_game_max(data):
    id_game = []
    for i in range(1,length(data)):
        for j in range(1):
            konso(id_game,data[i][j])
    game_int = ''
    T_game_int = [0 for i in range(length(id_game))]
    j = 0
    for i in range (length(id_game)):
        arr = id_game[i]
        terminated_id = False
        while not(terminated_id):
            if arr[j] == "0" or arr[j]=="G":
                j +=1
            else:
                while (j<=length(arr)-1):
                    game_int += arr[j]
                    j +=1
                T_game_int[i] = int(game_int)
                game_int = ''
                j = 0
                terminated_id = True
    imax = 0
    for i in range(length(T_game_int)):
        if T_game_int[i] > T_game_int[imax]:
            imax = i
    idgame_max = id_game[imax]
    return(idgame_max)

def tambah_game(data):
    # Menginput nama,kategori,tahun,harga,stok_awal
    # Menambahkan data dengan [id,nama,kategori,tahun,harga,stok_awal] 
    Cond = False
    while not(Cond):
        nama = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")
        if not(IsValid(nama,kategori,tahun,harga,stok_awal)):
            print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO")
        else:
            Cond = True
    id_game = id_game_max(data)
    id_kode = ''
    id_kode_new = ''  
    id_number = ''
    Terminated = False
    i = 0
    if id_game == 'game_id':
        id = 'G001'
    else:
        while(not(Terminated)):
            # Misal G001 -> Dipisah menjadi G00 dan 1
            if id_game[i] == "G" or id_game[i] == "0":
                id_kode += id_game[i]
                i +=1
            else:
                while (i<=length(id_game)-1):
                    id_number += id_game[i]
                    i +=1
                Terminated = True
        if id_number== "9" or id_number =="99":
            # G009 -> G010
            # G099 -> G100
            for j in range(length(id_kode)-1):
                id_kode_new += id_kode[j]
            id = id_kode_new + str(int(id_number)+1)
        else:
            id = id_kode + str(int(id_number)+1)
    T = [id,nama,kategori,tahun,harga,stok_awal]
    konso(data,T)
    print(f"Selamat! Berhasil menambahkan game {nama}.")
    #data += [T]
    return(data)

if __name__ == '__main__':
    data_game_csv = read_csv("game.csv")
    while 1:
        print(id_game_max(data_game_csv))
        print(tambah_game(data_game_csv))
