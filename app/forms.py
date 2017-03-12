from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField,SelectField,FileField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
class dataform(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
   # password = PasswordField('Password', validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    age = IntegerField("age",validators=[InputRequired()])
    biography= StringField('biography',validators= [InputRequired()])
    gender =  SelectField('gender', choices =[('female','female'),('male','male')],validators=[InputRequired()])
    image = FileField("file", validators=[InputRequired()])