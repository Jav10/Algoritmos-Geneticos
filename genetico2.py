import numpy as np
'''El cross-over: Toma los 2 mejores de la primera generación y crea 2 combinaciones'''
def seno(x):
	global senol
	senol.append(np.sin(x))

def fitness(x): 
	global fitnessl
	fitnessl.append(50 * (np.sin(x) + 1))
	
def entero(x):
	global enterol
	contador = 0
	potencias = {7:0,6:1,5:2,4:3,3:4,2:5,1:6,0:7}
	for i in range(7,-1,-1):
		if(x[i]==1):
			contador += 2**(potencias[i])
			
	enterol.append(contador)		
			
def porcentaje(x):
	global porcentajel
	contador = 0
	for i in x:
		contador += i
	for i in x:
		r = i/contador
		porcentajel.append(round(r*100,2))
		
def vaciar():
	global senol
	global fitnessl
	global enterol
	global porcentajel
	senol = []
	fitnessl = []
	enterol = []
	porcentajel = []
	
def crossover(x,y):
	xnuevo = [0,0,0,0,0,0,0,0]
	ynuevo = [0,0,0,0,0,0,0,0]
	mnuevo = [0,0,0,0,0,0,0,0]
	nnuevo = [0,0,0,0,0,0,0,0]
	#Primer combinación
	for i in range(8):
		if(i<4):
			xnuevo[i] = x[i]
			ynuevo[i] = y[i+4]
		elif(i>3):
			xnuevo[i] = y[i]
			ynuevo[i] = x[i-4]
	#Segunda combinación
	for i in range(8):
		if(i<4):
			mnuevo[i] = y[i]
			nnuevo[i] = x[i+4]
		elif(i>3):
			mnuevo[i] = x[i-4]
			nnuevo[i] = y[i]	
	return xnuevo,ynuevo,mnuevo,nnuevo		

def seleccionar():
	global cromosomas
	global fitnessl
	cromo = [0,0,0,0]
	valor = [0,0]
	posicion = [0,0]
	for i in range(2):
		valor[i] = max(fitnessl)
		posicion[i] = fitnessl.index(valor[i])
		centinela = posicion[i]
		fitnessl[int(centinela)] = -1
	for i in range(2):
		centinela = posicion[i]
		valor = cromosomas[int(centinela)]
		cromo.insert(i,valor)
	cromo[0],cromo[1],cromo[2],cromo[3] = crossover(cromo[0],cromo[1])
	for i in range(4):
		cromosomas[i] = cromo[i]	

		
senol = []
fitnessl = []
enterol = []
porcentajel = []

		
c1 = np.random.randint(0,2,8)
c2 = np.random.randint(0,2,8)
c3 = np.random.randint(0,2,8)
c4 = np.random.randint(0,2,8)

cromosomas = [list(c1),list(c2),list(c3),list(c4)]
#Iteraciones
for i in range(10):
	terminar = False
	print("Generación {}".format(i+1))
	#Para generar los valores enteros
	for i in cromosomas:
		entero(i)
	#Para generar los valores de f(x)
	for i in enterol:
		seno(i)
	#Para generar fitness
	for i in enterol:
		fitness(i)
	#Para generar el porcentaje	
	porcentaje(fitnessl)
	
	#Mostrar tabla
	print("Cromosomas\tGenes\t\t\t\tValorEntero\tf(x)\tfitness\tPorcentaje\n")
	for i in range(4):
		print("{0}\t\t{1}\t{2}\t\t{3}\t{4}\t{5}\n".format(i,cromosomas[i],enterol[i],round(senol[i],2),round(fitnessl[i],2),porcentajel[i]))
	
	for i in fitnessl:
		if(int(i)>95):
			print("fitness entero",int(i))
			terminar = True
	if(terminar == True):
		print("Llego a la meta!")
		break
	seleccionar()
	
	vaciar()
else:
	print("Terminaron las iteraciones.")


input()
