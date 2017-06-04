from wtforms import Form, StringField, IntegerField, FloatField
from wtforms import validators




class CommentForm(Form):
	fl = FloatField('Flujo', [validators.NumberRange(min=0, max=5.02, message='Introduce un valor en el intervalo de 0 a 5.02.')
									, validators.Required(message='Introduce un numero')])

