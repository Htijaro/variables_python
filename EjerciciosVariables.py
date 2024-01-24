#1. Programa que permita multiplicar 3 números

print (5 * 5 * 5)

#2. Solicitar al usuario un número y calcular cuál es el cuadrado del número (2**2=4).

numero = float (input ("Digite un número para saber cuál es el cuadrado: "))
print("El número ingresado al cuadrado es:", numero * numero)

#3. Programa para calcular la distancia recorrida en un movimiento rectilíneo. 
#   Recuerde x = v * t donde v es velocidad y t es tiempo. 
#   Solicitar al usuario velocidad en kilómetros por hora (Km/h) 
#   y tiempo en horas (h) para obtener la distancia en kilómetros (Km).

v = float (input("Digite la velocidad expresada en Km/h: "))
t = float (input("Digite el tiempo expresado en horas: "))
print("La distancia recorrida es:", v * t, "km")


#4. Programa que permita calcular la edad de una persona 
#   conociendo el año actual y el usuario digita su año de nacimiento.

fecha_nacimiento = int(input("Digite su año de nacimiento: "))
fecha_hoy = int (2024)

edad =  fecha_hoy - fecha_nacimiento
print ("su edad es:", edad, "años")


#5. Programa para calcular el 20% de cualquier número de entrada.

num = float(input("Digite un número al que le quiera sacar el 20 %: "))

print ("El 20% es:", num * 0.20)


#6. Programa que permita calcular el 30%, el 60% y el 90% de cualquier número.

num = float(input("Digite un número al que le quiera sacar el 30%, el  60% y el 90%: "))

print ("El 30% es:", num * 0.30,  "\nel 60% es:", num * 0.60,"\ny el 90% es:", num * 0.90)


#7. Programa para calcular el área de un cuadrado, la longitud de un lado la ingresa el usuario.

lado = float(input("Digite tamaño deseado expresado en metros del lado del cuadrado: "))

print ("El área del cuadrado es: ", lado * lado, "m2")


#8. Programa que permita ingresar 5 números y calcular el promedio.

num1 = float(input("Digite el primer número: "))
num2 = float(input("Digite el segundo número: "))
num3 = float(input("Digite el tercer número: "))
num4 = float(input("Digite el cuarto número: "))
num5 = float(input("Digite el quinto número: "))

promedio = (num1 + num2 + num3 + num4 + num5) /5 

print ("El promedio es: ", promedio)


#9. Programa que permita a una tienda saber el valor que pagará un cliente por la compra 
#   de varios elementos de la misma referencia. 
#   Debe tener como entradas el valor unitario, la cantidad de productos comprados y al 
#   valor final se debe adicionar el 16% correspondiente al IVA.

producto = float(input("Digite el valor unitario: "))
cantidad = float(input("Digite cantidad de artículos: "))
iva = float (0.16)

subtotal = (producto * cantidad)
impuesto = (subtotal * iva) 
total = (subtotal + impuesto)  

print ("Subtotal:", subtotal)
print ("Impuestos 16%: ", impuesto)
print ("El valor a pagar es: ", total)


#10. Programa que permita determinar el salario a pagar a un empleado, 
#    teniendo como entradas el salario diario y el número de días trabajados. 
#    Tenga en cuenta que al empleado se le debe descontar el 10% por concepto 
#    de pensión y 15% por concepto de salud.

salario_diario = float(input("Digite el salario diario: "))
dias_trabajados = int(input("Digite número de días laborados: "))
pension = float (-0.10)
salud = float (-0.15)

salario = (salario_diario * dias_trabajados)
deducciones = ((salario) * (pension + salud)) 
total = (salario + deducciones)  

print ("Salario:", salario)
print ("deducciones: ", deducciones)
print ("El valor a pagar es: ", total)


#11. Programa que solicite un número al usuario y permita calcular la raíz cuadrada del mismo 
#    (sin usar función). 

num = float(input("Digite el número al que le quiera sacar la raíz cuadrada: "))
raiz = num ** 0.5

print ("La raíz cuadrada es:", raiz)


#12. Calcular la hipotenusa con el Teorema de Pitágoras.

ab = float(input("Digite el valor del vértice ab: "))
bc = float(input("Digite el valor del vértice bc: "))


hipotenusa = (ab **2 + bc **2)** 0.5
print ("La longitud de hipotenusa es:", hipotenusa)



#13. Solicitar tiempo en segundos y transformar a horas y minutos.

segundos = int(input("Digite el tiempo expresado en segundos: "))
minutos = int(segundos /60)
horas = int(segundos /3600)

print ("El tiempo expresado en minutos es: ",minutos)
print ("El tiempo expresado en horas es:", horas,)


#14. Solicitar al usuario una distancia en metros y transformar a km., cm. o mm.

metros = int(input("Digite distancia expresada en metros: "))
milimetros = int(metros * 1000)
centimetros = int(metros * 100)
kilometros = float(metros / 1000)

print ("La  distancia expresada en milímetos es: ",milimetros)
print ("La  distancia expresada en centímetros es:", centimetros,)
print ("La distancia expresada en Kilómetros es:", kilometros)



