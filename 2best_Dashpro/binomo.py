import os
from fungsi import baris, length
from read_csv import read_csv
from login import login
from register import register
from tambah_game import tambah_game
from f06 import ubah_stok
from list_game_toko import list_game_toko
from list_game import list_game
from F11 import search_game_at_store
from f12 import topup
from riwayat import riwayat
from help import help
from load import load

folder_path = str(os.getcwd())
cek_load = False
if load(folder_path) != []:
    cek_load = True

if cek_load:
    # Load file sukses
    print("Loading...")
    print("Selamat datang di antarmuka “Binomo!”")
    data_game_csv = load(folder_path)[0]
    data_kepemilikan_csv = load(folder_path)[1]
    data_riwayat_csv = load(folder_path)[2]
    data_user_csv = load(folder_path)[3]

#data_game_csv = read_csv('game.csv')
#data_user_csv = read_csv("user.csv")
#data_riwayat_csv = read_csv('riwayat.csv')
#data_kepemilikan_csv = read_csv('kepemilikan.csv')

    print("Data_game =", data_game_csv)
    print("Data_user =",data_user_csv)
    print("Data_riwayat = " ,data_riwayat_csv)
    print("Data_kepemilikan = ",data_kepemilikan_csv)

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
    for i in range(baris(data_user_csv)):
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
                list_game(data_riwayat_csv,data_game_csv,id_user)
            elif perintah == 'search_game_at_store':
                search_game_at_store(data_game_csv)
            elif perintah == 'riwayat':
                riwayat(data_riwayat_csv,id_user)
            elif perintah == 'help':
                help(role)
            elif perintah == 'hanya_admin':
                print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
            else:
                print('perintah tidak valid')