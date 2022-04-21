from fungsi import length
from F02 import register
from F03 import login
from F04 import tambah_game
from F05 import ubah_game
from F06 import ubah_stok
from F07 import list_game_toko
from F08 import buy_game
from F09 import list_game
from F10 import search_my_game
from F11 import search_game_at_store
from F12 import topup
from F13 import riwayat
from F14 import help
from F15 import load
from F16 import save
from F17 import exit

#folder_path = str(os.getcwd())
cek_load = False
if load('semua') != []:
    cek_load = True

if cek_load:
    # Load file sukses
    print("Loading...")
    data_game_csv = load('game.csv')
    data_kepemilikan_csv = load('kepemilikan.csv')
    data_riwayat_csv = load('riwayat.csv')
    data_user_csv = load('user.csv')
    print("Selamat datang di antarmuka “Binomo!”")
    print()
    #print("Data_game =", data_game_csv)
    #print("Data_user =",data_user_csv)
    #print("Data_riwayat = " ,data_riwayat_csv)
    #print("Data_kepemilikan = ",data_kepemilikan_csv)

    cek_login = False
    while cek_login == False:
        perintah = input(">>> ")
        if perintah == 'login':
            id_user = login(data_user_csv)
            for i in str(id_user):
                if '0'<= i <= '9':
                    cek_login = True
                else:
                    cek_login = False
        elif perintah == 'help':
            help('belum login')
            print()
        else:
            print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain login")
            print()

    # Get Role
    for i in range(length(data_user_csv)):
        for j in range(1):
            if id_user == data_user_csv[i][j]:
                role = data_user_csv[i][4]
                break

    while True:
        if role == "admin":
            print()
            perintah = input(">>> ")
            if perintah == 'register':
                register(data_user_csv)
            elif perintah == 'ubah_game':
                ubah_game(data_game_csv)
            elif perintah == 'tambah_game':
                tambah_game(data_game_csv)
            elif perintah == 'ubah_stok':
                ubah_stok(data_game_csv)
            elif perintah == 'list_game_toko':
                list_game_toko(data_game_csv)
            elif perintah == 'search_game_at_store':
                search_game_at_store(data_game_csv)
            elif perintah == 'topup':
                topup(data_user_csv)
            elif perintah == 'help':
                help(role)
            elif perintah == "save":
                save(data_user_csv, data_game_csv, data_kepemilikan_csv, data_riwayat_csv)
            elif perintah == 'exit':
                exit(data_user_csv, data_game_csv, data_kepemilikan_csv, data_riwayat_csv)
            elif perintah == 'hanya_user':
                print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
            else:
                print("Perintah tidak valid")

        elif role == 'user':
            print()
            perintah = input(">>> ")
            if perintah == 'list_game_toko':
                list_game_toko(data_game_csv)
            elif perintah == 'list_game':
                list_game(data_kepemilikan_csv,data_game_csv,id_user)
            elif perintah == 'buy_game':
                buy_game(data_riwayat_csv,data_game_csv,data_kepemilikan_csv,data_user_csv,id_user)
            elif perintah == 'search_my_game':
                search_my_game(data_kepemilikan_csv,data_game_csv,id_user)
            elif perintah == 'search_game_at_store':
                search_game_at_store(data_game_csv)
            elif perintah == 'riwayat':
                riwayat(data_riwayat_csv,id_user)
            elif perintah == 'help':
                help(role)
            elif perintah == "save":
                save(data_user_csv, data_game_csv, data_kepemilikan_csv, data_riwayat_csv)
            elif perintah == 'exit':
                exit(data_user_csv, data_game_csv, data_kepemilikan_csv, data_riwayat_csv)
            elif perintah == 'hanya_admin':
                print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            else:
                print('perintah tidak valid')
