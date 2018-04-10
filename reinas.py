import math

# ListTodasFilas=[]
# ListTodasColumnas=[]
# ListTodasDiagonal=[]
# Listmarcado=[]

# def diagonales(Casilla,Diagonal):
#     Dia=Casilla[0]-Casilla[1]
#     Start=[Casilla[0]-Dia,Casilla[1]-Dia]
#     Final=[Casilla[0]+Dia,Casilla[1]-Dia]
#     for i in range(0,8-Dia):
#         if Start[0]+i <= 8 and Start[1]+i <= 8 and Start[0]+i > 1 and Start[1]+i > 1:
#             Diagonal.append( [ Start[0]+i , Start[1]+i ])
#     for i in range(0,Final[0]):
#         if Final[0]-i <= 8 and Final[1]+i <= 8 and  Final[0]-i > 1 and Final[1]+i > 1 :
#             Diagonal.append( [ Final[0]-i , Final[1]+i ])


def checkcomer():
    if len(ListTodasColumnas) != list(set(ListTodasColumnas)) or len(ListTodasFilas) != list(set(ListTodasFilas)) or len(ListTodasDiagonal) != list(set(ListTodasDiagonal)):
        print("false")
    else:
        print("true")


def comer(erase,helpposicion): # Incrementar las putas diagonales correctamente 
    for i in Reinas:
        if i.Columna != erase and erase not in i.notallow:
            i.notallow.append(erase)
            if erase+abs(i.Fila-helpposicion) <= 8 and erase+abs(i.Fila-helpposicion) not in i.notallow:
                i.notallow.append( erase+abs(i.Fila-helpposicion) )
            if erase-abs(i.Fila-helpposicion) >= 1 and erase-abs(i.Fila-helpposicion) not in i.notallow:
                i.notallow.append (erase-abs(i.Fila-helpposicion) )
                

def revisar():
    for i in Reinas:
        comer(i.Columna,i.Fila)

    


class reina(object):

    def __init__(self, fila, columna,positioned,tried,allow):
        self.Fila = fila
        self.Columna = columna
        self.positioned = positioned
        self.tried = tried
        self.notallow = allow


Reinas=[]

for i in range(8):
    Reinas.append(reina(i+1,0,False,[],[]))


def TES():
    for reina in Reinas:
        # ListTodasColumnas.append(reina.Columna)
        # ListTodasFilas.append(reina.Fila)
        # ListTodasDiagonal.append(reina.Fila-reina.Columna)
        print("la reina ", reina.Fila, "está en ",reina.Fila,reina.Columna, "PROHIBIDO",reina.notallow)


ListPass=[]
intento= 1
READY = False
SET = False
while READY != True:
    for i in Reinas:
        SET = False
        while SET != True:
            if intento not in i.notallow and intento not in i.tried:
                i.Columna=intento
                i.tried.append(intento)
                i.positioned=True
                comer(i.Columna,i.Fila)
                if intento <= 7:
                    intento += 1
                SET = True
            else:
                if intento <= 7:
                    intento += 1
                else:
                    SET = True
        TES()
        print(intento)
    Counter=0
    for i in Reinas:   
        if i.Columna != 0:
            Counter += 1
    if Counter == 8:    
        READY = True
    else:
        for i in Reinas:
            if i.positioned==False:
                #Desposicionar la anterior y comer de nuevo y añadir su Columna actual en notAllow

                SET = False


TES()
checkcomer()
