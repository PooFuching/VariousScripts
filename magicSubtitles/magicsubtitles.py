import re

class Tiempo:
    hora='00'
    minuto='00'
    segundo='00'
    milisegundo='00'

    def __init__(self, hh, mm, ss, mmmm):
        self.hora= hh
        self.minuto= mm
        self.segundo= ss
        self.milisegundo= mmmm

    def __str__(self):
        return ("{}:{}:{},{}".format(self.hora, self.minuto, self.segundo, self.milisegundo))

def Inicio():
    dialogo = []

    h_dialogo=m_dialogo=s_dialogo=mm_dialogo = 0
    nom_sub =''
    print('Ingrese el tiempo en el que comienza el dialogo.')
    print('hh')
    h_dialogo=input()
    dialogo.append(h_dialogo)
    print('mm')
    m_dialogo=input()
    dialogo.append(m_dialogo)
    print('ss')
    s_dialogo=input()
    dialogo.append(s_dialogo)
    print('mm mm')
    mm_dialogo=input()
    dialogo.append(mm_dialogo)
    stop = 0 
    limit = len(dialogo)
    while stop < limit:
        valor = str(dialogo[stop])
        print(valor)
        dialogo.append(str(valor))
        stop+=1
    print(dialogo)
    #tiempo_dialogo = Tiempo(h_dialogo,m_dialogo,s_dialogo,mm_dialogo)
    #print(tiempo_dialogo)
    input()
    print('Ingrese el nombre del subtitulo.')
    nom_sub=input()
    print(nom_sub)
    input()

    ObtencionTiempo(dialogo)

def ObtencionTiempo(dialogo):
    dialogo = dialogo
    subtitulo = open('Blade Runner 2049 old.srt')
    print(subtitulo.name)
    ##Patron de reconocimiento
    patron = re.compile(r'[0-9]+:')
    lista_Tsub = []

    input()
    #
    for line in subtitulo:
        if re.match(patron, line):
            lista_Tsub.append(line)
            print(line)
    input()

    CalculoDiferencial(lista_Tsub, dialogo)

def CalculoDiferencial(lista_Tsub, dialogo):
    lista_Tsub = lista_Tsub
    dialogo = dialogo
    tiempo_diferencial = []

    for line in lista_Tsub:
        valor=''
        tiempo_linea = []
        i=0
        for char in line:
            if char==':' or char==',' or char==' ' or char==chr(10):
                i+=1
                tiempo_linea.append(str(valor))
                print(valor)
                valor=''
            elif char.isnumeric():
                valor+=str(char)
        pos = 0
        for valor in tiempo_linea:
            cambio = (int(dialogo[pos])-int(valor))
            valor = str(int(valor)-int(cambio))
            #print(cambio)
            input()
            pos+=1

        print(line)
        input()
                #tiempo_linea[i]=(str(tiempo_linea[i])+str(char))
        #print(tiempo_linea)
        #print(len(tiempo_linea))
        #input()
    input()
    print(lista_Tsub)
    input()


Inicio()
