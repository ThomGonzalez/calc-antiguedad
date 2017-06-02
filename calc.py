from datetime import datetime
from datetime import date
from utils import to_date, first_day_month, previous_day_month

def get_days(fecha_desde, fecha_hasta):
	days = (fecha_hasta.day - fecha_desde.day) + 1
	return days

def dias360(fecha_desde, fecha_hasta):
	day = (fecha_hasta.day - fecha_desde.day) 
	month = (fecha_hasta.month - fecha_desde.month) * 30
	year = (fecha_hasta.year - fecha_desde.year) * 360 

	days_passed =  day + month + year
	days = round((days_passed / 30) * 30)
	return days

def calc_weeks(fecha_inicio, fecha_actual):
	"""
	Calculation of seniority in weeks.
	"""
	data = {}
	fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
	fecha_actual = datetime.strptime(fecha_actual, '%Y-%m-%d').date()
	# Resta numero de dias.
	numero = (fecha_actual - fecha_inicio)
	# Obtener número de días, sumar mas 1 y dividir entre 7.
	semanas = ((numero.days + 1) / 7)
	semanas = int(semanas)
	data['weeks'] = semanas
	return data
	
def calc_days(fecha_desde, fecha_hasta):
	"""
	Calculation of seniority for the elapsed time.
	"""
	data = {}
	start_date = to_date(fecha_desde)
	end_date = to_date(fecha_hasta)
	first_date = first_day_month(start_date)
	prev_date = previous_day_month(end_date)
	
	days_360 = dias360(fecha_desde=first_date, fecha_hasta=prev_date)
	day = get_days(fecha_desde=start_date, fecha_hasta=end_date)
	total_days = days_360 + day

	years = int(total_days / 360)
	months = int((total_days - 360 * years) / 30)
	days = total_days - (years * 360 + months * 30)
	
	data['years'] = years
	data['months'] = months
	data['days'] = days

	return data


fecha_desde = '2015-12-25'
fecha_hasta = '2017-06-02'

data = calc_weeks(fecha_desde, fecha_hasta)
print(data)

data = calc_days(fecha_desde, fecha_hasta)
print(data)


