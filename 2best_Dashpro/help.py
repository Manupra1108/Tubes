def help(role):
    print("============ HELP ============")
    if role == "Admin":
        print("register - untuk melakukan registrasi user baru")
        print("login - untuk melakukan login ke dalam sistem")
        print("tambah_game - untuk menambah game yang dijual pada toko")
        print("ubah_game - untuk mengubah game yang dijual pada toko")
        print("ubah_stok - untuk melakukan penambahan atau pengurangan stok pada game tertentu yanf dijual pada toko")
        print("list_game_toko - untuk melihat list game yang dijual pada toko")
        print("search_game_at_store - untuk mencari game di Toko dari ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
        print("topup - untuk menambahkan saldo kepada user")
        print("save - untuk melakukan penyimpanan data ke dalam suatu file setelah melakukan perubahan")
        print("exit - untuk keluar dari aplikasi")
    elif role == "User":
        print("login - untuk melakukan login ke dalam sistem")
        print("list_game_toko - untuk melihat list game yang dijual pada toko")
        print("buy_game - Untuk membeli game")
        print("list_game - Untuk melihat game yang dimiliki")
        print("search_my_game - untuk melakukan pencarian terhadap game yang dimiliki berdasarkan id dan tahun rilis")
        print("search_game_at_store - untuk mencari game di Toko dari ID, Nama Game, Harga, Kategori, dan Tahun Rilis")
        print("riwayat - untuk melihat riwayat pembelian game user")
        print("save - untuk melakukan penyimpanan data ke dalam suatu file setelah melakukan perubahan")
        print("exit - untuk keluar dari aplikasi")
    return


# Fungsi :
# 2_Register : Admin
# 3_Login : User dan Admin
# 4_tambah_game : Admin
# 5_ubah_game : Admin
# 6_ubah_stok : Admin
# 7_list_game_toko : User dan Admin
# 8_buy_game : User
# 9_list_game : User
# 10_search_my_game : User
# 11_search_game_at_store : User dan Admin
# 12_topup : Admin
# 13_riwayat : User
# 14_help
# 15_load
# 16_save : User dan Admin
# 17_exit : User dan Admin