import numpy as np

#Creando la matriz
tablero = np.zeros((16,16))
tableroFuturo = np.zeros((16,16))
#Estado inicial
tablero[0,1] = 1
tablero[1,2] = 1
tablero[2,0] = 1
tablero[2,1] = 1
tablero[2,2] = 1
contador = 0

def buscarCelulas(matrizBC):
	for i in range(16):
		for j in range(16):
			valor = matrizBC[i][j]
			buscarVecinos(matrizBC, i, j, valor)
			
	global tableroFuturo
	cambio(matrizBC, tableroFuturo)
	rellenarZero()
	'''
	global tableroFuturo
	buscarVecinos(matrizBC,2,3,0)
	print(tableroFuturo)'''

def buscarVecinos(matriz, n, m, valor):
	global contador
	#Si n=0 y m=0
	if(n==0 and m==0):
		for i in range(n+2):
			for j in range(m+2):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j], "n=0 y m=0") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:
					if(int(matriz[i][j]) == 1):
						contador = contador + 1
	
	#Si n=0 y 0<m<15
	elif(n==0 and (m>0 and m<15)):
		for i in range(n+2):
			for j in range(m-1,m+2):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j],"n=0 y 0<m<15") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:	
					if(int(matriz[i][j]) == 1):
						contador = contador + 1

	#Si n=0 y m=15
	elif(n==0 and m==15):
		for i in range(n+2):
			for j in range(m-1,m+1):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j],"n=0 y m=15") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:	
					if(int(matriz[i][j]) == 1):
						contador = contador + 1
	
	#Si 0<n<15 y m=0
	elif((n>0 and n<15) and m==0):
		for i in range(n-1,n+2):
			for j in range(m,m+2):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j],"0<n<15 y m=0") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:	
					if(int(matriz[i][j]) == 1):
						contador = contador + 1	
						
	#Si 0<n<15 y 0<m<15
	elif((n>0 and n<15) and (m>0 and m<15)):
		for i in range(n-1,n+2):
			for j in range(m-1,m+2):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j],"0<n<15 y 0<m<15") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:	
					if(int(matriz[i][j]) == 1):
						contador = contador + 1	

	#Si 0<n<15 y m=15
	elif((n>0 and n<15) and m==15):
		for i in range(n-1,n+2):
			for j in range(m-1,m+1):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j],"0<n<15 y m=15") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:	
					if(int(matriz[i][j]) == 1):
						contador = contador + 1

	#Si n=15 y m=0
	elif(n==15 and m==0):
		for i in range(n-1,n+1):
			for j in range(m,m+2):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j],"n=15 y m=0") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:	
					if(int(matriz[i][j]) == 1):
						contador = contador + 1

	#Si n=15 y 0<m<15
	elif(n==15 and (m>0 and m<15)):
		for i in range(n-1,n+1):
			for j in range(m-1,m+2):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j],"n=15 y 0<m<15") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:	
					if(int(matriz[i][j]) == 1):
						contador = contador + 1	

	#Si n=15 y m=15
	elif(n==15 and m==15):
		for i in range(n-1,n+1):
			for j in range(m-1,m+1):
				#print("n = ",i,"m = ",j, "valor = ",matriz[i][j],"n=15 y m=15") #BORRAR ESTO
				if(i==n and j==m):
					pass
				else:	
					if(int(matriz[i][j]) == 1):
						contador = contador + 1					

	#print("Contador=",contador,"buscando en m y n: ",n,m) #BORRAR ESTE PRINT
	vm = vidaMuerte(contador, valor)
	global tableroFuturo
	#Cambiar valor AUN FALTA VER COMO
	if(vm == True):
		tableroFuturo[n][m] = 1
	elif(vm == False):
		tableroFuturo[n][m] = 0
		
	contador = 0	
		
#Verificar vida o muerte de celula		
def vidaMuerte(c, v):
	if(v == 0):
		if(c==3):
			return True
		else:
			return False
	elif(v == 1):
		if(c==2 or c==3):
			return True
		elif(c<2):
			return False
		elif(c>3):
			return False

#Reiniciar tablero futuro	
def rellenarZero():
	global tableroFuturo
	tableroFuturo = np.zeros((16,16))

#Cambiar tableroFuturo por tablero
def cambio(t, tf):
	for i in range(16):
		for j in range(16):
			t[i][j] = tf[i][j]
	


#Iniciar el Juego
#Estado inicial

print("Estado inicial")
print(tablero)	
for i in range(60):
	print("/nIteración: ", i+1)
	buscarCelulas(tablero)
	print(tablero)
	v1 = tablero[15][15]
	v2 = tablero[15][14]
	v3 = tablero[14][15]
	if(v1 == 1 and v2 == 1 and v3 == 1):
		print("Llego hasta la meta.")
		break
	
	
