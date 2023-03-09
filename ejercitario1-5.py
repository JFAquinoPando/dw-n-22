"""
5- Calcular el nuevo salario de un obrero si obtuvo un incremento
del X% sobre su salario anterior."""

salario = int(input("Ingrese su salario anterior para calcular el nuevo: "))
porcentaje = float(input("Ingrese el porcentaje para aumento: "))
salarioNuevo = salario * (100 + porcentaje)/100
print(type(salario), salario, salarioNuevo)