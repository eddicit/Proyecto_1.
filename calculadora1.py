number1=int(input("Ingresa un número:")) #inicio de la calculadora ingreso de datos
number2=int(input("Ingresar otro número:")) #ingreso del segundo dato
 
elección=0
 
while elección != 6: #incio de menú de la calculadora
    print("""
    Indique la opercación a realizar:
 
    1)Suma #la suma
    2)Resta #la resta
    3)Multiplicación #la multiplicación
    4)Divivsión #la División
    5)Cambio de valores #esto es por is alguin ya no queire sumar si no que quiere multiplicar o viceversa
    6)Salir #la opción de salida de la calculadora
    """) #termina el menú
 
    elección=int(input())
 
    if elección == 1:
        print(" ")
        print("Resultado: ",number1,"+",number2,"=",number1+number2) #codigo para la suma
    elif elección == 2:
        print(" ")
        print("Resultado: ",number1,"-",number2,"=",number1-number2) #codigo para resta
    elif elección == 3:
        print(" ")
        print("Resultado: ",number1,"*",number2,"=",number1*number2) #codigo para multiplicación
    if elección == 4:
        print(" ")
        print("Resultado: ",number1,"/",number2,"=",number1/number2) #codigo para División
    elif elección == 5:
        number1=int(input("Ingresa un número:")) #Codigo para salida
        number2=int(input("Ingresar otro número:")) #esto es para ingresar el dato diferente que se quiera dar
    elif elección == 6:
        print("Gracias por usar la Calculadora.Creadada por: Mendoza") #Mensaje de salida