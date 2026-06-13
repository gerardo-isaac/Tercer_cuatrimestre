def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


continuar = "si"

while continuar == "si":
    base = float(input("Ingresa la base del triángulo: ")).strip()
    altura = float(input("Ingresa la altura del triángulo: ")).strip()

    resultado = calcular_area_triangulo(base, altura)

    print("El área del triángulo es:", resultado)

    continuar = input("¿Quieres calcular otra área? si/no: ").strip()