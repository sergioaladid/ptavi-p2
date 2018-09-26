#!/usr/bin/python3
# -*- coding: utf-8 -*-
# comentario

import sys


class Calculadora:


	def plus(self, op1, op2):
	    """ Function to sum the operands. Ops have to be ints """
	    return op1 + op2


	def minus(self, op1, op2):
	    """ Function to substract the operands """
	    return op1 - op2

micalc = Calculadora()
 #micalc.minus(3,1)

if __name__ == "__main__":

    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = micalc.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = micalc.minus(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
