import matplotlib.pyplot as plt
import math

# note that plot function does not check if the string is secure,
# thus, this is not a safe code (needs improvement on this field).

def all_domain_function(function):
	def f(x):
		try:
			return function(x)
		except ValueError:
			return None
		except ZeroDivisionError:
			return None
	return f

math_dict = vars(math)
def plot(function, x_range=[-50,50], step=1):
	if type(function) is str:
		function  = eval(f"lambda x:{function}",math_dict)
	x_range = range(*x_range,step)
	function = all_domain_function(function)
	plt.plot(list(x_range),[function(x) for x in x_range])
	plt.show()
