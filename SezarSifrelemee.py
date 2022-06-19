#Sezar şifreleme tekniği ile orijinal stringin Türkçe olduğunu varsayarak, argüman olarak bir şifre alan ve şifreyi çözmek için en uygun ofseti tahmin etmek için istatistiksel bir yöntem kullanan ya da istatistik dışı bir yöntem kullanan otomatik şifre kırma işlevi yazınız.


#GİRİLEN MESAJI ŞİFRELEYEN KISIM#
def sezarsifreleme(mesaj, key): # sifreleme işlemim için öncelikle sezarsifrelem adında bir fonk. tanımladım
    sifrelenmis_mesaj = ''   #ve sifrelenecek olan mesaj için bir değişken oluştrdum.

    alfabe = [ 'a', 'b', 'c','ç', 'd', 'e', 'f', 'g','ğ','h','ı','i', 'j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z'] #Soruda Türkçe karakter istendiği için Türkçe Alfabeyi tanımladım.
    for i in mesaj:  # burada ise tanımlamış olduğum mesaj değişkeninin her bir karakterini yakalayabilmek için for döngüsü oluşturdum.

        if i not in alfabe: # if ile mesajı giren kişi özel bir karakter girerse
            sifrelenmis_mesaj += i  #o karakteri mesajıma ekletiyorum.
        else:  # else ile de zaten alfabede bulunan bir karaktere ofset değerini ekleyerek alfabenin uzunluğuna modunu aldım.
            sifrelenmis_mesaj+= alfabe[(alfabe.index(i)+ofset) % len(alfabe)]

    print("Şifrelenmiş Mesaj:", sifrelenmis_mesaj)

print("MESAJ ŞİFRELEME")

ofset = int(input('Ofset Değerini Giriniz: ')) # bu kısımda ofset değerini kullanıcıdan alınması için input tanımladım.

mesaj = input("Şifrelenecek Mesaj: ")  # aynı şekilde şifrelenecek mesajı kullanıcıdan istedim.
sezarsifreleme(mesaj, ofset)


#ŞİFRELENEN MESAJI ÇÖZEN KISIM#

print("ŞİFRELİ MESAJ ÇÖZÜCÜ")

alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'  # burada yine bir alfabe tanımladım.

ymesaj = ''  # aynı şekilde değişken tanımladım.

mesaj= input('Şifresi Çözülecek Mesajınızı Giriniz:')
for kod in mesaj:    #basit bir for döngüsü ile mesaj değişkenin içinde
    konum = alfabe.find(kod) # find metodu yardımı ile konumunu bulup
    konum = konum-int(ofset) # bulunduğu yerden girilen ofset sayısını çıkartarak
    yharf = alfabe[konum] # yeni harfi belirledim
    ymesaj = ymesaj+yharf  # ve bu harfi girilen mesaja ekleterek şifreli mesajı çözdüm.


print('Şifresi Çözülmüş Yeni Mesajınız:',ymesaj)






