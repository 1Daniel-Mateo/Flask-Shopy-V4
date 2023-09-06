from flask_wtf import FlaskForm
from wtforms import StringField,EmailField,PasswordField,SubmitField
from wtforms.validators import InputRequired

class NuevoCliente(FlaskForm):
    userName=StringField("Nombre del cliente:",
                       validators= [InputRequired(message="por favor ingresa un nombre de cliente")])

    email=EmailField("Correo de cliente:",
                       validators= [InputRequired(message="por favor ingresa el correo del cliente")])
    
    password=PasswordField("Contraseña de cliente:",
                       validators= [InputRequired(message="por favor ingresa la contrasela del cliente")])
    
    submit = SubmitField("Registrar Cliente")
