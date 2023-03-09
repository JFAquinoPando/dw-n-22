"""
6- Leer dos números,
si son iguales que se multipliquen,
si el
primero es mayor que el segundo que se resten y 
sino que se
sumen.
"""
numero1 =  int(input("Ingrese un valor para el numero 1:"))
numero2 = int(input("Ingrese un valor para el numero 2:"))

if numero1 == numero2:
    print("Son iguales, por ende los multiplico: ", numero2 * numero1)
elif numero1 > numero2:
    print("El primero es mayor que el segundo, por eso los resto:", numero1 - numero2)
else:
    print("El segundo es mayor que el primero, por eso los sumo:", numero2 + numero1)