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
	lst_fact = fecha_actual.split('-')
	lst_fini = fecha_inicio.split('-')
	
	anios = int(lst_fact[0]) - int(lst_fini[0])
	meses = int(lst_fact[1]) - int(lst_fini[1])

	if meses < 0:
		meses = meses + 12 
		anios = anios - 1
		
	return meses



fecha_inicio = '1989-11-16'
fecha_actual = '2017-05-26'

semanas = calc_ant_semanas(fecha_inicio, fecha_actual)
print(semanas)

tiempo = calc_ant_tiempo(fecha_inicio, fecha_actual) 
print(tiempo)