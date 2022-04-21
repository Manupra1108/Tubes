from fungsi import length,konso
import datetime

def found_game(data2,id_game):
    # Melakukan pencarian id_game yang ingin dibeli pada data_game
    found = False
    for i in range(length(data2)):
        for j in range(1):
            if data2[i][j] == id_game:
                found = True
                break
    return(found)

def get_indeks_idgame(data2,id_game):
    # Melakukan pencarian indeks dari id_game yang ingin dibeli pada data_game
    for i in range(1,length(data2)):
        for j in range(1):
            if data2[i][j] == id_game:
                indeks = i
                break
    return(indeks)

def get_indeks_userid(data4,id):
    # Melakukan pencarian indeks dari user_id pada data_user
    for i in range(1,length(data4)):
        for j in range(1):
            if data4[i][j] == id:
                indeks = i
                break
    return(indeks)

def cek_saldo (data2,data4,id,id_game):
    # Melakukan pengecekan apakah saldo cukup atau tidak
    saldo_cukup = True
    for i in range(1,length(data4)):
        for j in range(1):
            if data4[i][j] == id:
                if int(data4[i][5]) < int(data2[get_indeks_idgame(data2,id_game)][4]):
                    # Saldo tidak cukup
                    saldo_cukup = False
                    break
                else:
                    # Saldo cukup
                    break
    return(saldo_cukup)

def cek_stok(data,id_game):
    # Melakukan pengecekan apakah stok masih tersedia atau tidak
    stok_ada = True
    for i in range(1,length(data)):
        for j in range(1):
            if data[i][j] == id_game:
                if data[i][5] == "0":
                    stok_ada = False
                    break
                else:
                    break
    return(stok_ada)
                
# data1 = riwayat, data2 = game , data3 = kepemilikan, data4 = user, id = user_id
def buy_game(data1, data2, data3, data4, id):
    id_game = input('Masukkan ID Game: ')
    game_found = False
    for i in range(1,length(data3)): # KEPEMILIKAN
        for j in range(1):
            if data3[i][j] == id_game:
                if data3[i][1] == id:
                    game_found = True
                    break
    if game_found == True:
        # Sudah punya game yang ingin dibeli
        print("Anda sudah memiliki Game tersebut!")
    else: #Belum punya game tersebut
        if not(found_game(data2,id_game)):
            print("Game yang ingin Anda beli tidak ditemukan pada toko")
        else:
            if not(cek_stok(data2,id_game)):
                print("Stok Game tersebut sedang habis!")
            else:
                if not(cek_saldo(data2,data4,id,id_game)):
                    print("Saldo anda tidak cukup untuk membeli Game tersebut!")
                else:
                    sisa_saldo = int(data4[get_indeks_userid(data4,id)][5]) - int(data2[get_indeks_idgame(data2,id_game)][4])
                    print(f"Game “{data2[get_indeks_idgame(data2,id_game)][1]}” berhasil dibeli!")
                    # Mengurangi stok game dari game yang dibeli :
                    data2[get_indeks_idgame(data2,id_game)][5] = str(int(data2[get_indeks_idgame(data2,id_game)][5])-1)
                    # Mengubah saldo user setelah membeli game :
                    data4[get_indeks_userid(data4,id)][5] = str(sisa_saldo)
                    # Menambah data riwayat :
                    tahun_beli = datetime.datetime.now() 
                    konso(data1,[id_game,data2[get_indeks_idgame(data2,id_game)][1],data2[get_indeks_idgame(data2,id_game)][4],id,str(tahun_beli.year)])
                    # Menambah data kepemilikan :
                    konso(data3,[id_game,id])
    return
            