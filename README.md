# Troll-Text-Encryption
Yeni, Eğlencesine yapılmış güçlü bir şifreleme algoritması

başlamadan önce typing ve random kütüphanelerine sahip olduğundan emin ol

#----------------------------------------------------------------

# Troll-Text Encryption (TTE) - Siber Güvenlikte Yeni Bir Çağ!

Siber güvenlik mi? Matematik mi? Algoritmik ciddiyet mi? Yeter artık!
TTE, geleneksel şifreleme mantığını çöpe atıyor ve siber dünyayı kahkahalara boğarken, hacker'ları delirten devrimsel bir yaklaşım sunuyor.

## Nedir Bu TTE?

Troll-Text Encryption (TTE), parolalarınızı veya hassas metinlerinizi matematiksel olarak güvenli, ancak psikolojik olarak yıkıcı ve absürt bir "troll cümleye" dönüştüren tek yönlü bir algoritmalar bütünüdür. Amacımız, veri tabanınıza sızan bir saldırganın karşısına "HASH" veya "AES şifreli metin" değil, "Bıyıklı Ali, ananı avradını sikti bodoslama, amına gerizekalı pislik herifi tüh be!" gibi bir ifade çıkarmaktır.

Hacker, veriyi ele geçirdiğinde şunlarla karşılaşacak:
1.  **ŞOK ve HAYAL KIRIKLIĞI:** Beklediği ciddiyet yerine, hakaretlerle dolu bir kaosa saplanacak.
2.  **KIRILAMAZ BİR ENGELLER:** Algoritma tek yönlü tasarlanmıştır. `decrypt_troll_to_password` metodumuz kasten `return None` döner. Yani: **Bu şifreleri geri çözmek İMKANSIZDIR.**
3.  **PSİKOLOJİK YIKIM:** Düşünün, aylarca uğraşıp ele geçirdiğiniz veri tabanında sadece küfürler ve absürt cümleler buluyorsunuz. Bu, siber güvenlikte yeni bir "psikolojik savaş" seviyesidir.

## Nasıl Çalışır?

TTE, her bir giriş karakterini, geniş ve küfürlü kelime listelerimizden (Subject, Verb, Object, Adjective, Adverb, Preposition, Filler, Exclamation) rastgele seçilen kelimelerle eşleştirir. Bu seçim, orijinal karaktere, döngü sırasına ve sahte rastgele sayılara bağlıdır. Sonuç? Orijinal parolayı geri döndürmeyi **matematiksel olarak anlamsız ve pratik olarak imkansız** hale getiren, benzersiz ve aşağılayıcı bir troll cümlesi!

### Örnek Bir Çıktı:

**Orijinal Parola:** `SuperGucluSifre123!`

**Troll Şifre (Örnek):**
`kıvırcık marul nefes nefese ağzına sıçtı altına sarkık annemin kocasını hassiktir, vay amk! | SIKTIMIN DELİSİ! | o ibne balıklama kafasını ütüledi önüne boktan annemin kocasını lan, o neydi gız! | SIKTIMIN DELİSİ! | ...`
(Ve bu cümle, şifrenizin her karakteri için böyle uzayıp gider.)

## Neden TTE'yi Kullanmalısınız?

* **Hacker'ları Delirtin:** Geleneksel şifreleme hacker'lara meydan okur. TTE, hacker'ları aşağılar ve sinir krizine sokar.
* **Geri Dönüşü Olmayan Güvenlik:** Parolaları geri çözmek için hiçbir mekanizma yoktur. Matematiksel düzen mi? Ciddiyet mi? TTE'de bunlara yer yok. Sadece saf kaos var!
* **Siber Psikolojik Savaş:** Düşmanlarınızın zamanını, kaynaklarını ve akıl sağlıklarını tüketin.
* **Açık Kaynak:** İnceleyin, gülün, geliştirin ve bu trollemeye siz de katılın!

## Kurulum ve Kullanım

1.  zip dosyasını indirin
2.  `tte_encryption.py` dosyasını projenize dahil edin.
3.  Örnek kullanım için `test_troll_db.py` scriptine göz atın.

```python
from tte_encryption import TrollTextEncryption

tte = TrollTextEncryption()
password = "mySecretPassword123"
troll_password = tte.encrypt_password_to_troll(password)
print(f"Orijinal: {password}")
print(f"Troll: {troll_password}")

# Hacker'lar için kötü haber:
decrypted_password = tte.decrypt_troll_to_password(troll_password)
print(f"Çözülen: {decrypted_password}") # Çıktı: None
