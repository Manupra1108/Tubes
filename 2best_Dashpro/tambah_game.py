from read_csv import read_csv

def IsValid(nama,kategori,tahun,harga,stok_awal):
    # Melakukan validasi terhadap masukan nama,kategori,tahun,harga,stok_awal    
    if nama == '':
        kondisi = False
    else:
        if kategori == '':
            kondisi = False
        else:
            if tahun == '':
                kondisi = False
            else:
                if harga == '':
                    kondisi = False
                else:
                    if stok_awal == '':
                        kondisi = False
                    else:
                        kondisi = True
    return(kondisi)

def jumlah_baris():
    # Mencari jumlah baris pada data_game_csv
    baris = 0
    for i in data_game_csv:
        baris += 1
    return(baris)

def tambah_game():
    # Menginput nama,kategori,tahun,harga,stok_awal
    # mengeluarkan sebuah array yang berisikan id,nama,kategori,tahun,harga,stok_awal 
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
    id_game = data_game_csv[jumlah_baris()-1][0]
    id_kode = ''
    id_kode_new = ''
    id_number = ''
    Terminated = False
    i = 0
    if id_game == 'game_id':
        # di dalam data_game_csv belum terdapat game
        id = 'G001'
    else:
        while(not(Terminated)):
            # Misal G001 -> Dipisah menjadi G00 dan 1
            if id_game[i] == "G" or id_game[i] == "0":
                id_kode += id_game[i]
                i +=1
            else:
                id_number = id_game[i:]
                Terminated = True
        if id_number== "9" or id_number =="99":
            # G009 -> G010
            # G099 -> G100
            for j in range(i-1):
                id_kode_new += id_kode[j]
                id = id_kode_new + str(int(id_number)+1)
        else:
            id = id_kode + str(int(id_number)+1)
    T = [id,nama,kategori,tahun,harga,stok_awal]
    return(T)

data_game_csv = read_csv('game.csv')
data_game_csv += [tambah_game()]

# Mengecek data game csv
print(data_game_csv)
