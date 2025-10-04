import hmac
import hashlib
from typing import List, Optional

# Dinamik Kaos TTE - Güç, Sistemin Kendi İç Kaosundan Gelir.
class DynamicKaosTrollTextEncryption:

    def __init__(self):
        # Seed phrase artık bir başlangıç noktası olarak, ama asıl anahtar değil.
        # Bu, ilk HMAC'yi beslemek için kullanılır (düşük entropili ama sabit).
        self.initial_seed_phrase = "troll_key_baslangic" 

        self.troll_words = {

            "subject": [

                "bıyıklı ali", "ayşe teyze", "üçüncü velayet", "gizli uzaylı", "sinsice bekleyen kedi",

                "hakan", "bir porsuk", "esrarengiz dayı", "rüştü amca", "yenge", "kıvırcık marul",

                "o ibne", "şu pezevenk", "lanet olası herif", "baban", "anneannen"

            ],

            "verb": [

                "domalttı", "sikti", "ebesini tersten gördü", "gözüne soktu", "kafasını ütüledi",

                "içine attı", "ters düz etti", "ortaya karıştırdı", "fırlattı", "gömmeye çalıştı",

                "ışınladı", "uzaya postaladı", "ağzına sıçtı", "götünden nefes aldı", "beynini emdi",

                "bacısını düdükledi", "ananı avradını sikti", "yarrağı yedi", "kıçını yaladı"

            ],

            "object": [

                "komşunun kedisini", "bakkalın çırağını", "uzay mekiğini", "geçen haftaki faturayı",

                "çayırlı ineği", "evin anahtarını", "alt komşunun karısını", "müdürün kravatını",

                "patates püresini", "uzun eşeği", "koca karıyı", "yavşak tilkiyi",

                "kendi götünü", "şerefsiz köpeği", "malum organını", "annemin kocasını", "pislik herifi"

            ],

            "adjective": [

                "morarmış", "işlevsiz", "acayip", "zibidi", "yemyeşil", "kıçıkırık", "patlak",

                "bomboş", "sinsi", "kısa devre", "yüksek voltajlı", "sarkık", "igrenç",

                "sapık", "top", "mal", "gerizekalı", "boktan", "salak salak", "orospu çocuğu", "dümbelek"

            ],

            "adverb": [

                "bodoslama", "pat diye", "aniden ve sertçe", "şaşkınlıkla", "hızla ve anlamsızca",

                "davul çalarak", "horlayarak", "nefes nefese", "zıplayarak", "döverek",

                "hayvan gibi", "sanki hiç olmamış gibi", "göz göre göre", "tüyler ürpertici şekilde",

                "siklemeden", "umursamadan", "balıklama"

            ],

            "preposition": [

                "boyunca", "üzerine", "karşısında", "yanı başında", "içinden", "arasına", "altına",

                "peşinden", "arkasına", "önünden", "amına", "götüne", "kafasının üstüne", "sırtına",

                "tam ortasına"

            ],

            "filler": [

                "aga be", "yaani", "bak şimdi", "hadi eyvallah", "falan filan", "lan", "aq", "yok ya",

                "aynen", "kanka", "kısaca", "hassiktir", "amma da", "yeminle", "tövbe yarabbi"

            ],

            "exclamation": [

                "Ohaaa", "hassiktir", "vay amk", "püü", "yok artık", "ehehehe", "gülme komşuna gelir başına",

                "ben şok", "bön bön baktı", "wtf", "aha da böyle", "yuh", "ananı satayım", "o neydi gız",

                "tüh be", "lanet olsun", "allah belanı vermesin"

            ]

        }

        random.seed(None)

    def _derive_hmac_output(self, seed: bytes, message: bytes) -> bytes:
        """Verilen seed ve mesajdan kriptografik olarak güvenli HMAC çıktısı üretir."""
        # Kendi kendini üreten kaos için HMAC kullanıyoruz.
        return hmac.new(seed, message, hashlib.sha256).digest()

    def _get_deterministic_index(self, hmac_output: bytes, words_list: List[str]) -> int:
        """HMAC çıktısını kullanarak deterministik indeks seçer."""
        list_len = len(words_list)
        
        if len(hmac_output) < 4:
            # HMAC çıktısı kısa gelirse (teorik değil), kendini tekrar hash et
            hmac_output = self._derive_hmac_output(hmac_output, hmac_output)

        large_int = int.from_bytes(hmac_output[:4], 'big')
        return large_int % list_len

    def encrypt_password_to_troll(self, password: str, username: str) -> str:
        troll_phrase_parts = []
        
        # 1. Başlangıç Seed'i (Düşük Entropili Ama Deterministic)
        # Bu, eski key'in yerine geçer.
        current_hmac_seed = self.initial_seed_phrase.encode('utf-8')
        
        # Tüm şifrelemeyi tek bir HMAC ile başlatıyoruz.
        hmac_message_base = f"{username}|{password}".encode('utf-8')

        for i, char in enumerate(password):
            # 2. Dinamik Kaos Girişi (4. Karakterden İtibaren)
            if i >= 3:
                # Önceki 3 trol ifadesini al ve yeni bir seed üret (Kaos patlaması!)
                last_three_trolls = " | ".join(troll_phrase_parts[i-3:i])
                
                # Dinamik Seed: Önceki Kaos Çıktısı + Kullanıcı Verisi
                new_seed_message = f"{last_three_trolls}|{username}".encode('utf-8')
                current_hmac_seed = self._derive_hmac_output(current_hmac_seed, new_seed_message)
            
            # Her adım için benzersiz mesaj oluştur (pozisyon tabanlı)
            hmac_message = self._derive_hmac_output(current_hmac_seed, hmac_message_base + str(i).encode('utf-8'))

            categories = [
                ("subject", self.troll_words["subject"]), ("verb", self.troll_words["verb"]), 
                # ... diğer kategoriler ...
            ]
            
            selected_words = {}
            for j, (category_name, word_list) in enumerate(categories):
                # Her kategori için HMAC çıktısının farklı bir 4 byte'lık bölümünü kullan
                # Bu, zincirleme kaosun PRNG state recovery'yi engelleme yoludur.
                hmac_chunk = hmac_message[j*4:(j+1)*4]
                if len(hmac_chunk) < 4: 
                    # HMAC çıktısı biterse, yeni bir HMAC üret
                    hmac_message = self._derive_hmac_output(hmac_message, current_hmac_seed)
                    hmac_chunk = hmac_message[0:4] # Başa dön

                index = self._get_deterministic_index(hmac_chunk, word_list)
                selected_words[category_name] = word_list[index]
            
            # Troll Cümle Yapısı (Estetik)
            troll_part = (
                f"{selected_words['subject']} {selected_words['adverb']} {selected_words['verb']} "
                f"{selected_words['preposition']} {selected_words['adjective']} {selected_words['object']} "
                f"{selected_words['filler']}, {selected_words['exclamation']}!"
            )
            troll_phrase_parts.append(troll_part)
            
        final_troll_phrase = " | SIKTIMIN DELİSİ! | ".join(troll_phrase_parts)
        
        return final_troll_phrase

    def decrypt_troll_to_password(self, troll_phrase: str) -> Optional[str]:
        # Kırılamazlık devam ediyor.
        return None

