# Author : Orion F.
# This program allows you to convert currency. Enjoy.


from currency_converter import CurrencyConverter


c = CurrencyConverter()
print(c.convert(100, 'EUR', 'USD'))  # EUR to USD


c = CurrencyConverter()
# You can change the date of the rate
print(c.convert(100, 'USD', 'EUR',))  # USD to EUR
