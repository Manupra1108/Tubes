from fungsi import length

data_user = [["id","username","nama","password","role","saldo"], 
            ['0',"rafi","rafi","rafi","admin",'10000'], 
            ['1',"bat_man","batman","kelelawar","user",'30000'], 
            ['2',"baim","ibrahim","baimsipsip","user",'50000'],
            ['3',"ard_studios","ardhan","dandan123","user",'40000'],
            ['4',"super_man","superman","kuat","user",'20000']]

#def length(list):
#    index = 0
#    for i in list :
#        index += 1 
#    return index 

def search(input_data,data,column):
    x = 0
    for i in range(length(data)):
        if input_data != data[i][column]:
            x += 1
        elif input_data == data[i][column]:
            break
    return x

def topup(data):
    username = input("Masukan username: ")
    tambah_saldo = input("Masukan saldo: ")
    if 0 < search(username,data,1) < length(data):
        isSaldoValid = True
        if tambah_saldo == '':
            isSaldoValid = False
        else:
            for i in tambah_saldo:
                if not(i>="0"and i<="9" or i=='-') or i =='':
                    isSaldoValid = False
                    break
        if not(isSaldoValid):
            print("Masukan tidak valid")
        else:
            if int(tambah_saldo) < 0:
                if -int(tambah_saldo) > int(data[search(username,data,1)][5]):
                    print("Masukan tidak valid.")
                else:
                    saldo = int(data[search(username,data,1)][5]) + int(tambah_saldo)
                    print(f"Top up berhasil. Saldo {username} berkurang menjadi {saldo}.")
                    data[search(username,data,1)][5] = str(saldo)
            else:
                saldo = int(data[search(username,data,1)][5]) + int(tambah_saldo)
                print(f"Top up berhasil. Saldo {username} bertambah menjadi {saldo}.")
                data[search(username,data,1)][5] = str(saldo)
    else:
        print(f"Username {username} tidak ditemukan.")
    
    return data