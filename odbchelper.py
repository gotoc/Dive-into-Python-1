""" odbchelper.py"""


def buildConnectionString(params):
	"""Build a connection string from a dictionary of parameters.

	Returns string."""

	return ";".join(["%s=%s" % (k, v) for k, v in params.items()])


""" 	__name__ is an attribute of the function.
		Other attributes can be accessed with dir(function or library):
		__doc__ for the docstring ie the first line of the function in tripple quotes.
		__file__ for the filename.
		__builtins__ for the built in Python functions.

		And remember, everything in Python is an object. Functions, modules, lists, variables.
"""

def fib(n):
	""" Prints the Fibonacci series.

		Returns the Fibonacci series. """
	print 'n = ', n
	if n > 1:
		return n * fib(n-1)
	else:
		print "Nothing to see here!"
		return 1


""" By testing if __name__ is __main__ you can test the module as a standalone piece of code.
	If the file is run directly the value of __name__ is __main__ so the indented code runs.
	If the file is imported as a module, the value of name is something else, maybe the name of the file.
	"""

if __name__ == "__main__":

	myParams = {
		"server" : "mpilgrim", \
		"database" : "master", \
		"uid" : "sa", \
		"pwd" : "secret" \
	}

	print buildConnectionString(myParams)
	fib(5)

	print "Hey, you ran me from the command line!"
	print "You could test me from here."
	print "My name attribute is: ", __name__
	print "Or import me to access the modules functions."
	


