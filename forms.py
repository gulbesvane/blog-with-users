from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


valid_mail = Email(message="not a valid email")


class RegisterForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), valid_mail])
    password = PasswordField(label='password', validators=[DataRequired()])
    name = StringField("name", validators=[DataRequired()])
    submit = SubmitField("Sign me up!")


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), valid_mail])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField("Log in!")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")