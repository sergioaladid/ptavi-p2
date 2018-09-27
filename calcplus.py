#!/usr/bin/python3
# -*- coding: utf-8 -*-
# comentario

import sys


class CalculadoraHija:


	def plus(self, op1, op2, op3, op4, op5):
	    """ Function to sum the operands. Ops have to be ints """
	    return ((((op1 + op2) + op3) + op4) + op5)


	def minus(self, op1, op2, op3, op4, op5, op6):
	    """ Function to substract the operands """
	    return (((((op1 - op2) - op3) - op4) - op5) - op6)
	    
	def multiply(self, op1, op2, op3):
	    """ Function to substract the operands """
	    return ((op1 * op2) * op3)
	    
	def divide(self, op1, op2, op3):
	    """ Function to substract the operands """
	    if op2 != 0:
	        return ((op1 / op2) / op3)
	    else:
		    sys.exit('Division by zero is not allowed.')

micalc = CalculadoraHija()


if __name__ == "__main__":
    try:
        fich = (sys.argv[1])
        
    except ValueError:
        sys.exit("Error: No has introducido el fichero.txt")

   
    with open(fich) as fp:  
        
        for line in (fp):
            
            lista = line.split(",")
            operacion = (lista[0])
            

            if operacion == "suma":
                 ope1 = int(lista[1])
                 ope2 = int(lista[2])
                 ope3 = int(lista[3])
                 ope4 = int(lista[4])
                 ope5 = int(lista[5])
                 result = micalc.plus(ope1, ope2, ope3, ope4, ope5)
            elif operacion == "resta":
                 ope1 = int(lista[1])
                 ope2 = int(lista[2])
                 ope3 = int(lista[3])
                 ope4 = int(lista[4])
                 ope5 = int(lista[5])
                 ope6 = int(lista[6])
                 result = micalc.minus(ope1, ope2, ope3, ope4, ope5, ope6)
            elif operacion == "multiplica":
                 ope1 = int(lista[1])
                 ope2 = int(lista[2])
                 ope3 = int(lista[3])
                 result = micalc.multiply(ope1, ope2, ope3)
            elif operacion == "divide":
                 ope1 = int(lista[1])
                 ope2 = int(lista[2])
                 ope3 = int(lista[3])
                 result = micalc.divide(ope1, ope2, ope3)
            else:
                 sys.exit('Operación sólo puede ser sumar, restar, multiplicar o dividir.')


            print(result)

