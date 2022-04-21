from read_csv import read_csv
from fungsi import length


def isIdValid(id_game,data_game):
    isValid = False
    for i in range(1, length(data_game)):
        if data_game[i][0] == id_game:
            isValid = True
            break
    return isValid

def updateData(id_game, nama_game, kategori, tahun_rilis, harga, data_game):
    # Inisialisasi Awal
    id_game_isi = False
    tahun_isi = False
    harga_isi = False
    
    # Validasi masukkan id_game dan pencarian indeks dari masukkan id_game
    for i in range(1,length(data_game)):
        for j in range(1):
            if data_game[i][j] == id_game:
                id_game_isi = True
                indeks = i
                break
    if id_game_isi == True:
        # id_game diisi dan valid
        if nama_game != '':
            # nama diisi sehingga nama game pada id_game yang dimasukkan berubah
            data_game[indeks][1] = nama_game
        if kategori != '':
            # kategori diisi sehingga kategori pada id_game yang dimasukkan berubah
            data_game[indeks][2] = kategori
        if tahun_rilis != '':
            # tahun rilis diisi
            tahun_isi = True
            for i in tahun_rilis:
                if not(i>='0' and i<= '9') or i =='':
                    # masukkan tahun tidak valid sehingga tahun rilis pada id_game yang dimasukkan tidak berubah
                    tahun_isi = False
            if tahun_isi:
                # masukkan tahun valid sehingga tahun rilis pada id_game yang dimasukkan berubah
                data_game[indeks][3] = tahun_rilis
        if harga != '':
            # Harga diisi
            harga_isi = True
            for i in harga:
                if not(i>='0' and i<= '9') or i =='':
                    # Masukkan Harga tidak valid sehingga harga pada id_game yang dimasukkan tidak berubah 
                    harga_isi = False
            if harga_isi:
                # Masukkan harga valid sehingga harga pada id_game yang dimasukkan berubah
                data_game[indeks][4] = harga
    return (data_game)

def ubah_game(data_game):
    cond = False
    while not(cond):
        id_game = input("Masukkan ID game: ")
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        if isIdValid(id_game,data_game) == True:
            updateData(id_game, nama_game, kategori, tahun_rilis, harga, data_game)
            print(f"Game dengan ID {id_game} berhasil diupdate")
            cond = True
        else:
            print("ID game invalid!")
    return (data_game)

#if __name__ == "__main__":
#    data_game_csv = read_csv('game.csv')
#    while True:
#        print(ubah_game(data_game_csv))
#print(data_game)