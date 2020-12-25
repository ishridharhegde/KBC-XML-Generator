from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField, FieldList
from wtforms.validators import DataRequired, Length

class XMLQuestionForm(FlaskForm):
    tags = StringField('Tags', validators=[Length(max=50)])
    question = FieldList(StringField('Question', validators=[DataRequired(), Length(max=395)]), min_entries=14, max_entries=14 )
    optionA = FieldList(StringField('Option A', validators=[DataRequired(), Length(max=85)]), min_entries=14, max_entries=14)
    optionB = FieldList(StringField('Option B', validators=[DataRequired(), Length(max=85)]), min_entries=14, max_entries=14)
    optionC = FieldList(StringField('Option C', validators=[DataRequired(), Length(max=85)]), min_entries=14, max_entries=14)
    optionD = FieldList(StringField('Option D', validators=[DataRequired(), Length(max=85)]), min_entries=14, max_entries=14)
    
    answer = FieldList(SelectField('Answer', validators=[DataRequired()], choices=[(None,'<Select an answer>'),('A','Option A'),('B','Option B'),('C','Option C'),('D','Option D')]), min_entries=14, max_entries=14)
    timer = FieldList(IntegerField('Timer', default=60),  min_entries=14, max_entries=14)

    submit = SubmitField('Generate XML')



