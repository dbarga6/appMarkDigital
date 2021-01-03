from flask_wtf import FlaskForm
from wtforms import TextField,  SubmitField,  StringField,  Form, IntegerField, DateField

class CargarTweetForm(FlaskForm):
   
    search = StringField("search")
    maximo = IntegerField('maximo')
    fecha =  DateField('fecha_hasta')
    submit = SubmitField('Cargar')

class ObtenerTweetForm(FlaskForm):
   
    coleccion = StringField("coleccion")
    submit = SubmitField('Buscar')
    
