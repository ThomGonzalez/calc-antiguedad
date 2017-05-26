from datetime import datetime


def calc_ant_semanas(fecha_inicio, fecha_actual):
	"""
	Cálcula antigüedad en semanas.
	"""
	fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
	fecha_actual = datetime.strptime(fecha_actual, '%Y-%m-%d').date()
	# Resta numero de dias.
	numero = (fecha_actual - fecha_inicio)
	# Obtener número de días, sumar mas 1 y dividir entre 7.
	semanas = ((numero.days + 1) / 7)
	semanas = int(semanas)

	return semanas

def calc_ant_tiempo(fecha_inicio, fecha_actual):
	"""
	Cálculo de antiguedad por el timepo transcurrido.
	"""

	data = {}

	lst_fact = fecha_actual.split('-')
	lst_fini = fecha_inicio.split('-')
	
	anios = int(lst_fact[0]) - int(lst_fini[0])
	meses = int(lst_fact[1]) - int(lst_fini[1])
	dias = int(lst_fact[2]) - int(lst_fini[2])

	dias_mes_anterior = 0
	mes_actual = int(lst_fact[1])

	if dias < 0:
		meses -= 1
		# Ahora hay que sumar a $dias los dias que tiene el mes anterior de la fecha actual 
		if mes_actual == 1:
			dias_mes_anterior = 31
		elif mes_actual == 2:
			dias_mes_anterior = 31
		elif mes_actual == 3:
			dias_mes_anterior = 28
		elif mes_actual == 4:
			dias_mes_anterior = 31
		elif mes_actual == 5:
			dias_mes_anterior = 30
		elif mes_actual == 6:
			dias_mes_anterior = 31
		elif mes_actual == 7:
			dias_mes_anterior = 30
		elif mes_actual == 8:
			dias_mes_anterior = 31
		elif mes_actual == 9:
			dias_mes_anterior = 31
		elif mes_actual == 10:
			dias_mes_anterior = 30
		elif mes_actual == 11:
			dias_mes_anterior = 31
		elif mes_actual == 12:
			dias_mes_anterior = 30

		dias = dias + dias_mes_anterior

	if meses < 0:
		meses = meses + 12 
		anios = anios - 1

	data['anios'] = anios
	data['meses'] = meses
	data['dias'] = dias
		
	return data


fecha_inicio = '1989-11-16'
fecha_actual = '2017-05-26'

data = calc_ant_semanas(fecha_inicio, fecha_actual)
print("Semanas: %s" % data)

data = calc_ant_tiempo(fecha_inicio, fecha_actual) 
print("Años: %s Meses: %s Dias: %s" % (data['anios'], data['meses'], data['dias']))