import os
from xml.etree import ElementTree as ET
from xml.dom import minidom
from flask import render_template, url_for, flash, redirect, render_template_string
from kbc import app
from kbc.forms import XMLQuestionForm


@app.route("/",methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    form = XMLQuestionForm()
    if form.validate_on_submit():
        root = ET.Element('QuizXML')
        tags = ET.Element('QTags')        
        tag = ET.SubElement(tags, 'QTag')
        tag.text = form.tags.data
        root.append(tags)
        questionBank = ET.Element('QuestionBank')

        for i in range(14):
            questionN = ET.SubElement(questionBank, 'Question'+ str(i+1))
            question = ET.SubElement(questionN, 'Question')
            question.text = form.question[i].data

            optionA = ET.SubElement(questionN, 'OptionA')
            optionA.text = form.optionA[i].data

            optionB = ET.SubElement(questionN, 'OptionB')
            optionB.text = form.optionB[i].data

            optionC = ET.SubElement(questionN, 'OptionC')
            optionC.text = form.optionC[i].data

            optionD = ET.SubElement(questionN, 'OptionD')
            optionD.text = form.optionD[i].data
            
            answer = ET.SubElement(questionN, "Answer")
            answer.text = form.answer[i].data

            timer = ET.SubElement(questionN, "Timer")
            timer.text = str(form.timer[i].data)            

        root.append(questionBank)

        advertisement = ET.Element('Advertisement')
        comment = ET.Comment('This will be added later')
        root.append(comment)
        root.append(advertisement)

        tree = ET.ElementTree(root)

        xmlStr = minidom.parseString(ET.tostring(root,encoding='utf8', method='xml')).toprettyxml(indent="\t")

        with open("testFile.xml", "w") as f:
            f.write(xmlStr) 
    return render_template('home.html', title='Home', form=form)