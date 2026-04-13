temperatures = list()
temperature = int(input("Enter temperature: "))

c = lambda cel : (temperature - 32) / 1.8

f = str((temperature - 32) / 1.8)
f += " f"


result = list(map(c, temperatures))
result.append(f)
celc = str(temperature)
celc += " c"
result.insert(0, celc)


print(result)
