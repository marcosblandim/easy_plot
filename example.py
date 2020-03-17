from easy_plot import *

def function(x):
	y = sin(x)**2
	return y

# plot(function, [-100,100])

# plot(lambda x: 10*(sqrt(100-x**2)),[-100,100])

# plot("10*(sqrt(100-x**2))",[-100,100])
def f(x):
	return 10*(sqrt(100-x**2))
	
plot(f,[-100,100])