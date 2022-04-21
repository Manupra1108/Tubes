from F16 import save
import sys

def exit(data_user,data_game,data_kepemilikan,data_riwayat):
    while True:
        masukan = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
        if masukan == 'y' or masukan =='Y':
            save(data_user, data_game, data_kepemilikan, data_riwayat)
            sys.exit()
        elif masukan == 'n' or masukan == 'N':
            sys.exit()            


if __name__ == '__main__':
    exit()