print("Calculadora con una sola variable \n")
 
print("^^^^^^^^^^^^^^^^^^^^")
print("^ Menù de opciones ^")
print("^^^^^^^^^^^^^^^^^^^^ \n")

print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Division entera")
print ("6. Exponente")
print ("7. Modulo o eesto \n")

calculadora = int(input("Introduce la opciòn deseada:"))

if calculadora == 1:
    print("Elegiste Suma \n")
    calculadora = int(input("introduce el primer numero:"))
    calculadora += int(input("Introduce el segundo numero:"))
    print("El resulado de la suma es: " + str(calculadora))
    
elif calculadora == 2:
    print("Elegiste Resta \n")
    calculadora = int(input("introduce el primer numero:"))
    calculadora -= int(input("Introduce el segundo numero:"))
    print("El resulado de la Resta es: " + str(calculadora))

elif calculadora == 3:
    print("Elegiste Multiplicar \n")
    calculadora = int(input("introduce el primer numero:"))
    calculadora *= int(input("Introduce el segundo numero:"))
    print("El resulado de la Multiplicacion es: " + str(calculadora))

elif calculadora == 4:
    print("Elegiste Division \n")
    calculadora = float(input("introduce el primer numero:"))
    calculadora /= float(input("Introduce el segundo numero:"))
    print("El resulado de la Division es: " , round(calculadora,2))

elif calculadora == 5:
    print("Elegiste Division entera \n")
    calculadora = int(input("introduce el primer numero:"))
    calculadora //= int(input("Introduce el segundo numero:"))
    print("El resulado de la Division entera es: " , str(calculadora))

elif calculadora == 6:
    print("Elegiste Exponente \n")
    calculadora = int(input("introduce el primer numero:"))
    calculadora **= int(input("Introduce el segundo numero:"))
    print("El resulado del Exponente es: " , str(calculadora))

elif calculadora == 7:
    print("Elegiste Modulo o resto \n")
    calculadora = int(input("introduce el primer numero:"))
    calculadora %= int(input("Introduce el segundo numero:"))
    print("El resulado del Modulo o resto es: " , str(calculadora))
    
else:
    print("\n !!!!Debe elegir los numeros del menu de opciones!!!")
    


