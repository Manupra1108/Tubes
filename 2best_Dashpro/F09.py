from read_csv import read_csv
from fungsi import length,konso

def array_game_id(data1,id):
    # Membuat array berisikan kumpulan game_id yang dimiliki user 
    T_game_id = []
    
    for i in range(1,length(data1)):
        for j in range(1,2):
            if id == data1[i][j]:
                konso(T_game_id,data1[i][0])
                #T_game_id += [data1[i][0]]
    return(T_game_id)

def sort_game_id(data1,id):
    # Melakukan sorting pada id_game
    len_game_id = length(array_game_id(data1,id))
    game_int = ''
    T_game_int = [0 for i in range(len_game_id)]
    j = 0
    for i in range (len_game_id):
        T_game_id = array_game_id(data1,id)
        arr = array_game_id(data1,id)[i]
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
    i = 0
    kondisi = False
    while not(kondisi):
        Pass = i
        imin = Pass
        while(Pass<=len_game_id-1):
            if T_game_int[Pass] < T_game_int[imin]:
                imin = Pass
                Pass +=1
            else:
                Pass +=1
        temp_int = T_game_int[i]
        temp_id = T_game_id[i]
        T_game_int[i] = T_game_int[imin]
        T_game_id[i] = T_game_id[imin]
        T_game_int[imin] = temp_int
        T_game_id[imin] = temp_id
        i +=1
        if i == len_game_id:
            kondisi = True
    return(T_game_id)


def list_game(data1,data2,id):
    len_game_id = length(array_game_id(data1,id))
    if len_game_id == 0:
        print("Maaf, kamu belum memiliki game. Ketik perintah beli_game untuk beli")
    else:
        count = 0
        i = 0
        j = 0
        while (count<len_game_id):
            if data2[i][j] == sort_game_id(data1,id)[count]:
                print(data2[i][0], '|' , data2[i][1], '|',data2[i][2], '|' , data2[i][3], '|', data2[i][4])
                count +=1
                i = 0
            else:
                i +=1
    return


if __name__ == '__main__': 
    id = input()
    data_kepemilikan_csv = read_csv('kepemilikan.csv')
    data_riwayat_csv = read_csv('riwayat.csv')
    data_game_csv = read_csv('game.csv')
    print(array_game_id(data_kepemilikan_csv,id))
    print(sort_game_id(data_kepemilikan_csv,id))
    list_game(data_kepemilikan_csv,data_game_csv,id)