import datetime

def fullDateNow():
	"""
	Outputs the datetime now in the following format: Sept 15, 1986
	"""
	return datetime.datetime.now().strftime("%B %d, %Y")
