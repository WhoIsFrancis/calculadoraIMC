peso = int(input("Ingrese su peso en kg. : "))
estatura = (float(input("Ingrese su estatura en metros. : ")))

imc = peso / (estatura * 100)

print("Su indice de masa corporal es de: ", round(imc, 2))
