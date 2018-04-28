import math

def TES(List):
    global GlobalCounter
    print('Solucion: ', GlobalCounter )
    for i in range(8):
        pinter=[]
        for x in range(8):  
            if List[i] == x:
                pinter.append('[X]')
            else:
                pinter.append('[ ]')
        print(pinter)
    print(' ')


def Check(Fila,Col,intento):
    for i in range(intento):
        if Fila[i] == Col or Fila[i] - i == Col - intento or Fila[i]  + i == Col + intento:
            return False
    return True


def Comer(Fila,intento):
    global GlobalCounter
    if intento == 8:
        GlobalCounter += 1
        TES(Fila)
    else:     
        for Col in range(8):
            if Check(Fila,Col,intento) == True:
                Fila[intento] = Col
                Comer( Fila , intento + 1)


def Sol():
    global GlobalCounter
    GlobalCounter = 0
    ListNumber = [0,0,0,0,0,0,0,0]
    Comer(ListNumber, 0 )

Sol()