from read_csv import read_csv
from fungsi import length,konso

def isUserValid(username):
    isvalid = True
    for i in username:
        if not((i>='a' and i<='z') or (i>='A' and i<='Z') or (i>='0' and i<='9') or (i=='_' or i=='-')):
            isvalid=False
        
    return isvalid

#def length(list):
#    index = 0

#    for i in list :
#        index += 1 
#    return index 

def isUnique(username,data):
    len = length(data)

    issame = True
    for i in range(1,len):
        if data[i][1] == username:
            issame = False

    return issame

def register(data):
    
    cek_regis=True
    while(cek_regis):
        nama = input("Masukan nama: ")
        username = input("Masukan username: ")
        password = input("Masukan password: ")
        
        if isUserValid(username) == False:
            print("Username Anda tidak valid. Silakan buat Username lagi.")
        else:
            if isUnique(username,data) == False:
                print(f"Username {username} sudah terpakai, silakan menggunakan username lain.")
            else:
                print(f'Username {username} telah berhasil register ke dalam "Binomo".')
                konso(data,[str(length(data)-1),username,nama,password,"user",'0'])
                #data+=[[str(length(data)-1),username,nama,password,"user",'0']]
                cek_regis=False
    return data

if __name__ == '__main__':
    data_user_csv = read_csv('user.csv')
    register(data_user_csv)
    