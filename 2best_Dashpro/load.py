import argparse
import os
from read_csv import read_csv

def load(dir):
    filenames = os.listdir(dir)
    file_found = False
    if argument() == '':
        print("Tidak ada nama folder yang diberikan!")
    else:
        for fileName in filenames:
            if argument() == fileName:
                file_found = True
                files = os.listdir(fileName)
                for file in files:
                    if file == 'game.csv':
                        data_game_csv = read_csv(file)
                    elif file == 'user.csv':
                        data_user_csv = read_csv(file)
                    elif file == 'riwayat.csv':
                        data_riwayat_csv = read_csv(file)
                    elif file == 'kepemilikan.csv':
                        data_kepemilikan_csv = read_csv(file)
                #print('FileName: ' + fileName)
                #print('folder path:' + os.path.abspath(os.path.join(dir,fileName)),sep='\n')
                break
    if file_found == False:
        print(f"Folder “{argument()}” tidak ditemukan")
        return ([])
    else:
        return (data_game_csv,data_kepemilikan_csv,data_riwayat_csv,data_user_csv)

def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help ='')
    args = parser.parse_args()
    return(args.nama_folder)


#folder_path = str(os.getcwd())
#path = r"D:\File Kadek\2best_Dashpro\Folder123"
#if __name__ == '__main__':
    #files = next(os.walk(path))[2]
    #print("Files = %s" % files)
    #print(argument())
    #print(load(folder_path))