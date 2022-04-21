from read_csv import read_csv
from fungsi import length,konso

def data_riwayat_user(data,id):
    T_riwayat_user = []
    for i in range(1,length(data)):
        for j in range(3,4):
            if id == data[i][j]:
                konso(T_riwayat_user,[data[i][0],data[i][1],data[i][2],data[i][4]])
    return(T_riwayat_user)

               
def riwayat(data,id):   
    if length(data_riwayat_user(data,id)) == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli")
    else:
        for i in range(length(data_riwayat_user(data,id))):
            for j in range(4):
                print(data_riwayat_user(data,id)[i][j],end= " | ")
            print()
    return

if __name__ == "__main__":
    id = input()
    # Program untuk mengecek fungsi
    data_riwayat_csv = read_csv('riwayat.csv')
    print(data_riwayat_user(data_riwayat_csv,id)) 
    riwayat(data_riwayat_csv,id)