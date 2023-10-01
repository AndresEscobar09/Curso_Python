

while True :
    entrada = input('ingrese un numero para conocer su factorial:\n')
    factorial = 1  
    try :
        numero = int(entrada)

    except :
        print('no se ingresado numeros, por favor intente de nuevo \n')
        continue

    for i in range(1,numero+1) :
        factorial = factorial*i
        

    print('el factorial de ',entrada,' es: ',factorial)
    quit()
