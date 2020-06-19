# https://docs.python.org/3/tutorial/venv.html
# This is just a list of commands. It doesn't work here becase each line run in a sub shell in make
init-venv:
	python3 -m venv pil
activate:
	source pil/bin/activate
deactivate:
	deactivate
