from password_generator import PasswordGenerator

pwo = PasswordGenerator()
password = pwo.generate()

print(password)      # Basic olarak böyle yapılıyor karmaşık hali aşşağıda


pwo1 = PasswordGenerator()
password1 = pwo1.generate()

#Propertys

pwo1.minlen = 15  # Minumum ne kadar uzunlukta olacağını yazıyoruz
pwo1.maxlen = 20   # Maxmimum ne kadar uzunlukta olacağını yazıyoruz
pwo1.minuchars = 5  # Şifremizde minumum büyük harf olacağını yazıyoruz
pwo1.minlchars = 5   # Şifremizde minumum küçük harf olacağını yazıyoruz
pwo.minnumbers = 3  # Şifremizde en az kaç sayı olacağını yazıyoruz
pwo.minchars = 3    # Şifremizde en az kaç harf olacağını yazıyoruz

print(password1)



