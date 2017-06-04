def Activar():
#	variador.write_register(9,2) #Parametro b000=0002
#	variador.write_register(15,4) #Parametro b004=0004
	print "Activado"


def Desactivar():
#	variador.write_register(9,0) #Parametro b000=0000
#	variador.write_register(15,0) #Parametro b004=0000
	print "Desactivado"

def Arrancar():
	variador.write_register(257,1,0)

def Conversion(flujo):
	c=60
	b=5.02
	d=(flujo*c)/b
	e=round(d,2)
	f= e*100
	g= int(f)
	return g

def EscribirFrecuencia(registro,frecuencia):
	time.sleep(1)
	variador.write_register(registro,frecuencia) 