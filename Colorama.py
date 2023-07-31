
from colorama import Fore , Back , Style

print(Fore.RED + "Red Text")
print(Back.RED + Fore.BLACK +"Red Background ")
print(Style.DIM+"and in dim text")
print(Style.RESET_ALL)
print('back to normal now')

# ANSI kodlarıyla renklendirme

print('\033[31m' + 'some red text')
print('\033[39m')

# Daha çok fazla fonksiyonları var kullanılabilirim


# **** Bununla benzer terminal stillendirme packge "Blessing" var *****