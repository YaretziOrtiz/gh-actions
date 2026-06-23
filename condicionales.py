import os

edad=int(os.getenv("EDAD"))
nombre=os.getenv("NAME")
if edad >= 18:
    print(f"{nombre} es mayor de edad")
else:
    print(f"{nombre} es menor de edad")