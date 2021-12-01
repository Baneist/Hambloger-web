from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
    name = StringField("请输入您的用户名: ", validators=[DataRequired()])
    submit = SubmitField("登录")

class EditProfileForm(FlaskForm):
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('地址', validators=[Length(0, 64)])
    about_me = StringField('个人简介', validators=[Length(0, 64)])
    submit = SubmitField('提交')

class PostForm(FlaskForm):
    body = TextAreaField("想写什么？", validators=[DataRequired()])
    submit = SubmitField('写完了')
