"""
Las personas para la jubilación por
edad deben tener 60 años o más y una antigüedad en su empleo
de menos de 25 años.


Las personas para la jubilación por antigüedad joven deben tener
menos de 60 años y una antigüedad en su empleo de 25 años o
más.
Las personas para antigüedad adulta deben tener 60 años o más
y una antigüedad en su empleo de 25 años o más
"""
edad = int(input("Introduce por favor tu edad: "))
antiguedadLaboral = int(input("Introduce por favor tu antigüedad laboral: "))

if edad >= 60 and antiguedadLaboral < 25:
    print("Entras en jub. por edad")
elif edad < 60 and antiguedadLaboral >= 25:
    print("Entras en jub. por antigüedad joven")
elif edad >= 60 and antiguedadLaboral >= 25:
    print("Entras en jub. por antigüedad adulta")
else:
    print("No te jubilar aún")