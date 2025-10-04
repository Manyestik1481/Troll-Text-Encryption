import sqlite3
import os
from tte_encryption import TrollTextEncryption  # Kendi troll şifreleyicimizi çağırıyoruz

# --- AYRI VERİ TABANI AYARLARI ---
DB_NAME = "data/test_auth.db"  # Deneme için ayrı bir DB kullanıyoruz
DATA_DIR = "data"  # Veritabanının bulunacağı klasör


def ensure_data_directory():
    """Veritabanı için 'data' klasörünün varlığını kontrol eder, yoksa oluşturur."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def create_users_table(conn):
    """Veritabanında 'users' tablosunu oluşturur."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            troll_password TEXT
        )
    """)
    conn.commit()


def register_user(username, password):
    """Kullanıcı adı ve şifreyi alıp, şifreyi troll ifadeye dönüştürüp veritabanına kaydeder."""
    tte_encryptor = TrollTextEncryption()  # TTE sınıfını başlatıyoruz

    # Şifreyi troll ifadeye dönüştür
    troll_password = tte_encryptor.encrypt_password_to_troll(password)

    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, troll_password) VALUES (?, ?)",
                       (username, troll_password))
        conn.commit()
        print(f"Kullanıcı '{username}' başarıyla kaydedildi.")
        print(f"  Troll şifresi: {troll_password[:70]}...")  # Uzunluğu kısaltarak göster
        return True
    except sqlite3.IntegrityError:
        print(f"Hata: Kullanıcı adı '{username}' zaten mevcut.")
        return False
    except Exception as e:
        print(f"Kullanıcı kaydederken hata oluştu: {e}")
        return False
    finally:
        if conn:
            conn.close()


def main():
    ensure_data_directory()  # data klasörünü oluştur

    # Veritabanı bağlantısını aç ve tabloyu oluştur
    conn = sqlite3.connect(DB_NAME)
    create_users_table(conn)
    conn.close()  # İşlem bitince bağlantıyı kapat

    print("=== Troll-Text Veritabanı Kayıt Aracı ===")
    print(f"Şifreler '{DB_NAME}' dosyasına kaydedilecektir.")
    print("Çıkmak için kullanıcı adı veya şifre yerine 'q' yazın.")

    while True:
        username_input = input("\nKullanıcı Adı: ").strip()
        if username_input.lower() == 'q':
            break

        password_input = input("Şifre: ").strip()
        if password_input.lower() == 'q':
            break

        if not username_input or not password_input:
            print("Hata: Kullanıcı adı veya şifre boş olamaz. Lütfen tekrar deneyin.")
            continue

        register_user(username_input, password_input)
        print("-" * 40)

    print(f"\nProgramdan çıkılıyor. '{DB_NAME}' dosyası hazır.")
    print("Bu dosyayı dilediğin platformda 'kırılması imkansız şifreler' diye paylaşabilirsin. ;)")


if __name__ == "__main__":
    main()