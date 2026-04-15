temperatures = list()
temperature = int(input("Enter temperature: "))

centigrade = lambda centigrade_unit : (temperature - 32) / 1.8

fahrenheit = str((temperature - 32) / 1.8)
fahrenheit += " fahrenheit"


result = list(map(centigrade, temperatures))
result.append(fahrenheit)
temperature_with_unit = str(temperature)
temperature_with_unit += " centigrade"
result.insert(0, temperature_with_unit)


print(result)
