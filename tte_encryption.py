import random
from typing import Optional

class TrollTextEncryption:
    def __init__(self, seed_phrase="misi_bot_troll_key"):
        self.seed_phrase = seed_phrase
        random.seed(self.seed_phrase)

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
        random.seed(None) # Önemli: Global random state'i sıfırlıyoruz.

    # encrypt_password_to_troll ve decrypt_troll_to_password metotları aynı kalacak
    def _get_random_word(self, category, char_code):
        # ... (bu metot aynı kalacak) ...
        words = self.troll_words[category]
        index = (char_code + random.randint(0, 1000)) % len(words)
        return words[index]

    def encrypt_password_to_troll(self, password: str) -> str:
        # ... (bu metot aynı kalacak) ...
        troll_phrase_parts = []
        random.seed(password + self.seed_phrase)

        for i, char in enumerate(password):
            char_code = ord(char)
            subject = self._get_random_word("subject", char_code + i)
            verb = self._get_random_word("verb", char_code * 2 + i)
            object_word = self._get_random_word("object", char_code * 3 + i)
            adjective = self._get_random_word("adjective", char_code + i * 2)
            adverb = self._get_random_word("adverb", char_code * 4 + i)
            preposition = self._get_random_word("preposition", char_code * 5 + i)
            filler = self._get_random_word("filler", char_code + i * 3)
            exclamation = self._get_random_word("exclamation", char_code * 6 + i)

            # Bu formatı daha da simsiyah hale getirmek için değiştiriyoruz
            # Daha rastgele, daha "kopuk" bir cümle yapısı
            troll_part = f"{subject} {adverb} {verb} {preposition} {adjective} {object_word} {filler}, {exclamation}!"
            troll_phrase_parts.append(troll_part)

        final_troll_phrase = " | SIKTIMIN DELİSİ! | ".join(troll_phrase_parts) # Ayırıcıyı da değiştirdik
        random.seed(None) # Rastgeleliği sıfırla
        return final_troll_phrase

    def decrypt_troll_to_password(self, troll_phrase: str) -> Optional[str]:

        return None
