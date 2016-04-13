from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField

from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from .models import Author, Post


class LoginForm(Form):
    username = StringField('Username: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')

    def validate(self):
        return True


class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    published = SelectField('Status', choices=[('1', 'Published'), ('0', 'Draft')], validators=[DataRequired()])
    short_desc = TextAreaField("Front page display", validators=[DataRequired()])
    body = TextAreaField("What's on your mind?", validators=[DataRequired()])
    tags = StringField('Tags')

    def validate_title(self, title_field):
        if Post.query.filter_by(title=title_field.data).first():
            raise ValidationError('This title has already been used.')
