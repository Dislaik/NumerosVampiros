def get_data(lista):
	file = open('vampiro_in.txt', 'r')
	#lista = []
	for x in file.readlines():
		lista.append(x)
	file.close()
	lista = ''.join(lista)
	lista = lista.split()
	return lista

def data_to_list(lista):
	j=0
	for i in lista:
		lista[j]=i.rstrip("\n")
		j += 1
	print(lista)

def genera(n, lista):
	lista = lista[:]
	permutaciones = []
	ceros = []
	for i in range (n):
		ceros.append(0)
	permutaciones.append(lista[:])
	i = 0
	while i < n:
		if ceros[i] < i:
			if i%2 == 0:
				tmp = lista[0]
				lista[0] = lista[i]
				lista[i] = tmp
			else:
				tmp = lista[ceros[i]]
				lista[ceros[i]] = lista[i]
				lista[i] = tmp
			permutaciones.append(lista[:])
			ceros[i] += 1
			i = 0
		else:
			ceros[i] = 0
			i += 1
	return permutaciones

def comparate(lista_2):
	i = 0
	while i < len(lista_2):
		to_list = lista_2[i]
		test = list(to_list)
		leer = len(test)
		n = leer
		lista = test
		permutaciones = genera(n, lista)
		j = 0
		while j < len(permutaciones):
			if len(lista) <= 3:
				a = 'FALSE'
				print('No cumple una condición (Numero par no primo) =', a)
			else:
				x = permutaciones[j][:int(leer/2)]
				y = permutaciones[j][int(leer/2):]
				x = ''.join(x)
				y = ''.join(y)
				if x[-1:] == '0' and y[-1:] == '0':
					a = 'FALSE'
					print('No cumple una condición (Colmillos terminan en 0) =', a)
				else:
					result = int(x) * int(y)
					if result != int(to_list):
						a = 'FALSE'
						print(result, '=', a)
					else:
						a = 'TRUE'
						print(result, '=', a, '<-- Número vampiro encontrado!')
						break
			j += 1
		save.append(a + '\n')
		i += 1

def set_data(lista):
	file = open('salida.txt', 'w')
	for i in lista:
		file.write(i)
	file.close()

if __name__ == '__main__':
	save = []
	number = []
	get_data(number)
	data_to_list(number)
	comparate(number)
	set_data(save)
