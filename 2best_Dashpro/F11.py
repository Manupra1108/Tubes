from read_csv import read_csv
from fungsi import length,konso

def search_game_at_store(data):
    id = input("Masukkan ID Game: ")
    nama = input("Masukkan Nama Game: ")
    harga = input("Masukkan Harga Game: ")
    kategori = input("Masukkan Kategori Game: ")
    tahun_rilis = input("Masukkan Tahun Rilis Game: ")

    data_id = []
    data_nama = []
    data_harga = []
    data_kategori = []
    data_tahun_rilis = []
    data_final = []
    
    id_isi = False
    nama_isi = False
    harga_isi = False
    kategori_isi = False
    
    if id != '':
        # id diisi
        id_isi = True
        # data_id diisi menggunakan data_game_csv
        for i in range(1,length(data)):
            for j in range(1):
                if id == data[i][j]:
                    konso(data_id,data[i])
                    #data_id += [data[i]]
                    
    # Memasukkan data_id ke dalam data_final
    data_final = data_id
    
    if nama != '':
        # nama diisi
        nama_isi = True
        if id_isi == False:
            # id tidak diisi
            # data nama diisi menggunakan data_game_csv
            for i in range(1,length(data)):
                for j in range(1,2):
                    if nama == data[i][j]:
                        konso(data_nama,data[i])
                        #data_nama += [data[i]]
        else:
            # id diisi
            if data_id == []:
                # id diisi tapi kosong maka data nama juga kosong
                data_nama = []
            elif data_id != []:
                # id diisi dan tidak kosong sehingga data_nama diisi menggunakan data_id
                for i in range(length(data_id)):
                    for j in range(1,2):
                        if nama == data_id[i][j]:
                            konso(data_nama,data_id[i])
                            #data_nama += [data_id[i]]
        # Mengganti isi dari data_final menjadi data_nama
        data_final = data_nama
    
    if harga !='':
        # harga diisi
        harga_isi = True
        if nama_isi == True:
            # nama diisi
            if data_nama == []:
                # nama diisi tapi data nama kosong sehingga data harga juga kosong
                data_harga == []
            elif data_nama != []:
                # nama diisi dan tidak kosong sehingga data_harga diisi menggunakan data_nama
                for i in range(length(data_nama)):
                    for j in range(4,5):
                        if harga == data_nama[i][j]:
                            konso(data_harga,data_nama[i])
                            #data_harga += [data_nama[i]]
        elif nama_isi == False:
            # Nama tidak diisi
            if id_isi == False:
                # id dan nama tidak diisi sehingga data_harga diisi menggunakan data_game_csv
                for i in range(1,length(data)):
                    for j in range(4,5):
                        if harga == data[i][j]:
                            konso(data_harga,data[i])
                            #data_harga += [data[i]]
        
            elif id_isi == True:
                # id diisi
                if data_id == []:
                    # id diisi namun data_id kosong sehingga data_harga kosong
                    data_harga = []
                elif data_id != []:
                    # id diisi dan tidak kosong sehingga data_harga diisi menggunakan data id
                    for i in range(length(data_id)):
                        for j in range(4,5):
                            if harga == data_id[i][j]:
                                konso(data_harga,data_id[i])
                                #data_harga += [data_id[i]]
        # Mengganti isi dari data_final menjadi data_harga                        
        data_final = data_harga
    
    if kategori != '':
        kategori_isi = True
        # kategori diisi
        if harga_isi == True:
            # harga diisi
            if data_harga == []:
                # harga diisi namum data_harga kosong sehingga data_kategori kosong
                data_kategori == []
            elif data_harga != []:
                # harga diisi dan tidak kosong sehingga data_kategori diisi menggunakan data_harga
                for i in range(length(data_harga)):
                    for j in range(2,3):
                        if kategori == data_harga[i][j]:
                            konso(data_kategori,data_harga[i])
                            # data_kategori += [data_harga[i]]
        elif harga_isi == False:
            # harga tidak diisi
            if nama_isi == True:
                # nama diisi
                if data_nama == []:
                    # nama diisi tapi data nama kosong sehingga data kategori juga kosong
                    data_kategori == []
                elif data_nama != []:
                    # nama diisi dan tidak kosong sehingga data_kategori diisi menggunakan data nama
                    for i in range(length(data_nama)):
                        for j in range(2,3):
                            if kategori == data_nama[i][j]:
                                konso(data_kategori,data_nama[i])
                                #data_kategori += [data_nama[i]]
            elif nama_isi == False:
                # nama tidak diisi
                if id_isi == False:
                # id dan nama tidak diisi sehingga data_kategori diisi menggunakan data_game_csv
                    for i in range(1,length(data)):
                        for j in range(2,3):
                            if kategori == data[i][j]:
                                konso(data_kategori,data[i])
                                #data_kategori += [data[i]]
                    
                elif id_isi == True:
                    # id diisi
                    if data_id == []:
                        # id diisi tapi data kosong sehingga data harga kosong
                        data_kategori = []
                    elif data_id != []:
                        # id diisi dan tidak kosong sehingga data_kategori diisi menggunakan data id
                        for i in range(length(data_id)):
                            for j in range(2,3):
                                if kategori == data_id[i][j]:
                                    konso(data_kategori,data_id[i])
                                    #data_kategori += [data_id[i]]
        # Mengganti isi dari data_final menjadi data_kategori
        data_final = data_kategori
        
    if tahun_rilis != '':
        # tahun rilis diisi
        if kategori_isi == True:
            # kategori diisi
            if data_kategori == []:
                # katerogi diisi namum data kosong sehingga data_tahun_rilis kosong
                data_tahun_rilis = []
            elif data_kategori != []:
                # kategori diisi dan tidak kosong sehingga data_tahun_rilis diisi menggunakan data kategori
                for i in range(length(data_kategori)):
                    for j in range(3,4):
                        if tahun_rilis == data_kategori[i][j]:
                            konso(data_tahun_rilis,data_kategori[i])
                            #data_tahun_rilis += [data_kategori[i]]
        elif kategori_isi == False:
            # Kategori tidak diisi
            if harga_isi == True:
                # Harga diisi
                if data_harga == []:
                    # Harga diisi tapi kosong sehingga data_tahun_rilis juga kosong
                    data_tahun_rilis = []
                elif data_harga != []:
                    #Harga diisi dan tidak kosong sehingga data_tahun_rilis diisi menggunakan data harga
                    for i in range(length(data_harga)):
                        for j in range(3,4):
                            if tahun_rilis == data_harga[i][j]:
                                konso(data_tahun_rilis,data_harga[i])
                                #data_tahun_rilis += [data_harga[i]]
            elif harga_isi == False:
                # harga tidak diisi
                if nama_isi == False:
                    # nama tidak diisi
                    if id_isi == False:
                    # id dan nama tidak diisi sehingga data_tahun_rilis diisi menggunakan data_game_csv
                        for i in range(1,length(data)):
                            for j in range(3,4):
                                if tahun_rilis == data[i][j]:
                                    konso(data_tahun_rilis,data[i])
                                    #data_tahun_rilis += [data[i]]
                    elif id_isi == True:
                        # id diisi 
                        if data_id == []:
                            # id diisi tapi data_id kosong sehingga data_tahun_rilis kosong
                            data_tahun_rilis = []
                        elif data_id != []:
                            # id diisi dan tidak kosong sehingga data_tahun_rilis diisi menggunakan data id
                            for i in range(length(data_id)):
                                for j in range(3,4):
                                    if tahun_rilis == data_id[i][j]:
                                        konso(data_tahun_rilis,data_id[i])
                                        #data_tahun_rilis += [data_id[i]]
                
                elif nama_isi == True:
                    if data_nama == []:
                        # nama diisi tapi data_nama kosong sehingga data_tahun_rilis juga kosong
                        data_tahun_rilis == []
                    elif data_nama != []:
                        # nama diisi dan tidak kosong sehingga data_tahun_rilis diisi menggunakan data nama
                        for i in range(length(data_nama)):
                            for j in range(3,4):
                                if tahun_rilis == data_nama[i][j]:
                                    konso(data_tahun_rilis,data_nama[i])
                                    #data_tahun_rilis += [data_nama[i]]
        # Mengganti isi dari data_final menjadi data_tahun_rilis
        data_final = data_tahun_rilis                
        
    if data_final == []:
        # Tidak terdapat data yang memenuhi kriteria
        print("Tidak ada game pada toko yang memenuhi kriteria")
    else:
        # Terdapat data yang memenuhi kriteria
        for i in range(length(data_final)):
            for j in range(1):
                print(data_final[i][0],'|',data_final[i][1],'|',data_final[i][2],'|',data_final[i][3],'|',data_final[i][4],'|',data_final[i][5])
    return
