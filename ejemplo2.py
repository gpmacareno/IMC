def calcular_imc(peso, altura):
    # Calcula el IMC
    imc = peso / (altura ** 2)
    
    # Categorías de peso
    categorias = [
        ("Bajo peso", 16),
        ("Bajo peso", 16.9),
        ("Peso saludable", 17),
        ("Peso saludable", 18.4),
        ("Sobrepeso", 18.5),
        ("Sobrepeso", 24.9),
        ("Obesidad tipo 1", 25),
        ("Obesidad tipo 2", 29.9),
        ("Obesidad tipo 3", 34.9),
        ("Obesidad tipo 4", 35)
    ]
    
    # Determina la categoría de peso
    for categoria, limite in categorias:
        if imc <= limite:
            return f"Tu IMC es {imc:.2f}, lo que corresponde a: {categoria}"
    
    # Si el IMC es mayor que 35, se considera obesidad tipo 4
    return f"Tu IMC es {imc:.2f}, lo que corresponde a: Obesidad tipo 4"

# Ingresa tu peso en kilogramos y altura en metros
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

# Llama a la funci5ón para calcular el IMC y mostrar la categoría de peso
resultado = calcular_imc(peso, altura)
print(resultado)
