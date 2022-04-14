from read_csv import read_csv

def baris_riwayat():
    # Mencari jumlah baris pada data_riwayat_csv
    baris = 0
    for i in data_riwayat_csv:
        baris +=1
    return(baris)

def array_game_id():
    # Membuat array berisikan kumpulan game_id yang dimiliki user 
    T_game_id = []
    for i in range(1,baris_riwayat()):
        for j in range(1):
            T_game_id += [data_riwayat_csv[i][j]]
    return(T_game_id)

def jumlah_game_id():
    # Mencari jumlah game yang dimiliki user
    count_game = 0
    for arr in array_game_id():
        count_game +=1
    return(count_game)

def sort_game_id():
    # Melakukan sorting pada id_game
    T_game_int = [0 for i in range(jumlah_game_id())]
    j = 0
    for i in range (jumlah_game_id()):
        T_game_id = array_game_id()
        arr = array_game_id()[i]
        terminated_id = False
        while not(terminated_id):
            if arr[j] == "0" or arr[j]=="G":
                j +=1
            else:
                T_game_int[i] = int(arr[j:])
                j = 0
                terminated_id = True
    
    i = 0
    kondisi = False
    while not(kondisi):
        Pass = i
        temp = 0
        imin = Pass
        while(Pass<=jumlah_game_id()-1):
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
        if i == jumlah_game_id():
            kondisi = True
    return(T_game_id)

def baris_game():
    # Mencari jumlah baris pada data_game_csv
    baris = 0
    for i in data_game_csv:
        baris += 1
    return(baris)

def list_game():
    count = 0
    for i in range(baris_game()):
        if jumlah_game_id() == count:
            break
        for j in range(1):
            if data_game_csv[i][j] == sort_game_id()[count]:
                print(data_game_csv[i][0], '|' , data_game_csv[i][1], '|',data_game_csv[i][2], '|' , data_game_csv[i][3], '|', data_game_csv[i][4])
                count +=1
    return
                
        
data_game_csv = read_csv('game.csv')
data_riwayat_csv = read_csv('riwayat.csv')
list_game()