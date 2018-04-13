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
    h_dialogo=m_dialogo=s_dialogo=mm_dialogo = 0
    nom_sub =''
    print('Ingrese el tiempo en el que comienza el dialogo.')
    print('hh')
    h_dialogo=input()
    print('mm')
    m_dialogo=input()
    print('ss')
    s_dialogo=input()
    print('mm mm')
    mm_dialogo=input()
    tiempo_dialogo = Tiempo(h_dialogo,m_dialogo,s_dialogo,mm_dialogo)
    print(tiempo_dialogo)
    input()
    print('Ingrese el nombre del subtitulo.')
    nom_sub=input()
    print(nom_sub)
    input()

    ObtencionTiempo()

def ObtencionTiempo():
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

    CalculoDiferencial(lista_Tsub)

def CalculoDiferencial(lista_Tsub):
    lista_Tsub = lista_Tsub
    tiempo_diferencial = []
    for line in lista_Tsub:
        tiempo_linea = []
        i=0
        for char in line:
            if char==':' or char==',' or char==' ':
                i+=1
            elif char.isnumeric():
                tiempo_linea.append(str(char))
                print(tiempo_linea[i])
                #tiempo_linea[i]=(str(tiempo_linea[i])+str(char))
        print(tiempo_linea)
        print(len(tiempo_linea))
        input()
        


Inicio()
