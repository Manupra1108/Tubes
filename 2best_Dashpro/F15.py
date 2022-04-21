import argparse
import os
from fungsi import read_csv

def load(x):
    filename = x
    dir = argument()
    
    if not os.path.isdir(dir):
        print(f"Folder “{dir}” tidak ditemukan")
        return([])
    else:
        data_game_csv = read_csv('game.csv',dir)
        data_user_csv = read_csv('user.csv',dir)
        data_riwayat_csv = read_csv('riwayat.csv',dir)
        data_kepemilikan_csv = read_csv('kepemilikan.csv',dir)
        if filename == 'game.csv':
            return(data_game_csv)
        elif filename == 'user.csv':
            return (data_user_csv)
        elif filename == 'riwayat.csv':
            return(data_riwayat_csv)    
        elif filename == 'kepemilikan.csv':
            return(data_kepemilikan_csv)
        else:
            return(data_game_csv,data_user_csv,data_riwayat_csv,data_kepemilikan_csv)
            
def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help ='')
    args = parser.parse_args()
    return(args.nama_folder)

