from datetime import datetime


def calc_semanas(fecha_inicio, fecha_actual):
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


fecha_inicio = '1989-11-16'
fecha_actual = '2017-05-26'
data = calc_semanas(fecha_inicio, fecha_actual)
print(data)
