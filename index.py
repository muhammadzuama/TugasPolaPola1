import psycopg2

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Cek apakah instansi sudah ada sebelumnya
        if not cls._instance:
            # Jika tidak ada, buat instansi baru
            cls._instance = super().__new__(cls, *args, **kwargs)
            # Mengatur parameter koneksi basis data sesuai dengan informasi yang diperlukan
            cls._instance.connection_parameters = {
                "host": "localhost",
                "database": "rumah_sakit",
                "user": "postgres",
                "password": "1905"
            }
        return cls._instance

    def connect(self):
        try:
            # Membuat koneksi ke basis data
            self.connection = psycopg2.connect(**self.connection_parameters)
            print("Connected to database successfully!")
        except psycopg2.Error as e:
            print("Unable to connect to the database:", e)

    def close(self):
        if hasattr(self, 'connection') and self.connection is not None:
            # Menutup koneksi ke basis data
            self.connection.close()
            print("Connection to database closed.")

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek DatabaseConnection
    db = DatabaseConnection()

    # Melakukan koneksi ke basis data
    db.connect()

    # Melakukan query atau operasi lain pada basis data
    # Misalnya:
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM RumahSakit")
    
    # Mengambil semua baris hasil dari query
    rows = cursor.fetchall()
    
    # Menampilkan hasilnya
    for row in rows:
        print(row)

    #Menutup koneksi saat selesai menggunakan basis data
    db.close()
