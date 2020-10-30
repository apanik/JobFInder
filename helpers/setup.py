from django.contrib.auth.models import User

from exam.models import ExamCategory, ExamLevel
from question.models import Subject, Topics, SubTopics, Question, Difficulty, QuestionType
from questionnaire.models import Questionnaire


def subject(self):
    sub1 = Subject(name='Machine')
    sub2 = Subject(name='Python')
    sub1.save()
    sub2.save()
    self.subject1 = sub1
    self.subject2 = sub2

def topic(self):
    top1 = Topics(name='Regression', subject_id=self.subject1)
    top2 = Topics(name='Basic Python', subject_id=self.subject2)
    top1.save()
    top2.save()
    self.topic1 = top1
    self.topic2 = top2

def sub_topic(self):
    sub_top1 = SubTopics(name='Regression', subject=self.subject1, topics=self.topic1)
    sub_top2 = SubTopics(name='Regression', subject=self.subject2, topics=self.topic2)
    sub_top1.save()
    sub_top2.save()
    self.subtopic1 = sub_top1
    self.subtopic2 = sub_top2

def qtype(self):
    typ1 = QuestionType(name='Checkbox')
    typ2 = QuestionType(name='Radio Button')
    typ1.save()
    typ2.save()
    self.qtyp1 = typ1
    self.qtyp2 = typ2

def difficulty(self):
    diff1 = Difficulty(name='Easy')
    diff2 = Difficulty(name='Medium')
    diff1.save()
    diff2.save()
    self.difficulty1 = diff1
    self.difficulty2 = diff2

def question(self):
    ques1 = Question(question='Why we split data into train and test?', subject=self.subject1, topic=self.topic1,
                     sub_topic=self.subtopic1, qtype=self.qtyp1, difficulties=self.difficulty1, status=2)
    ques2 = Question(
        question='The minsplit parameter to split() specifies the minimum number of splits to make to the input string',
        subject=self.subject2, topic=self.topic2,
        sub_topic=self.subtopic2, qtype=self.qtyp2, difficulties=self.difficulty2, status=2)
    ques1.save()
    ques2.save()
    self.question1 = ques1
    self.question2 = ques2

def questionnaire(self):
    questionnaire1 = Questionnaire(name='Questionnaire One', subject=self.subject1, topic=self.topic1, sub_topic=self.subtopic1)
    questionnaire1.save()
    self.questionnaire1 = questionnaire1

def exam_category(self):
    e_category1 = ExamCategory(name='Category')
    e_category1.save()
    self.exam_category1 = e_category1

def exam_level(self):
    e_level1 = ExamLevel(name='Beginner')
    e_level1.save()
    self.exam_level1 = e_level1