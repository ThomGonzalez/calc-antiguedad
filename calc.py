from datetime import datetime, timedelta
from datetime import date

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

def string_to_date(str_date):
	"""
	Convierte string a fecha.
	"""
	date = datetime.strptime(str_date, '%Y-%m-%d').date()
	return date

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



def first_day_of_month(year, month):
	"""
	Obtiene el primer día del mes y año.
	"""
	return date(year, month, 1)

def get_first_day_of_month(fecha_desde):
	"""
	Obtiene el primer día del mes del año actual.
	"""
	date = fecha_desde.replace(day=1)
	return date

def get_previous_day_of_month(fecha_hasta):
	date = fecha_hasta - timedelta(days=fecha_hasta.day)
	return date

def dias360(fecha_desde, fecha_hasta):
	day = (fecha_hasta.day - fecha_desde.day) 
	month = (fecha_hasta.month - fecha_desde.month) * 30
	year = (fecha_hasta.year - fecha_desde.year) * 360 

	days_passed =  day + month + year
	days =  (days_passed / 30) * 30

	return days

def get_days(fecha_desde, fecha_hasta):
	days = (fecha_hasta.day - fecha_desde.day) + 1
	return days

def calc_ant_dias(fecha_desde, fecha_hasta):
	start_date = string_to_date(fecha_desde)
	end_date = string_to_date(fecha_hasta)

	first_date = get_first_day_of_month(start_date)
	prev_date = get_previous_day_of_month(end_date)
	
	days = dias360(fecha_desde=first_date, fecha_hasta=prev_date)
	day = get_days(fecha_desde=start_date, fecha_hasta=end_date)

	total_days = days + day
	print(total_days)

fecha_desde = '1989-11-16'
fecha_hasta = '2017-06-02'

# data = calc_ant_semanas(fecha_desde, fecha_hasta)
# print("Semanas: %s" % data)

# data = calc_ant_tiempo(fecha_desde, fecha_hasta) 
# print("Años: %s Meses: %s Dias: %s" % (data['anios'], data['meses'], data['dias']))

calc_ant_dias(fecha_desde, fecha_hasta)


