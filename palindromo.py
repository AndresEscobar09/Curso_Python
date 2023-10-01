
x = 1
while (x>0):

    palabra = input('ingrese una palabra para verificar si es un palindromo\n')
    palabra1 = ''
    x = len(palabra)


    for i in range(x-1,-1,-1):
        palabra1 = palabra1 + palabra[i]

    if palabra == palabra1 and len(palabra) > 1:
        print('la palabra "',palabra,'" si es un palindromo\n')
    else:
        print('la palabra "',palabra,'" no es un palindromo\n')

quit()