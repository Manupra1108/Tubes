import os
from fungsi import length,konso

#def length(data):
#    index = 0
#
#    for i in data :
#        index += 1 
#    return index 

def stringfromarray(data):
    empty_arr = []

    for i in data:
        str = ''
        len = length(i)
        index = 1 
        for j in i:
            str += j
            if index != len:
                str+=';'
                index += 1
                
        konso(empty_arr,str)
        #empty_arr += [str]

    return empty_arr

def save(data_user, data_game, data_kepemilikan, data_riwayat):

    folder = input("Masukkan nama folder penyimpanan: ")
    
    if folder == '':
        print("Nama folder tidak valid!")
    else:        
        if not os.path.isdir(folder):
            os.mkdir(folder)

        print("Saving...")

        user = stringfromarray(data_user)
        game = stringfromarray(data_game)
        kepemilikan = stringfromarray(data_kepemilikan)
        riwayat = stringfromarray(data_riwayat)
        
        with open(f"{folder}"+"/user.csv", "w") as file:
            banyak_data = length(data_user)
            x=stringfromarray(data_user)
            for i in range(banyak_data):
                file.write(x[i]+"\n")

        with open(f"{folder}"+"/game.csv", "w") as file:
            banyak_data = length(data_game)
            x=stringfromarray(data_game)
            for i in range(banyak_data):
                file.write(x[i]+"\n")

        with open(f"{folder}"+"/kepemilikan.csv", "w") as file:
            banyak_data = length(data_kepemilikan)
            x=stringfromarray(data_kepemilikan)
            for i in range(banyak_data):
                file.write(x[i]+"\n")

        with open(f"{folder}"+"/riwayat.csv", "w") as file:
            banyak_data = length(data_riwayat)
            x=stringfromarray(data_riwayat)
            for i in range(banyak_data):
                file.write(x[i]+"\n")

        print(f"Data telah disimpan pada folder {folder}!")