import arrow
import pyperclip

from pyperclip import copy
# import pyperclip yapıp ta copy i çağırabiliriz sadece copy kullancağım için böyle import ettim
# Bu başka bir packge

utc = arrow.utcnow()
print(utc)

#Üsste sadece anlık tarihi veren bir uygulama daha bir çok fonksiyonlar var kullanılabirsin


#Pyperclip

str1 = "Kopyalanacak text burda"

pyperclip.copy(str1)

copied_text = pyperclip.paste()

print("Kopyalanan : " + copied_text)

# Kopyala yapıştır işini yapıyor temelde

