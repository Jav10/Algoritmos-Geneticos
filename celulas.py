import numpy as np

#Creando la matriz
tablero = np.zeros(30)
tableroFuturo = np.zeros(30)
#Estado inicial
tablero[1] = 1
tablero[4] = 1
tablero[5] = 1
tablero[7] = 1
tablero[9] = 1
tablero[11] = 1
tablero[13] = 1
tablero[14] = 1
contador = 0

def buscarCelulas(matrizBC):
	for j in range(30):
		valor = matrizBC[j]
		buscarVecinos(matrizBC,j, valor)
			
	global tableroFuturo
	cambio(matrizBC, tableroFuturo)
	rellenarZero()
	'''
	global tableroFuturo
	buscarVecinos(matrizBC,2,3,0)
	print(tableroFuturo)'''

def buscarVecinos(matriz, n, valor):
	global contador
	#Si n=0
	if(n==0):
		for j in range(n+1,n+3):
			print("n = ",j, "valor = ",matriz[j], "n=0") #BORRAR ESTO
			if(j==n):
				pass
			else:
				if(int(matriz[j]) == 1):
					contador = contador + 1
			
	
	#Si n=1
	elif(n==1):
		for j in range(n-1,n+3):
			print("n = ",j, "valor = ",matriz[j],"n=1") #BORRAR ESTO
			if(j==n):
				pass
			else:	
				if(int(matriz[j]) == 1):
					contador = contador + 1
			

	#Si 2<=n<=27
	elif(n>=2 and n<=27):
		for j in range(n-2,n+3):
			print("n = ",j, "valor = ",matriz[j],"2<=n<=27") #BORRAR ESTO
			if(j==n):
				pass
			else:	
				if(int(matriz[j]) == 1):
					contador = contador + 1	
					
	#Si n=28
	elif(n==28):
		for j in range(n-2,n+2):
			print("n = ",j, "valor = ",matriz[j],"n=28") #BORRAR ESTO
			if(j==n):
				pass
			else:	
				if(int(matriz[j]) == 1):
					contador = contador + 1	

	#Si n=29
	elif(n==29):
		for j in range(n-2,n):
			print("n = ",j, "valor = ",matriz[j],"n=29") #BORRAR ESTO
			if(j==n):
				pass
			else:	
				if(int(matriz[j]) == 1):
					contador = contador + 1				
						

	print("Contador=",contador,"buscando en n: ",n) #BORRAR ESTE PRINT
	vm = vidaMuerte(contador, valor)
	global tableroFuturo
	#Cambiar valor AUN FALTA VER COMO
	if(vm == True):
		tableroFuturo[n] = 1
	elif(vm == False):
		tableroFuturo[n] = 0
		
	contador = 0	
		
#Verificar vida o muerte de celula		
def vidaMuerte(c, v):
	if(v == 0):
		if(c==3):
			return True
		else:
			return False
	elif(v == 1):
		if(c>=2):
			return True
		else:
			return False

#Reiniciar tablero futuro	
def rellenarZero():
	global tableroFuturo
	tableroFuturo = np.zeros(30)

#Cambiar tableroFuturo por tablero
def cambio(t, tf):
	for j in range(30):
		t[j] = tf[j]
	


#Iniciar el Juego
#Estado inicial

print("Estado inicial")
print(tablero)	
for i in range(3):
	print("/nIteración: ", i+1)
	buscarCelulas(tablero)
	print(tablero)
	termino = 0
	for i in tablero:
		if (i == 1):
			termino = termino + 1
	if(termino == 30):
		print("Llego hasta la meta. Sobrepoblación.")
		break
	
