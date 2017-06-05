import forms, acciones, minimalmodbus, time
from flask import Flask, render_template, request


title = "LABINTAHP"
flag=0
f=0
#port='/dev/tty.wchusbserial14220'
#nodo=2
#variador = minimalmodbus.Instrument(port, nodo)
#variador

def Activar():
	acciones.Activar()
	global flag
	flag=1

def Desactivar():
	acciones.Desactivar()
	global flag
	flag=0

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
	comment_form = forms.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		if flag == 1:
			global f
			print flag
			a = comment_form.fl.data
			f = acciones.Conversion(a)
			print f
#			acciones.EscribirFrecuencia(258,f)
		elif flag == 0:
			return "Activa el variador de frecuencia"
	return render_template('index.html', title = title, form = comment_form, f=f)


@app.route('/process', methods = ['GET', 'POST'])
def activate():
	
	if request.method == 'POST' and flag == 0:
		Activar()
		return "El variador de frecuencia se ha activado"

	elif request.method == 'POST' and flag == 1:
		Desactivar()
		return "El variador de frecuencia se ha desactivado"
	return render_template('index.html', title = title, form = comment_form, f=f )

if __name__ == '__main__':
	app.run(debug = True, port=8000)
#	app.run(debug = True, host=10.8.0.99, port=80)

