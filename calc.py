from datetime import datetime


def check_date(year, month, day):
    correct_date = None
    try:
        new_date = datetime(year, month, day)
        correct_date = True
    except ValueError:
        correct_date = False
    return correct_date


def es_bisiesto(anio=None):
	"""
	Valida si el año actual es bisiesto.
	"""
	bisiesto = False 
	# Probamos si el mes de febrero del año actual tiene 29 días 
	if check_date(anio, 2, 29):
		bisiesto = True
	return bisiesto


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
	anio_actual = int(lst_fact[0])
	mes_actual = int(lst_fact[1])
	# Sumar días mas uno.
	dias += 1
	
	if dias < 0:
		meses -= 1
		# Ahora hay que sumar a $dias los dias que tiene el mes anterior de la fecha actual 
		if mes_actual == 1:
			dias_mes_anterior = 31
		elif mes_actual == 2:
			dias_mes_anterior = 31
		elif mes_actual == 3:
			if es_bisiesto(anio=anio_actual):
				dias_mes_anterior = 29
			else: 
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


fecha_inicio = '2008-03-31'
fecha_actual = '2009-03-02'

data = calc_ant_semanas(fecha_inicio, fecha_actual)
print("Semanas: %s" % data)

data = calc_ant_tiempo(fecha_inicio, fecha_actual) 
print("Años: %s Meses: %s Dias: %s" % (data['anios'], data['meses'], data['dias']))
