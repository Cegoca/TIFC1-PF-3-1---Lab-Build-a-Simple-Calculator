num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma_inicial = num1 + num2
print(f"Resultado de la suma: {suma_inicial}")

""" Se declaran dos variables de tipo float para que permita decimales: 
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

Se declara una variable para brindar el resultado:   suma_inicial
suma_inicial = num1 + num2 print(f"Resultado de la suma: {suma_inicial}")
La función print despliega el resultado de la suma de num1+num2 anticipando el texto: Resultado de la suma o sea que en la variable:  suma_inicial se guardará el resultado. 
"""



# --- EXTRA actividad ---



def menu_extra():
    print("\n--- FUNCIONES EXTRA ---")
    print("1. Restar el segundo número del primero")
    print("2. Multiplicar dos números")
    print("3. Dividir el primer número por el segundo")
    print("4. Operación módulo (resto)")
    print("5. Sumar 3 números")
    print("6. Evaluar expresión personalizada con 3 o más números")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"Resultado: {a - b}")

    elif opcion == "2":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"Resultado: {a * b}")

    elif opcion == "3":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Error: No se puede dividir entre cero.")

    elif opcion == "4":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        if b != 0:
            print(f"Resultado del módulo: {a % b}")
        else:
            print("Error: No se puede realizar el módulo entre cero.")

    elif opcion == "5":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        c = float(input("Tercer número: "))
        print(f"Resultado de la suma: {a + b + c}")

    elif opcion == "6":
        expresion = input(
            "Ingrese la expresión (ejemplo: 2 + 4 - 3 o 4 * 5 + 1 / 3): "
        )
        try:
            # eval calcula operaciones combinadas respetando la jerarquía matemática
            resultado = eval(expresion)
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Expresión inválida: {e}")



menu_extra()