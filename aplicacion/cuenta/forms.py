from flask_wtf import FlaskForm
from wtforms import IntegerField, PasswordField, StringField
from wtforms import SelectField
from wtforms import SubmitField
from wtforms.validators import DataRequired, Email

class Formulariologin (FlaskForm): 
    usuariologin = StringField ("Usuario", validators=[DataRequired("Ingrese su usuario")])
    contraseñalogin = PasswordField ("Contraseña", validators=[DataRequired("Ingrese su contraseña")])
    submitlogin = SubmitField('Iniciar Sesión')

class Formularioregistro (FlaskForm): 
    usuarioreg = StringField ("Usuario", validators=[DataRequired("Ingrese su usuario")])
    correoreg = StringField ("Correo electrónico", validators=[DataRequired("Ingrese su correo electrónico"), Email(message="Ingrese un correo valido")])
    contraseñareg = PasswordField ("Contraseña", validators=[DataRequired("Ingrese su contraseña")])
    submitreg = SubmitField('Registrarse')  