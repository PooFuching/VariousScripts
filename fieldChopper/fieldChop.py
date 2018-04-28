archivo = ''
contenido=''
chop=[]
separado=''
chop.append(chr(10))
archivo=input('Ingrese la direccion del archivo.')
contenido=open(archivo)

while True:
	spliter=input('Ingrese un delimitador o presione 0 para salir.')
	if spliter == '0':
		break
	elif spliter == '':
		break
	else:
		chop.append(spliter)


li=0

for line in contenido:
	separado+=str(li)+': '
	linea_separada=[]
	gr=0
	valor=''
	li+=1
	last_char=len(line)-1

	for char in line:
		if char in chop:
			if valor != '':
				print(str(li)+':'+valor)
				input()
				linea_separada.append(valor)
			valor=''
			gr+=1
		elif char is line[last_char] or char==chr(10):
			valor+=char
			print(str(li)+':'+valor)
			input()
			linea_separada.append(valor)
			valor=''
			break
		else:
			valor+=char
	cont=1
	for grupo in linea_separada:
		separado+=str(cont)+':'+str(grupo)+'. '
		cont+=1
	separado+=chr(10)

print(separado)
	#for spliter in chop:
	#	if spliter == char:
	#		i+=1
	#		linea_separada=''
	#	else:
	#		linea_separada+=char
#separado+=linea_separada

#print(separado)

