invoer = int(input())
aantalTjirpsPerMinuut = invoer

def berekenTempFahrenheit(aantalTjirpsPerMinuut):
    return 50+((aantalTjirpsPerMinuut-40)/4)

def berekenTempCelsius(aantalTjirpsPerMinuut):
    return 10+((aantalTjirpsPerMinuut-40)/7)

aantalGradFahr = berekenTempFahrenheit(aantalTjirpsPerMinuut)
aantalGradCelc = berekenTempCelsius(aantalTjirpsPerMinuut)

print('temperatuur (Fahrenheit):', aantalGradFahr)
print('temperatuur (Celsius):', aantalGradCelc)