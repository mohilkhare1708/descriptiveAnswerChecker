from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
import pandas as pd
import os
import string
import random
from django.conf import settings
from algos.attributeCheck import cleanSentence, keywordsChecker, lengthChecker, lcsChecker

a=0.33
b = 0.5
c = 0.17
N = 5

class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    model_answer_key = models.FileField(upload_to='modelAns/')
    response_sheet = models.FileField(upload_to='studentAns/')
    no_of_ans = models.IntegerField()
    total_marks = models.IntegerField()
    passing_marks = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.test_name

class Result(models.Model):
    test = models.OneToOneField(Test, on_delete=models.CASCADE)
    names = ArrayField(models.CharField(max_length=100))
    emails = ArrayField(models.CharField(max_length=100))
    scores = ArrayField(models.IntegerField())
    total_students = models.IntegerField(default=75)
    mean_percentage = models.IntegerField(default=70)
    success_rate = models.IntegerField(default=90)
    high_score = models.IntegerField(default=20)

    def __str__(self):
        return self.test.test_name + "'s Result"

    
@receiver(post_save, sender=Test)
def update_result_signal(sender, instance, created, **kwargs):
    if created:
        mans = pd.read_csv(os.path.join(settings.BASE_DIR, str(instance.model_answer_key)))
        mans= pd.DataFrame(data=mans)
        rsheet = pd.read_csv(os.path.join(settings.BASE_DIR, str(instance.response_sheet)))
        rsheet= pd.DataFrame(data=rsheet)
        names, emails, scores, rollno, answer, passing = [], [], [], [], [], 0
        modelAns = mans['Q1'][0]
        # modelAns = cleanSentence([modelAns])
        for i in range(len(rsheet)):
            names.append(rsheet['Name'][i])
            emails.append(rsheet['Email'][i])
            rollno.append(rsheet['Roll Number'][i])
            answer.append(rsheet['Answer'][i])
        # score generation logic here
        for i in range(len(answer)):
            # cleaned = cleanSentence([answer[i]])
            # print(cleaned)
            lCS_score = lcsChecker(modelAns, answer[i])
            len_score = lengthChecker(modelAns, answer[i])
            keyword_score = keywordsChecker(modelAns, answer[i])
            print(lCS_score, len_score, keyword_score)
            marks = a * lCS_score + c * len_score + b * keyword_score
            scores.append(min(marks*100, instance.total_marks))
            print(instance.passing_marks, "hi", marks)
            if marks >= instance.passing_marks:
                print("hi")
                passing += 1
        print("broooo", float(passing), len(scores))
        successRate, totalStudents = (float(float(passing) / float(len(scores))) * 100), len(names)
        meanPercentage = (sum(scores)/(instance.total_marks*totalStudents))*100
        highScore = (max(scores) / instance.total_marks) * 100
        Result.objects.create(test=instance,names=names,emails=emails,scores=scores,total_students=totalStudents,mean_percentage=meanPercentage,success_rate=successRate,high_score=highScore)
    instance.result.save()
