# PR Konversi satuan temperatur

# program konversi Kelvin ke Farenheit
print("\n PROGRAM KONVERSI TEMPERATUR \n")

kelvin = float(input('Masukkan suhu dalam Kelvin: '))
print("suhu adalah",kelvin, "K")

#Farenheit
farenheit = (9/4 * (4/5 * (kelvin - 273))) + 32 # F - C - K
print("suhu dalam fahrenheit adalah ",farenheit, "F")

# program konversi Farenheit ke Kelvin
print("\n PROGRAM KONVERSI TEMPERATUR \n")

farenheit = float(input('Masukkan suhu dalam Farenheit: '))
print("suhu adalah",farenheit, "F")

#Kelvin
kelvin = (5/9 * (farenheit - 32)) + 273 # K - R - F
print("suhu dalam kelvin adalah",kelvin, "K")
