from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, EmailField, 
                     SubmitField, ValidationError)
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

from models.users import User

################# Formulario de Registro ##################
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                    EqualTo('password_confirm', 
                                                            message='Las contraseñas deben coincidir')])
    password_confirm = PasswordField('Password Confirm', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    ######## Validar Correo Unico #########
    def validate_email(self, field):
        ######## Consultar si el correo existe en la base de datos #######
        if User.check_email(field.data):
            raise ValidationError('El correo ya existe')

    ######## Validar Username Unico #########
    def validate_username(self, field):
        ######## Consultar si el username existe en la base de datos #######
        if User.check_username(field.data):
            raise ValidationError('El username ya existe')
        
################# Formulario de Login ##################
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

################ Formulario de Perfil ################
class ProfileForm(FlaskForm):
    # username No se edita
    # password No se edita
    # email, Verificar antes de actualizar
    name = StringField('Nombre',
                             validators=[DataRequired(), Length(min=3, max=30)])
    ape_pat = StringField('Apellido Paterno', 
                            validators=[DataRequired(), Length(min=10, max=40)])
    ape_mat = StringField('Apellido Materno', 
                            validators=[DataRequired(), Length(min=10, max=40)])
    direction = StringField('Dirección', 
                            validators=[DataRequired(), Length(min=10, max=80)])
    image = FileField('Imagen de Perfil', 
                      validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Solo se admiten archivos con extension (jpg, png, jpeg) por favor verifique que su imagen corresponda')])
    submit = SubmitField('Actualizar')