from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
import pandas as pd
import os
from django.conf import settings

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
    
@receiver(post_save, sender=Test)
def update_result_signal(sender, instance, created, **kwargs):
    if created:
        mans = pd.read_csv(os.path.join(settings.BASE_DIR, str(instance.model_answer_key)))
        mans= pd.DataFrame(data=mans)
        rsheet = pd.read_csv(os.path.join(settings.BASE_DIR, str(instance.response_sheet)))
        rsheet= pd.DataFrame(data=rsheet)
        names, emails, scores = [], [], []
        for name in rsheet['Name']:
            names.append(name)
        for email in rsheet['Email']:
            emails.append(email)
        # score generation logic here
        for i in range(len(names)):
            scores.append(20)
        Result.objects.create(test=instance,names=names,emails=emails, scores=scores)
    instance.result.save()
