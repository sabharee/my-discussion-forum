from django.db import models


class Question(models.model):
    question_text = models.CharFiels(max_length=200)
    pub_date = model.DateTimeField('date published')


class Choice(models.model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.ItegerField(default=0)