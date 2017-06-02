from datetime import datetime

def check_date(year, month, day):
    correct_date = None
    try:
        new_date = datetime(year, month, day)
        correct_date = True
    except ValueError:
        correct_date = False
    return correct_date

def is_leap_year(anio=None):
	"""
	Validate if the current year is leap year.
	"""
	bisiesto = False 
	# We test if the month of February of the current year has 29 days. 
	if check_date(anio, 2, 29):
		bisiesto = True
	return bisiesto

def string_to_date(str_date):
	"""
	Convert string to date.
	"""
	date = datetime.strptime(str_date, '%Y-%m-%d').date()
	return date
