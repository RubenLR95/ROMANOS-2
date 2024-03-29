'''
1-Crear una funcion que pase de entero >0 y <4000 a romano
2-cualquier otra entrada debe dar error
3-limite 3999

Casos de prueba
a)1994 -> MCMXCIV
b)4000 -> RomanNumberError("El valor debe ser menor de 4000")
c)"unacadena"-> RomanNumberError("Debe ser un entero")
d) 0-> RomanNumberError("El valor debe ser mayor de cero")
e) -3 ->RomanNumberError("El valor debe ser mayor de cero")
f) 4.5 -> RomanNumberError("Debe ser un entero")

M → 1000
D → 500
C → 100
L → 50
X → 10
V → 5
I → 1
'''



dic_entero_a_romano= {1:'I' ,2: 'II' ,3: 'III' ,4: 'IV' , 5: 'V' , 6: 'VI' ,  7: 'VII' , 8: 'VIII', 9: 'IX', 
                      10: 'X' , 20: 'XX' , 30: 'XXX' ,  40: 'XV' , 50: 'L' , 60: 'LX' , 70: 'LXX' , 80: 'LXXX' , 90: 'XC', 
                      100: 'C' , 200: 'CC' , 300: 'CCC' ,400: 'CD' , 500: 'D' , 600: 'DC' ,700: 'DCC' , 800: 'DCCC' , 900: 'CM', 
                      1000: 'M' , 2000: 'MM' , 3000: 'MMM'}

dic_romano_a_entero={
    'I' : 1, 'V': 5, 'X':10,
    'L':50, 'C':100, 'D':500, 
    'M':1000
}



class RomanNumberError( Exception ):
    pass

def romano_a_entero(romano:str)->int:
    valor_entero = 0
    lista_romano = list(romano)
    longitud = len(lista_romano)

    for pos in range(longitud):
        if pos != 0:
            if dic_romano_a_entero.get(lista_romano[pos-1]) <  dic_romano_a_entero.get(lista_romano[pos]):
                valor_entero -=dic_romano_a_entero.get(lista_romano[pos-1])
                valor_entero += (dic_romano_a_entero.get(lista_romano[pos]) - dic_romano_a_entero.get(lista_romano[pos-1]))
            else:
                 valor_entero += dic_romano_a_entero.get(lista_romano[pos])
        else:
            valor_entero += dic_romano_a_entero.get(lista_romano[pos])


    '''
    for i in romano:
        valor_entero += dic_romano_a_entero.get(i , 0)    
    '''

    return valor_entero 
  
print(romano_a_entero("IX")) 

#1994
def entero_a_romano(numero:int)->str:

    numero = "{:0>4d}".format(numero)#transforma el numero dado a un str de 4 digitos, y si es menos lo complementa con ceros a la izquierda
    list_numero = list(numero)#transforma el str dado a una lista de string de cada caracter 
    valor_romano = ""

    cont = 0
    valor_num = 1000
    while cont < len(list_numero):
        list_numero[cont] = int(list_numero[cont])*valor_num
        valor_romano += dic_entero_a_romano.get(list_numero[cont])
        cont+=1
        valor_num /= 10

   
#print( entero_a_romano(1994) )
